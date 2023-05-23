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

import math

import pandas as pd

from enums.city_enum import CityEnum
from enums.rletTpCd_enum import rletTpCdEnum
from enums.tradTpCd_enum import tradTpCdEnum
from api.naver_land_api import NaverLandAPI
import asyncio


class NaverLandCrawlerProcess:
    def __init__(self):
        self.default_wait = 10
        # self.driver = get_chrome_driver_new(is_headless=False, is_secret=True, move_to_corner=False)
        # self.driver.implicitly_wait(self.default_wait)

    def setGuiDto(self, guiDto: GUIDto):
        self.guiDto = guiDto

    def setLogger(self, log_msg):
        self.log_msg = log_msg

    def get_cluster_max_page(self, cluster_count):
        cluster_max_page = math.ceil(cluster_count / 20)
        return cluster_max_page

    # 전체작업 시작
    def work_start(self):
        try:
            city_dict: dict = getattr(CityEnum, self.guiDto.city).value
            rletTpCd = getattr(rletTpCdEnum, self.guiDto.rletTpCd).value
            tradTpCd = getattr(tradTpCdEnum, self.guiDto.tradTpCd).value
            print(city_dict)
            city_cortarName = city_dict["cortarName"]
            city_cortarNo = city_dict["cortarNo"]

            APIBot = NaverLandAPI()

            # 시/군/구 리스트
            dvsn_list = asyncio.run(APIBot.get_dvsn_list_from_cortarNo(city_cortarNo))

            print(dvsn_list)

            for i, dvsn in enumerate(dvsn_list):
                dvsn_cortarNo = dvsn["cortarNo"]
                dvsn_cortarName = dvsn["cortarName"]
                dvsn_lat = dvsn["centerLat"]
                dvsn_lon = dvsn["centerLon"]

                print(f"{i} {dvsn_cortarNo} {city_cortarName} {dvsn_cortarName} {dvsn_lat} {dvsn_lon}")
                self.log_msg.emit(f"{city_cortarName} {dvsn_cortarName} {self.guiDto.tradTpCd} {self.guiDto.rletTpCd}")

                filter_dict = asyncio.run(
                    APIBot.get_filter_dict_from_search_keyword(f"{city_cortarName} {dvsn_cortarName}")
                )
                dvsn_z = filter_dict["z"]
                print(f"{dvsn_cortarNo} {dvsn_lat} {dvsn_lon} {dvsn_z} {rletTpCd} {tradTpCd}")

                clusterList = asyncio.run(
                    APIBot.get_clusterList_from_cortar_info_and_type_code(
                        dvsn_cortarNo, dvsn_lat, dvsn_lon, dvsn_z, rletTpCd, tradTpCd
                    )
                )
                print()

                for j, cluster in enumerate(clusterList):
                    cluster_lgeo = cluster["lgeo"]
                    cluster_count = cluster["count"]
                    cluster_z = cluster["z"]
                    cluster_lat = cluster["lat"]
                    cluster_lon = cluster["lon"]
                    cluster_max_page = self.get_cluster_max_page(cluster_count)
                    print(
                        f"{cluster_lgeo} {cluster_z} {cluster_lat} {cluster_lon} {cluster_count} {cluster_max_page} {dvsn_cortarNo} {rletTpCd} {tradTpCd}"
                    )
                    articleList = asyncio.run(
                        APIBot.get_articleList_from_cluster_info(
                            cluster_lgeo,
                            cluster_z,
                            cluster_lat,
                            cluster_lon,
                            cluster_count,
                            cluster_max_page,
                            dvsn_cortarNo,
                            rletTpCd,
                            tradTpCd,
                        )
                    )

                    remaked_URL2 = f"https://m.land.naver.com/cluster/ajax/articleList?itemId={cluster_lgeo}&mapKey=&lgeo={cluster_lgeo}&showR0=&rletTpCd={rletTpCd}&tradTpCd={tradTpCd}&z={cluster_z}&lat={cluster_lat}&lon={cluster_lon}&totCnt={cluster_count}&cortarNo={dvsn_cortarNo}&page={cluster_max_page}"
                    print(remaked_URL2)
                    print()

                print()

        except Exception as e:
            print(e)


if __name__ == "__main__":
    process = NaverLandCrawlerProcess()
    process.work_start()
