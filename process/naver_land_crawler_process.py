if 1 == 1:
    import sys
    import os

    sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))


from selenium import webdriver
from dtos.gui_dto import GUIDto
from dtos.article_dto import ArticleDto

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
import clipboard


import pandas as pd

from enums.city_enum import CityEnum
from enums.rletTpCd_enum import rletTpCdEnum
from enums.tradTpCd_enum import tradTpCdEnum
from api.naver_land_api import NaverLandAPI
import asyncio

from configs.program_config import ProgramConfig


class NaverLandCrawlerProcess:
    def __init__(self):
        self.config = ProgramConfig()
        self.today_output_folder = self.config.today_output_folder

    def setGuiDto(self, guiDto: GUIDto):
        self.guiDto = guiDto

    def setLogger(self, log_msg):
        self.log_msg = log_msg

    def get_cluster_max_page(self, cluster_count):
        cluster_max_page = math.ceil(cluster_count / 20)
        return cluster_max_page

    def article_dto_from_article_detail_info(self, article_detail_info: dict):
        article_dto = ArticleDto()

        article_group = article_detail_info["article"]
        addition_group = article_detail_info["addition"]
        price_group = article_detail_info["price"]
        articleTax_group = article_detail_info["articleTax"]
        realtor_group = article_detail_info["realtor"]
        location_group = article_detail_info["location"]

        try:
            article_dto.totalDongCount = article_group["totalDongCount"]
            article_dto.roomCount = article_group["roomCount"]
            article_dto.bathroomCount = article_group["bathroomCount"]
            article_dto.moveInTypeName = article_group["moveInTypeName"]
            article_dto.parkingCount = article_group["parkingCount"]
            article_dto.parkingPossibleYN = article_group["parkingPossibleYN"]
            article_dto.floorLayerName = article_group["floorLayerName"]

            article_dto.articleNo = addition_group["articleNo"]
            article_dto.articleName = addition_group["articleName"]
            article_dto.realEstateTypeName = addition_group["realEstateTypeName"]
            article_dto.articleRealEstateTypeName = addition_group["articleRealEstateTypeName"]
            article_dto.tradeTypeName = addition_group["tradeTypeName"]
            article_dto.floorInfo = addition_group["floorInfo"]
            article_dto.dealOrWarrantPrc = addition_group["dealOrWarrantPrc"]
            article_dto.area1 = addition_group["area1"]
            article_dto.area2 = addition_group["area2"]
            article_dto.articleConfirmYmd = addition_group["articleConfirmYmd"]
            article_dto.articleFeatureDesc = addition_group["articleFeatureDesc"]
            article_dto.tagList = addition_group["tagList"]

            article_dto.priceBySpace = price_group["priceBySpace"]
            article_dto.rentPrice = price_group["rentPrice"]
            article_dto.dealPrice = price_group["dealPrice"]
            article_dto.warrantPrice = price_group["warrantPrice"]
            article_dto.allWarrantPrice = price_group["allWarrantPrice"]
            article_dto.financePrice = price_group["financePrice"]
            article_dto.allRentPrice = price_group["allRentPrice"]

            article_dto.acquisitionTax = articleTax_group["acquisitionTax"]
            article_dto.brokerFee = articleTax_group["brokerFee"]
            article_dto.maxBrokerFee = articleTax_group["maxBrokerFee"]
            article_dto.eduTax = articleTax_group["eduTax"]
            article_dto.specialTax = articleTax_group["specialTax"]
            article_dto.totalPrice = articleTax_group["totalPrice"]

            article_dto.realtorName = realtor_group["realtorName"]
            article_dto.representativeName = realtor_group["representativeName"]
            article_dto.address = realtor_group["address"]
            article_dto.establishRegistrationNo = realtor_group["establishRegistrationNo"]
            article_dto.representativeTelNo = realtor_group["representativeTelNo"]
            article_dto.cellPhoneNo = realtor_group["cellPhoneNo"]

            article_dto.cityName = location_group["cityName"]
            article_dto.divisionName = location_group["divisionName"]
            article_dto.sectionName = location_group["sectionName"]
            article_dto.detailAddress = location_group["detailAddress"]

        except Exception as e:
            print(str(e))

        return article_dto

    def article_dtos_to_excel(self, city_cortarName, dvsn_cortarName, article_dtos):
        try:
            article_excel = os.path.join(
                self.today_output_folder,
                f"{self.run_time}_{city_cortarName}_{dvsn_cortarName}_{self.guiDto.tradTpCd}_{self.guiDto.rletTpCd}.xlsx",
            )

            if os.path.isfile(article_excel):
                with pd.ExcelWriter(article_excel, engine="openpyxl", mode="a", if_sheet_exists="replace") as writer:
                    pd.DataFrame.from_dict(article_dtos).to_excel(writer, index=False)

            else:
                with pd.ExcelWriter(article_excel, engine="openpyxl") as writer:
                    pd.DataFrame.from_dict(article_dtos).to_excel(writer, index=False)

        except Exception as e:
            print(e)

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
                self.run_time = str(datetime.now())[0:-7].replace(":", "")
                article_dtos = []

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

                    self.log_msg.emit(f"총 {len(articleList)}건 조회되었습니다.")

                    for k, article in enumerate(articleList):
                        atclNo = article["atclNo"]
                        article_detail_info = {}
                        article_dto = None
                        article_detail_info = asyncio.run(APIBot.get_article_detail_info_from_atclNo(atclNo))
                        print(article_detail_info)

                        article_dto: ArticleDto = self.article_dto_from_article_detail_info(article_detail_info)

                        if article_dto != None:
                            print(article_dto.detailAddress)
                            article_dtos.append(article_dto.get_dict())
                        else:
                            continue

                    self.article_dtos_to_excel(city_cortarName, dvsn_cortarName, article_dtos)

                print()

        except Exception as e:
            print(e)


if __name__ == "__main__":
    process = NaverLandCrawlerProcess()
    process.work_start()
