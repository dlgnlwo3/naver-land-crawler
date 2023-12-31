if 1 == 1:
    import sys
    import warnings
    import os

    sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
    warnings.simplefilter("ignore", UserWarning)
    sys.coinit_flags = 2
from tkinter import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from dtos.gui_dto import *
from datetime import timedelta
from timeit import default_timer as timer

from process.naver_land_crawler_process import NaverLandCrawlerProcess

# import debugpy


class NaverLandCrawlerThread(QThread):
    log_msg = Signal(str)
    naver_land_crawler_finished = Signal()

    # 호출 시점
    def __init__(self):
        super().__init__()

    # guiDto세팅
    def setGuiDto(self, guiDto: GUIDto):
        self.guiDto = guiDto

    def run(self):
        try:
            # debugpy.debug_this_thread()

            self.log_msg.emit(f"시작")

            start_time = timer()

            process = NaverLandCrawlerProcess()

            process.setGuiDto(self.guiDto)

            process.setLogger(self.log_msg)

            if self.guiDto.dvsn_checkbox:
                process.work_start_from_dvsn()

            else:
                process.work_start_from_city()

            end_time = timer()

            progress_time = timedelta(seconds=end_time - start_time).seconds

            self.log_msg.emit(f"총 {str(progress_time)}초 소요되었습니다.")

        except Exception as e:
            print(f"작업 중 오류가 발생했습니다. {str(e)}")
            self.log_msg.emit(f"작업 중 오류가 발생했습니다. {str(e)}")

        self.naver_land_crawler_finished.emit()

    def stop(self):
        try:
            self.terminate()
        except Exception as e:
            print(e)
