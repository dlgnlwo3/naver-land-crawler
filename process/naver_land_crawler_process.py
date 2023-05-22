if 1 == 1:
    import sys
    import os

    sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))


from selenium import webdriver
from dtos.gui_dto import GUIDto

from configs.coupang_review_crawler_config import CoupangReviewCrawlerConfig
from configs.coupang_review_crawler_config import CoupangReviewCrawlerData


from common.utils import global_log_append
from common.chrome import get_chrome_driver_new
from common.selenium_activities import close_new_tabs, alert_ok_try

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains

from datetime import timedelta, datetime
import time

import pandas as pd

# import pandas as pd


class NaverLandCrawlerProcess:
    def __init__(self):
        self.default_wait = 10
        # self.driver = get_chrome_driver_new(is_headless=False, is_secret=True, move_to_corner=False)
        # self.driver.implicitly_wait(self.default_wait)

    def setGuiDto(self, guiDto: GUIDto):
        self.guiDto = guiDto

    def setLogger(self, log_msg):
        self.log_msg = log_msg

    # 전체작업 시작
    def work_start(self):
        print(f"process: work_start")

        try:
            print(f"process run")

        except Exception as e:
            print(e)


if __name__ == "__main__":
    process = NaverLandCrawlerProcess()
    process.work_start()
