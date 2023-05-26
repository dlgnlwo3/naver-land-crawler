import sys
import warnings

warnings.simplefilter("ignore", UserWarning)
sys.coinit_flags = 2
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from datetime import *

from threads.naver_land_search_keyword_thread import NaverLandSearchKeywordThread
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


class NaverLandSearchKeywordTab(QWidget):
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
    def naver_land_search_keyword_start_button_clicked(self):
        if self.search_keyword.text() == "":
            QMessageBox.information(self, "입력", f"검색어를 입력해주세요.")
            return

        guiDto = GUIDto()
        guiDto.search_keyword = self.search_keyword.text()

        self.naver_land_search_keyword_thread = NaverLandSearchKeywordThread()
        self.naver_land_search_keyword_thread.log_msg.connect(self.log_append)
        self.naver_land_search_keyword_thread.naver_land_search_keyword_finished.connect(
            self.naver_land_search_keyword_finished
        )
        self.naver_land_search_keyword_thread.setGuiDto(guiDto)

        self.naver_land_search_keyword_start_button.setDisabled(True)
        self.naver_land_search_keyword_stop_button.setDisabled(False)
        self.naver_land_search_keyword_thread.start()

    # 중지 클릭
    @Slot()
    def naver_land_search_keyword_stop_button_clicked(self):
        print(f"search stop clicked")
        self.log_append(f"중지 클릭")
        self.naver_land_search_keyword_finished()

    # 작업 종료
    @Slot()
    def naver_land_search_keyword_finished(self):
        print(f"search thread finished")
        self.log_append(f"작업 종료")
        self.naver_land_search_keyword_thread.stop()
        self.naver_land_search_keyword_start_button.setDisabled(False)
        self.naver_land_search_keyword_stop_button.setDisabled(True)
        print(f"thread_is_running: {self.naver_land_search_keyword_thread.isRunning()}")

    def open_save_path_button_clicked(self):
        os.startfile(self.config.today_output_folder)

    # 메인 UI
    def initUI(self):
        # 키워드 입력창
        search_keyword_groupbox = QGroupBox("검색어")
        self.search_keyword = QLineEdit("")
        self.search_keyword.setPlaceholderText("지역명, 단지명, 필터조건으로 검색 ex) 남양주시 다산동 오피스텔 전세...")

        search_keyword_inner_layout = QHBoxLayout()
        search_keyword_inner_layout.addWidget(self.search_keyword)
        search_keyword_groupbox.setLayout(search_keyword_inner_layout)

        # 시작 중지
        start_stop_groupbox = QGroupBox("작업 시작")
        self.open_save_path_button = QPushButton("저장 경로 열기")
        self.naver_land_search_keyword_start_button = QPushButton("시작")
        self.naver_land_search_keyword_stop_button = QPushButton("중지")
        self.naver_land_search_keyword_stop_button.setDisabled(True)

        self.open_save_path_button.clicked.connect(self.open_save_path_button_clicked)
        self.naver_land_search_keyword_start_button.clicked.connect(self.naver_land_search_keyword_start_button_clicked)
        self.naver_land_search_keyword_stop_button.clicked.connect(self.naver_land_search_keyword_stop_button_clicked)

        start_stop_inner_layout = QHBoxLayout()
        start_stop_inner_layout.addWidget(self.open_save_path_button)
        start_stop_inner_layout.addWidget(self.naver_land_search_keyword_start_button)
        start_stop_inner_layout.addWidget(self.naver_land_search_keyword_stop_button)
        start_stop_groupbox.setLayout(start_stop_inner_layout)

        # 로그 그룹박스
        log_groupbox = QGroupBox("로그")
        self.browser = QTextBrowser()

        log_inner_layout = QHBoxLayout()
        log_inner_layout.addWidget(self.browser)
        log_groupbox.setLayout(log_inner_layout)

        # 레이아웃 배치
        top_layout = QHBoxLayout()
        top_layout.addWidget(search_keyword_groupbox, 3)
        top_layout.addStretch(4)

        mid_layout = QHBoxLayout()
        mid_layout.addStretch(4)

        sec_layout = QHBoxLayout()

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
