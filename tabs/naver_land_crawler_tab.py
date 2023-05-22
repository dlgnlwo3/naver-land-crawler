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
        guiDto = GUIDto()

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

    def naver_land_crawler_all_checkbox_statechanged(self):
        print(self.naver_land_crawler_all_checkbox.isChecked())

        if self.naver_land_crawler_all_checkbox.isChecked():
            self.naver_land_crawler_count.setDisabled(True)
        else:
            self.naver_land_crawler_count.setDisabled(False)

    # 메인 UI
    def initUI(self):
        # 계정 정보
        account_file_groupbox = QGroupBox("계정 정보")
        self.account_file = QLineEdit()
        self.account_file.setDisabled(True)
        self.account_file_select_button = QPushButton("파일 선택")

        account_file_inner_layout = QHBoxLayout()
        account_file_inner_layout.addWidget(self.account_file)
        account_file_inner_layout.addWidget(self.account_file_select_button)
        account_file_groupbox.setLayout(account_file_inner_layout)

        # 전체 삭제
        naver_land_crawler_all_groupbox = QGroupBox("전체 삭제")
        self.naver_land_crawler_all_checkbox = QCheckBox("전체 삭제")

        self.naver_land_crawler_all_checkbox.stateChanged.connect(self.naver_land_crawler_all_checkbox_statechanged)

        naver_land_crawler_all_inner_layout = QHBoxLayout()
        naver_land_crawler_all_inner_layout.addWidget(self.naver_land_crawler_all_checkbox)
        naver_land_crawler_all_groupbox.setLayout(naver_land_crawler_all_inner_layout)

        # 삭제 횟수
        naver_land_crawler_count_groupbox = QGroupBox("삭제 횟수")
        self.naver_land_crawler_count = QLineEdit()
        self.naver_land_crawler_count.setValidator(QIntValidator(1, 999999))

        naver_land_crawler_count_inner_layout = QHBoxLayout()
        naver_land_crawler_count_inner_layout.addWidget(self.naver_land_crawler_count)
        naver_land_crawler_count_groupbox.setLayout(naver_land_crawler_count_inner_layout)

        # 시작 중지
        start_stop_groupbox = QGroupBox("시작 중지")
        self.naver_land_crawler_start_button = QPushButton("시작")
        self.naver_land_crawler_stop_button = QPushButton("중지")
        self.naver_land_crawler_stop_button.setDisabled(True)

        self.naver_land_crawler_start_button.clicked.connect(self.naver_land_crawler_start_button_clicked)
        self.naver_land_crawler_stop_button.clicked.connect(self.naver_land_crawler_stop_button_clicked)

        start_stop_inner_layout = QHBoxLayout()
        start_stop_inner_layout.addWidget(self.naver_land_crawler_start_button)
        start_stop_inner_layout.addWidget(self.naver_land_crawler_stop_button)
        start_stop_groupbox.setLayout(start_stop_inner_layout)

        # 제목 내용
        review_content_groupbox = QGroupBox("리뷰")
        self.review_title = QLineEdit()
        self.review_title.setPlaceholderText("제목")
        self.review_content = QPlainTextEdit()
        self.review_content.setPlaceholderText("내용")

        review_content_inner_layout = QVBoxLayout()
        review_content_inner_layout.addWidget(self.review_title)
        review_content_inner_layout.addWidget(self.review_content)
        review_content_groupbox.setLayout(review_content_inner_layout)

        # 로그 그룹박스
        log_groupbox = QGroupBox("로그")
        self.browser = QTextBrowser()

        log_inner_layout = QHBoxLayout()
        log_inner_layout.addWidget(self.browser)
        log_groupbox.setLayout(log_inner_layout)

        # 레이아웃 배치
        top_layout = QHBoxLayout()
        top_layout.addWidget(account_file_groupbox)

        mid_layout = QHBoxLayout()
        mid_layout.addStretch(4)
        mid_layout.addWidget(naver_land_crawler_all_groupbox, 2)
        mid_layout.addWidget(naver_land_crawler_count_groupbox, 3)
        mid_layout.addWidget(start_stop_groupbox, 4)

        bottom_layout = QHBoxLayout()
        # bottom_layout.addWidget(review_content_groupbox)

        log_layout = QVBoxLayout()
        log_layout.addWidget(log_groupbox)

        layout = QVBoxLayout()
        layout.addLayout(top_layout)
        layout.addLayout(mid_layout)
        layout.addLayout(bottom_layout)
        layout.addLayout(log_layout)

        self.setLayout(layout)
