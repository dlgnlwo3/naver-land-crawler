import sys
import warnings

warnings.simplefilter("ignore", UserWarning)
sys.coinit_flags = 2
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from datetime import *

from threads.naver_land_crawler_thread import NaverLandCrawlerThread
from dtos.gui_dto import GUIDto
from common.utils import *

from configs.coupang_review_crawler_config import CoupangReviewCrawlerConfig
from configs.coupang_review_crawler_config import CoupangReviewCrawlerData

from enums.city_enum import CityEnum
from enums.tradTpCd_enum import tradTpCdEnum
from enums.rletTpCd_enum import rletTpCdEnum

from api.naver_land_api import NaverLandAPI
import asyncio


import pandas as pd


class NaverLandCrawlerTab(QWidget):
    # 초기화
    def __init__(self):
        self.APIBot = NaverLandAPI()
        self.config = ProgramConfig()
        print(f"TODAY_OUTPUT_FOLDER: {self.config.today_output_folder}")

        super().__init__()
        self.initUI()

    # 로그 작성
    @Slot(str)
    def log_append(self, text):
        today = str(datetime.now())[0:10]
        now = str(datetime.now())[0:-7]
        self.browser.append(f"[{now}] {str(text)}")
        global_log_append(text)

    # 시작 클릭
    def naver_land_crawler_start_button_clicked(self):
        if self.dvsn_checkbox.isChecked():
            if self.dvsn_combobox.currentText() == "":
                QMessageBox.information(self, "입력", f"시/군/구를 선택해주세요.")
                return

        checked_tradTpCd = []
        print(self.tradTpCd_group)
        tradTpCd_checkbox: QCheckBox
        for tradTpCd_checkbox in self.tradTpCd_checkboxes_group:
            if tradTpCd_checkbox.isChecked():
                checked_tradTpCd.append(tradTpCd_checkbox.text())
        if len(checked_tradTpCd) <= 0:
            QMessageBox.information(self, "입력", f"거래 유형을 선택해주세요.")
            return
        print(checked_tradTpCd)

        checked_rletTpCd = []
        print(self.rletTpCd_group)
        rletTpCd_checkbox: QCheckBox
        for rletTpCd_checkbox in self.rletTpCd_checkboxes_group:
            if rletTpCd_checkbox.isChecked():
                checked_rletTpCd.append(rletTpCd_checkbox.text())
        if len(checked_rletTpCd) <= 0:
            QMessageBox.information(self, "입력", f"매물 유형을 선택해주세요.")
            return
        print(checked_rletTpCd)

        guiDto = GUIDto()
        guiDto.city = self.city_combobox.currentText()
        guiDto.dvsn_checkbox = self.dvsn_checkbox.isChecked()
        guiDto.dvsn = self.dvsn_combobox.currentText()
        guiDto.tradTpCd = checked_tradTpCd
        guiDto.rletTpCd = checked_rletTpCd

        self.naver_land_crawler_thread = NaverLandCrawlerThread()
        self.naver_land_crawler_thread.log_msg.connect(self.log_append)
        self.naver_land_crawler_thread.naver_land_crawler_finished.connect(self.naver_land_crawler_finished)
        self.naver_land_crawler_thread.setGuiDto(guiDto)

        self.naver_land_crawler_start_button.setDisabled(True)
        self.naver_land_crawler_stop_button.setDisabled(False)
        self.city_combobox.setDisabled(True)
        self.dvsn_checkbox.setDisabled(True)
        self.dvsn_combobox.setDisabled(True)
        rletTpCd_checkbox: QCheckBox
        for rletTpCd_checkbox in self.rletTpCd_checkboxes_group:
            rletTpCd_checkbox.setDisabled(True)
        tradTpCd_checkbox: QCheckBox
        for tradTpCd_checkbox in self.tradTpCd_checkboxes_group:
            tradTpCd_checkbox.setDisabled(True)

        self.naver_land_crawler_thread.start()

    # 중지 클릭
    @Slot()
    def naver_land_crawler_stop_button_clicked(self):
        print(f"search stop clicked")
        self.log_append(f"중지 클릭")
        self.naver_land_crawler_finished()

    # 작업 종료
    @Slot()
    def naver_land_crawler_finished(self):
        print(f"search thread finished")
        self.log_append(f"작업 종료")
        self.naver_land_crawler_thread.stop()
        self.naver_land_crawler_start_button.setDisabled(False)
        self.naver_land_crawler_stop_button.setDisabled(True)
        self.city_combobox.setDisabled(False)
        self.dvsn_checkbox.setDisabled(False)
        self.dvsn_combobox.setDisabled(False)
        rletTpCd_checkbox: QCheckBox
        for rletTpCd_checkbox in self.rletTpCd_checkboxes_group:
            rletTpCd_checkbox.setDisabled(False)
        tradTpCd_checkbox: QCheckBox
        for tradTpCd_checkbox in self.tradTpCd_checkboxes_group:
            tradTpCd_checkbox.setDisabled(False)
        print(f"thread_is_running: {self.naver_land_crawler_thread.isRunning()}")

    def open_save_path_button_clicked(self):
        os.startfile(self.config.today_output_folder)

    def city_combobox_textChanged(self):
        print(f"{self.city_combobox.currentText()}")
        try:
            dvsn_list = []
            dvsn_list = asyncio.run(
                self.APIBot.get_dvsn_list_from_cortarNo(
                    getattr(CityEnum, self.city_combobox.currentText()).value["cortarNo"]
                )
            )
            dvsn_list = [dict_dvsn["cortarName"] for dict_dvsn in dvsn_list]
        except Exception as e:
            self.log_append(f"시/군/구 정보 조회에 실패했습니다. 잠시 후 다시 시도해주세요.")
            dvsn_list = []
        self.set_dvsn_combobox(dvsn_list)

    def set_dvsn_combobox(self, dvsn_list):
        self.dvsn_combobox.clear()
        for dvsn in dvsn_list:
            self.dvsn_combobox.addItem(dvsn)

    # 메인 UI
    def initUI(self):
        # 시/도
        city_groupbox = QGroupBox("시/도")
        self.city_combobox = QComboBox()
        self.city_combobox.addItems(CityEnum.list())

        city_inner_layout = QHBoxLayout()
        city_inner_layout.addWidget(self.city_combobox)
        city_groupbox.setLayout(city_inner_layout)

        # 시/군/구
        dvsn_groupbox = QGroupBox("시/군/구")
        self.dvsn_checkbox = QCheckBox("시/군/구 단위 조회")
        self.dvsn_combobox = QComboBox()

        self.city_combobox_textChanged()
        self.city_combobox.currentTextChanged.connect(self.city_combobox_textChanged)

        dvsn_inner_layout = QHBoxLayout()
        dvsn_inner_layout.addWidget(self.dvsn_checkbox)
        dvsn_inner_layout.addWidget(self.dvsn_combobox)
        dvsn_groupbox.setLayout(dvsn_inner_layout)

        # 거래유형
        tradTpCd_groupbox = QGroupBox("거래유형")
        self.tradTpCd_group = QButtonGroup()
        self.tradTpCd_group.setExclusive(False)

        tradTpCd_inner_layout = QHBoxLayout()
        self.tradTpCd_checkboxes_group = []
        for tradTpCd in tradTpCdEnum.list():
            tradTpCd_checkbox = QCheckBox(tradTpCd)
            self.tradTpCd_checkboxes_group.append(tradTpCd_checkbox)
            self.tradTpCd_group.addButton(tradTpCd_checkbox)
            tradTpCd_inner_layout.addWidget(tradTpCd_checkbox)
        tradTpCd_groupbox.setLayout(tradTpCd_inner_layout)

        # 매물유형
        rletTpCd_groupbox = QGroupBox("매물유형")
        self.rletTpCd_group = QButtonGroup()
        self.rletTpCd_group.setExclusive(False)

        rletTpCd_inner_layout = QHBoxLayout()
        self.rletTpCd_checkboxes_group = []
        for rletTpCd in rletTpCdEnum.list():
            rletTpCd_checkbox = QCheckBox(rletTpCd)
            self.rletTpCd_checkboxes_group.append(rletTpCd_checkbox)
            self.rletTpCd_group.addButton(rletTpCd_checkbox)
            rletTpCd_inner_layout.addWidget(rletTpCd_checkbox)
        rletTpCd_groupbox.setLayout(rletTpCd_inner_layout)

        # 시작 중지
        start_stop_groupbox = QGroupBox("작업 시작")
        self.open_save_path_button = QPushButton("저장 경로 열기")
        self.naver_land_crawler_start_button = QPushButton("시작")
        self.naver_land_crawler_stop_button = QPushButton("중지")
        self.naver_land_crawler_stop_button.setDisabled(True)

        self.open_save_path_button.clicked.connect(self.open_save_path_button_clicked)
        self.naver_land_crawler_start_button.clicked.connect(self.naver_land_crawler_start_button_clicked)
        self.naver_land_crawler_stop_button.clicked.connect(self.naver_land_crawler_stop_button_clicked)

        start_stop_inner_layout = QHBoxLayout()
        start_stop_inner_layout.addWidget(self.open_save_path_button)
        start_stop_inner_layout.addWidget(self.naver_land_crawler_start_button)
        start_stop_inner_layout.addWidget(self.naver_land_crawler_stop_button)
        start_stop_groupbox.setLayout(start_stop_inner_layout)

        # 로그 그룹박스
        log_groupbox = QGroupBox("로그")
        self.browser = QTextBrowser()

        log_inner_layout = QHBoxLayout()
        log_inner_layout.addWidget(self.browser)
        log_groupbox.setLayout(log_inner_layout)

        # 레이아웃 배치
        top_layout = QHBoxLayout()
        top_layout.addWidget(city_groupbox, 3)
        top_layout.addWidget(dvsn_groupbox, 3)
        top_layout.addStretch(4)

        mid_layout = QHBoxLayout()
        mid_layout.addWidget(tradTpCd_groupbox, 4)
        mid_layout.addStretch(4)

        sec_layout = QHBoxLayout()
        sec_layout.addWidget(rletTpCd_groupbox)

        bottom_layout = QHBoxLayout()
        bottom_layout.addStretch(4)
        bottom_layout.addWidget(start_stop_groupbox, 4)

        log_layout = QVBoxLayout()
        log_layout.addWidget(log_groupbox)

        layout = QVBoxLayout()
        layout.addLayout(top_layout)
        layout.addLayout(mid_layout)
        layout.addLayout(sec_layout)
        layout.addLayout(bottom_layout)
        layout.addLayout(log_layout)

        self.setLayout(layout)
