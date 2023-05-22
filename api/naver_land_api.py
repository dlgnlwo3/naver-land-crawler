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
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.220 Whale/1.3.51.7 Safari/537.36",
            "Referer": "https://m.land.naver.com/",
        }

    @retry(
        wait=wait_fixed(3),  # 3초 대기
        stop=stop_after_attempt(2),  # 2번 재시도
    )
    async def get_filter_dict_from_search_keyword(self, search_keyword):
        auth_url = f"https://m.land.naver.com/search/result/{search_keyword}"
        response = requests.get(auth_url, headers=self.headers)
        soup = BeautifulSoup(response.content, "html.parser", from_encoding="utf-8")
        script = soup.find("script", {"type": "text/javascript"}, text=re.compile(r"filter:\s*{([^}]+)}"))
        script_content = script.string
        filter_value = re.search(r"filter:\s*{([^}]+)}", script_content).group(1)
        filter_dict = {}
        for match in re.finditer(r"(\w+):\s*\'?([^\',]+)\'?", filter_value):
            key = match.group(1)
            value = match.group(2)
            filter_dict[key] = value

        print(filter_dict)

        # 200
        if response.status_code == HTTPStatus.OK:
            print("성공")

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
        soup = BeautifulSoup(response.content, "html.parser", from_encoding="utf-8")
        dvsn_dict = json.loads(str(soup))
        print(dvsn_dict)

        # 200
        if response.status_code == HTTPStatus.OK:
            dvsn_list = dvsn_dict["regionList"]
            print("성공")

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


if __name__ == "__main__":
    # search_keyword -> xx도 yy시 -> 시의 정보가 필요함
    city = "경기도"

    city_dict = CityEnum.경기도.value

    cortarNo = city_dict["cortarNo"]
    lat = city_dict["centerLat"]
    lon = city_dict["centerLon"]

    APIBot = NaverLandAPI()

    data = ""

    # 원하는 지역명을 검색해서 해당 지역의 좌표를 얻는 방법
    data = asyncio.run(APIBot.get_dvsn_list_from_cortarNo(cortarNo))

    print(type(data))

    print(data)

    clipboard.copy(str(data))
