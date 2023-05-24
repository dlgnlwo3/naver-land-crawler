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


import pandas as pd


class NaverLandCrawlerTab(QWidget):
    # 초기화
    def __init__(self):
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
        guiDto.tradTpCd = checked_tradTpCd
        guiDto.rletTpCd = checked_rletTpCd

        self.naver_land_crawler_thread = NaverLandCrawlerThread()
        self.naver_land_crawler_thread.log_msg.connect(self.log_append)
        self.naver_land_crawler_thread.naver_land_crawler_finished.connect(self.naver_land_crawler_finished)
        self.naver_land_crawler_thread.setGuiDto(guiDto)

        self.naver_land_crawler_start_button.setDisabled(True)
        self.naver_land_crawler_stop_button.setDisabled(False)
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
        print(f"thread_is_running: {self.naver_land_crawler_thread.isRunning()}")

    def open_save_path_button_clicked(self):
        os.startfile(self.config.today_output_folder)

    # 메인 UI
    def initUI(self):
        # 지역
        city_groupbox = QGroupBox("지역 선택")
        self.city_combobox = QComboBox()
        self.city_combobox.addItems(CityEnum.list())

        city_inner_layout = QHBoxLayout()
        city_inner_layout.addWidget(self.city_combobox)
        city_groupbox.setLayout(city_inner_layout)

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

        # # 매물유형
        # rletTpCd_groupbox = QGroupBox("매물유형")
        # self.rletTpCd_combobox = QComboBox()
        # self.rletTpCd_combobox.addItems(rletTpCdEnum.list())

        # rletTpCd_inner_layout = QHBoxLayout()
        # rletTpCd_inner_layout.addWidget(self.rletTpCd_combobox)
        # rletTpCd_groupbox.setLayout(rletTpCd_inner_layout)

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
        start_stop_groupbox = QGroupBox("시작 중지")
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
        top_layout.addWidget(city_groupbox, 4)
        top_layout.addStretch(6)

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
