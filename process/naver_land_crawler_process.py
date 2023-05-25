if 1 == 1:
    import sys
    import os

    sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))


from dtos.gui_dto import GUIDto
from dtos.article_dto import ArticleDto

from configs.coupang_review_crawler_config import CoupangReviewCrawlerConfig
from configs.coupang_review_crawler_config import CoupangReviewCrawlerData


from common.utils import global_log_append


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

    def convert_tradTpCd(self):
        print(self.guiDto.tradTpCd)
        tradTpCd = self.guiDto.tradTpCd
        for enum in tradTpCdEnum.list():
            tradTpCd = tradTpCd.replace(enum, getattr(tradTpCdEnum, enum).value)
        tradTpCd = tradTpCd.replace(",", ":")
        return tradTpCd

    def convert_rletTpCd(self):
        print(self.guiDto.rletTpCd)
        rletTpCd = self.guiDto.rletTpCd
        for enum in rletTpCdEnum.list():
            rletTpCd = rletTpCd.replace(enum, getattr(rletTpCdEnum, enum).value)
        rletTpCd = rletTpCd.replace(",", ":")
        return rletTpCd

    def get_cluster_max_page(self, cluster_count):
        cluster_max_page = math.ceil(cluster_count / 20)
        return cluster_max_page

    # article_dto 생성
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
        except Exception as e:
            article_dto.totalDongCount = ""

        try:
            article_dto.roomCount = article_group["roomCount"]
        except Exception as e:
            article_dto.roomCount = ""

        try:
            article_dto.bathroomCount = article_group["bathroomCount"]
        except Exception as e:
            article_dto.bathroomCount = ""

        try:
            article_dto.moveInTypeName = article_group["moveInTypeName"]
        except Exception as e:
            article_dto.moveInTypeName = ""

        try:
            article_dto.parkingCount = article_group["parkingCount"]
        except Exception as e:
            article_dto.parkingCount = ""

        try:
            article_dto.parkingPossibleYN = article_group["parkingPossibleYN"]
        except Exception as e:
            article_dto.parkingPossibleYN = ""

        try:
            article_dto.floorLayerName = article_group["floorLayerName"]
        except Exception as e:
            article_dto.floorLayerName = ""

        try:
            article_dto.articleNo = addition_group["articleNo"]
        except Exception as e:
            article_dto.articleNo = ""

        try:
            article_dto.articleName = addition_group["articleName"]
        except Exception as e:
            article_dto.articleName = ""

        try:
            article_dto.realEstateTypeName = addition_group["realEstateTypeName"]
        except Exception as e:
            article_dto.realEstateTypeName = ""

        try:
            article_dto.articleRealEstateTypeName = addition_group["articleRealEstateTypeName"]
        except Exception as e:
            article_dto.articleRealEstateTypeName = ""

        try:
            article_dto.tradeTypeName = addition_group["tradeTypeName"]
        except Exception as e:
            article_dto.tradeTypeName = ""

        try:
            article_dto.floorInfo = addition_group["floorInfo"]
        except Exception as e:
            article_dto.floorInfo = ""

        try:
            article_dto.dealOrWarrantPrc = addition_group["dealOrWarrantPrc"]
        except Exception as e:
            article_dto.dealOrWarrantPrc = ""

        try:
            article_dto.area1 = addition_group["area1"]
        except Exception as e:
            article_dto.area1 = ""

        try:
            article_dto.area2 = addition_group["area2"]
        except Exception as e:
            article_dto.area2 = ""

        try:
            article_dto.articleConfirmYmd = addition_group["articleConfirmYmd"]
        except Exception as e:
            article_dto.articleConfirmYmd = ""

        try:
            article_dto.articleFeatureDesc = addition_group["articleFeatureDesc"]
        except Exception as e:
            article_dto.articleFeatureDesc = ""

        try:
            article_dto.tagList = addition_group["tagList"]
        except Exception as e:
            article_dto.tagList = ""

        try:
            article_dto.priceBySpace = price_group["priceBySpace"]
        except Exception as e:
            article_dto.priceBySpace = ""

        try:
            article_dto.rentPrice = price_group["rentPrice"]
        except Exception as e:
            article_dto.rentPrice = ""

        try:
            article_dto.dealPrice = price_group["dealPrice"]
        except Exception as e:
            article_dto.dealPrice = ""

        try:
            article_dto.warrantPrice = price_group["warrantPrice"]
        except Exception as e:
            article_dto.warrantPrice = ""

        try:
            article_dto.allWarrantPrice = price_group["allWarrantPrice"]
        except Exception as e:
            article_dto.allWarrantPrice = ""

        try:
            article_dto.financePrice = price_group["financePrice"]
        except Exception as e:
            article_dto.financePrice = ""

        try:
            article_dto.allRentPrice = price_group["allRentPrice"]
        except Exception as e:
            article_dto.allRentPrice = ""

        try:
            article_dto.acquisitionTax = articleTax_group["acquisitionTax"]
        except Exception as e:
            article_dto.acquisitionTax = ""

        try:
            article_dto.brokerFee = articleTax_group["brokerFee"]
        except Exception as e:
            article_dto.brokerFee = ""

        try:
            article_dto.maxBrokerFee = articleTax_group["maxBrokerFee"]
        except Exception as e:
            article_dto.maxBrokerFee = ""

        try:
            article_dto.eduTax = articleTax_group["eduTax"]
        except Exception as e:
            article_dto.eduTax = ""

        try:
            article_dto.specialTax = articleTax_group["specialTax"]
        except Exception as e:
            article_dto.specialTax = ""

        try:
            article_dto.totalPrice = articleTax_group["totalPrice"]
        except Exception as e:
            article_dto.totalPrice = ""

        try:
            article_dto.realtorName = realtor_group["realtorName"]
        except Exception as e:
            article_dto.realtorName = ""

        try:
            article_dto.representativeName = realtor_group["representativeName"]
        except Exception as e:
            article_dto.representativeName = ""

        try:
            article_dto.address = realtor_group["address"]
        except Exception as e:
            article_dto.address = ""

        try:
            article_dto.establishRegistrationNo = realtor_group["establishRegistrationNo"]
        except Exception as e:
            article_dto.establishRegistrationNo = ""

        try:
            article_dto.representativeTelNo = realtor_group["representativeTelNo"]
        except Exception as e:
            article_dto.representativeTelNo = ""

        try:
            article_dto.cellPhoneNo = realtor_group["cellPhoneNo"]
        except Exception as e:
            article_dto.cellPhoneNo = ""

        try:
            article_dto.cityName = location_group["cityName"]
        except Exception as e:
            article_dto.cityName = ""

        try:
            article_dto.divisionName = location_group["divisionName"]
        except Exception as e:
            article_dto.divisionName = ""

        try:
            article_dto.sectionName = location_group["sectionName"]
        except Exception as e:
            article_dto.sectionName = ""

        try:
            article_dto.detailAddress = location_group["detailAddress"]
        except Exception as e:
            article_dto.detailAddress = ""

        return article_dto

    # 엑셀 저장
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
            rletTpCd = self.convert_rletTpCd()
            tradTpCd = self.convert_tradTpCd()
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

                print(f"{i} / {dvsn_cortarNo} / {city_cortarName} {dvsn_cortarName} / {dvsn_lat} / {dvsn_lon}")
                self.log_msg.emit(
                    f"{city_cortarName} {dvsn_cortarName} / {self.guiDto.tradTpCd} / {self.guiDto.rletTpCd}"
                )

                filter_dict = asyncio.run(
                    APIBot.get_filter_dict_from_search_keyword(f"{city_cortarName} {dvsn_cortarName}")
                )

                try:
                    dvsn_z = filter_dict["z"]
                except Exception as e:
                    print(str(e))
                    self.log_msg.emit(f"{dvsn_cortarName} 위치값 탐색에 실패했습니다.")
                    continue

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

                    if cluster_count <= 1:
                        continue

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

                    self.log_msg.emit(f"{city_cortarName} {dvsn_cortarName} {j+1}구역 {cluster_count}건 조회되었습니다.")

                    for k, article in enumerate(articleList):
                        atclNo = article["atclNo"]
                        article_detail_info = {}
                        article_dto = None
                        article_detail_info = asyncio.run(APIBot.get_article_detail_info_from_atclNo(atclNo))

                        article_dto: ArticleDto = self.article_dto_from_article_detail_info(article_detail_info)

                        if article_dto != None:
                            print(article_dto.detailAddress)
                            article_dtos.append(article_dto.get_dict())
                            self.log_msg.emit(f"{atclNo} 확인")

                    self.article_dtos_to_excel(city_cortarName, dvsn_cortarName, article_dtos)
                    self.log_msg.emit(f"{city_cortarName} {dvsn_cortarName} {j+1}구역 {cluster_count}건 저장")

        except Exception as e:
            print(e)


if __name__ == "__main__":
    process = NaverLandCrawlerProcess()
    process.work_start()
