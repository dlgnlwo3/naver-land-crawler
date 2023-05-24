#!/usr/bin/env python
if 1 == 1:
    import sys
    import os

    sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from http import HTTPStatus
from bs4 import BeautifulSoup
import bcrypt
import pybase64
import requests
import json
import time
import asyncio
import clipboard
import re

from tenacity import retry, wait_fixed, stop_after_attempt

import datetime

from enums.city_enum import CityEnum


class NaverLandAPI:
    def __init__(self):
        self.get_headers()

    def get_timestamp(self):
        return round(time.time() * 1000)

    def get_headers(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7,ja;q=0.6",
            "Referer": "https://m.land.naver.com/",
        }

    @retry(
        wait=wait_fixed(3),  # 3초 대기
        stop=stop_after_attempt(2),  # 2번 재시도
    )
    async def get_filter_dict_from_search_keyword(self, search_keyword):
        filter_dict = {}
        auth_url = f"https://m.land.naver.com/search/result/{search_keyword}"
        response = requests.get(auth_url, headers=self.headers)

        # 200
        if response.status_code == HTTPStatus.OK:
            print("filter_dict 획득 성공")
            soup = BeautifulSoup(response.content, "html.parser", from_encoding="utf-8")
            script = soup.find("script", {"type": "text/javascript"}, text=re.compile(r"filter:\s*{([^}]+)}"))
            script_content = script.string
            filter_value = re.search(r"filter:\s*{([^}]+)}", script_content).group(1)
            for match in re.finditer(r"(\w+):\s*\'?([^\',]+)\'?", filter_value):
                key = match.group(1)
                value = match.group(2)
                filter_dict[key] = value

            print(filter_dict)

        # 400
        elif response.status_code == HTTPStatus.BAD_REQUEST:
            print("입력값이 유효하지 않음")

        # 404
        elif response.status_code == HTTPStatus.NOT_FOUND:
            print("Request-URI에 일치하는 건을 발견하지 못함")

        # 405
        elif response.status_code == HTTPStatus.METHOD_NOT_ALLOWED:
            print("허가되지 않은 메소드 사용")

        # 500
        elif response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
            print("서버 내부의 에러")

        # 503
        elif response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
            print("서버 과부하로 인한 사용 불가")

        # 그 외의 경우
        else:
            print("알 수 없는 오류")

        return filter_dict

    @retry(
        wait=wait_fixed(3),  # 3초 대기
        stop=stop_after_attempt(2),  # 2번 재시도
    )
    async def get_dvsn_list_from_cortarNo(self, cortarNo):
        dvsn_list = []
        auth_url = f"https://new.land.naver.com/api/regions/list?cortarNo={cortarNo}"
        response = requests.get(auth_url, headers=self.headers)

        # 200
        if response.status_code == HTTPStatus.OK:
            print("dvsn_list 획득 성공")
            soup = BeautifulSoup(response.content, "html.parser", from_encoding="utf-8")
            dvsn_dict = json.loads(str(soup))
            print(dvsn_dict)
            dvsn_list = dvsn_dict["regionList"]
            pass

        # 400
        elif response.status_code == HTTPStatus.BAD_REQUEST:
            print("입력값이 유효하지 않음")

        # 404
        elif response.status_code == HTTPStatus.NOT_FOUND:
            print("Request-URI에 일치하는 건을 발견하지 못함")

        # 405
        elif response.status_code == HTTPStatus.METHOD_NOT_ALLOWED:
            print("허가되지 않은 메소드 사용")

        # 500
        elif response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
            print("서버 내부의 에러")

        # 503
        elif response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
            print("서버 과부하로 인한 사용 불가")

        # 그 외의 경우
        else:
            print("알 수 없는 오류")

        return dvsn_list

    @retry(
        wait=wait_fixed(3),  # 3초 대기
        stop=stop_after_attempt(2),  # 2번 재시도
    )
    async def get_clusterList_from_cortar_info_and_type_code(self, cortarNo, lat, lon, z, rletTpCd, tradTpCd):
        clusterList = []
        auth_url = f"https://m.land.naver.com/cluster/clusterList?view=atcl&cortarNo={cortarNo}&rletTpCd={rletTpCd}&tradTpCd={tradTpCd}&z={z}&lat={lat}&lon={lon}"
        response = requests.get(auth_url, headers=self.headers)

        # 200
        if response.status_code == HTTPStatus.OK:
            print("clusterList 획득 성공")
            soup = BeautifulSoup(response.content, "html.parser", from_encoding="utf-8")
            cluster_dict = json.loads(str(soup))
            clusterList = cluster_dict["data"]["ARTICLE"]
            pass

        # 400
        elif response.status_code == HTTPStatus.BAD_REQUEST:
            print("입력값이 유효하지 않음")

        # 404
        elif response.status_code == HTTPStatus.NOT_FOUND:
            print("Request-URI에 일치하는 건을 발견하지 못함")

        # 405
        elif response.status_code == HTTPStatus.METHOD_NOT_ALLOWED:
            print("허가되지 않은 메소드 사용")

        # 500
        elif response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
            print("서버 내부의 에러")

        # 503
        elif response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
            print("서버 과부하로 인한 사용 불가")

        # 그 외의 경우
        else:
            print("알 수 없는 오류")

        return clusterList

    @retry(
        wait=wait_fixed(3),  # 3초 대기
        stop=stop_after_attempt(2),  # 2번 재시도
    )
    async def get_articleList_from_cluster_info(
        self,
        cluster_lgeo,
        cluster_z,
        cluster_lat,
        cluster_lon,
        cluster_count,
        cluster_max_page,
        dvsn_cortarNo,
        rletTpCd,
        tradTpCd,
    ):
        articleList = []
        for i in range(1, cluster_max_page + 1):
            auth_url = f"https://m.land.naver.com/cluster/ajax/articleList?itemId={cluster_lgeo}&mapKey=&lgeo={cluster_lgeo}&showR0=&rletTpCd={rletTpCd}&tradTpCd={tradTpCd}&z={cluster_z}&lat={cluster_lat}&lon={cluster_lon}&totCnt={cluster_count}&cortarNo={dvsn_cortarNo}&page={i}"
            response = requests.get(auth_url, headers=self.headers)

            # 200
            if response.status_code == HTTPStatus.OK:
                print("articleList 획득 성공")
                soup = BeautifulSoup(response.content, "html.parser", from_encoding="utf-8")
                cluster_dict = json.loads(str(soup))
                article_dict_list = cluster_dict["body"]
                for i, article_dict in enumerate(article_dict_list):
                    articleList.append(article_dict)
                    time.sleep(2)

            # 400
            elif response.status_code == HTTPStatus.BAD_REQUEST:
                print("입력값이 유효하지 않음")
                break

            # 404
            elif response.status_code == HTTPStatus.NOT_FOUND:
                print("Request-URI에 일치하는 건을 발견하지 못함")
                break

            # 405
            elif response.status_code == HTTPStatus.METHOD_NOT_ALLOWED:
                print("허가되지 않은 메소드 사용")
                break

            # 500
            elif response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
                print("서버 내부의 에러")
                break

            # 503
            elif response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
                print("서버 과부하로 인한 사용 불가")
                break

            # 그 외의 경우
            else:
                print("알 수 없는 오류")
                break

        return articleList

    @retry(
        wait=wait_fixed(3),  # 3초 대기
        stop=stop_after_attempt(2),  # 2번 재시도
    )
    async def get_article_detail_info_from_atclNo(self, atclNo):
        article_detail_info = {}
        auth_url = f"https://m.land.naver.com/article/info/{atclNo}?newMobile"
        response = requests.get(auth_url, headers=self.headers)

        # 200
        if response.status_code == HTTPStatus.OK:
            print("article_detail 획득 성공")
            soup = BeautifulSoup(response.content, "html.parser", from_encoding="utf-8")
            script = soup.find("script", text=re.compile(r"window.App"))
            script_content = script.string
            app_value = re.search(r"window.App=(\{.*\})", script_content).group(1)
            article_detail_dict = json.loads(app_value)
            article_detail_info = article_detail_dict["state"]["article"]
            pass

        # 400
        elif response.status_code == HTTPStatus.BAD_REQUEST:
            print("입력값이 유효하지 않음")

        # 404
        elif response.status_code == HTTPStatus.NOT_FOUND:
            print("Request-URI에 일치하는 건을 발견하지 못함")

        # 405
        elif response.status_code == HTTPStatus.METHOD_NOT_ALLOWED:
            print("허가되지 않은 메소드 사용")

        # 500
        elif response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
            print("서버 내부의 에러")

        # 503
        elif response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
            print("서버 과부하로 인한 사용 불가")

        # 그 외의 경우
        else:
            print("알 수 없는 오류")

        return article_detail_info


if __name__ == "__main__":
    # search_keyword -> city dvsn
    city_name = "경기도"

    city_dict = getattr(CityEnum, city_name).value

    city_cortarNo = city_dict["cortarNo"]
    city_lat = city_dict["centerLat"]
    city_lon = city_dict["centerLon"]

    dvsn_cortarNo = "4131000000"
    dvsn_cortarName = "구리시"
    dvsn_lat = 37.594409
    dvsn_lon = 127.129581
    dvsn_z = 12
    rletTpCd = "VL"
    tradTpCd = "A1"

    APT_atclNo = "2321571037"
    VL_atclNo = "2317652285"
    HANOK_atclNo = "2320930153"

    APIBot = NaverLandAPI()

    data = ""

    # data = asyncio.run(APIBot.get_article_detail_info_from_atclNo(HANOK_atclNo))

    # data = asyncio.run(APIBot.get_dvsn_list_from_cortarNo(city_cortarNo))

    # {'cortarNo': '4131000000', 'centerLat': 37.594409, 'centerLon': 127.129581, 'cortarName': '구리시', 'cortarType': 'dvsn'}

    data = asyncio.run(APIBot.get_filter_dict_from_search_keyword(f"강원도 강릉시"))

    print(type(data))

    print(data)

    clipboard.copy(str(data))
