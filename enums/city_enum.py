if 1 == 1:
    import sys
    import os

    sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from enum import Enum


class CityEnum(Enum):
    서울시 = {
        "cortarNo": "1100000000",
        "centerLat": 37.566427,
        "centerLon": 126.977872,
        "cortarName": "서울시",
        "cortarType": "city",
    }

    경기도 = {
        "cortarNo": "4100000000",
        "centerLat": 37.274939,
        "centerLon": 127.008689,
        "cortarName": "경기도",
        "cortarType": "city",
    }

    인천시 = {
        "cortarNo": "2800000000",
        "centerLat": 37.456054,
        "centerLon": 126.705151,
        "cortarName": "인천시",
        "cortarType": "city",
    }

    부산시 = {
        "cortarNo": "2600000000",
        "centerLat": 35.180143,
        "centerLon": 129.075413,
        "cortarName": "부산시",
        "cortarType": "city",
    }

    대전시 = {
        "cortarNo": "3000000000",
        "centerLat": 36.350465,
        "centerLon": 127.384953,
        "cortarName": "대전시",
        "cortarType": "city",
    }

    대구시 = {
        "cortarNo": "2700000000",
        "centerLat": 35.87139,
        "centerLon": 128.601763,
        "cortarName": "대구시",
        "cortarType": "city",
    }

    울산시 = {
        "cortarNo": "3100000000",
        "centerLat": 35.5386,
        "centerLon": 129.311375,
        "cortarName": "울산시",
        "cortarType": "city",
    }

    세종시 = {
        "cortarNo": "3600000000",
        "centerLat": 36.592907,
        "centerLon": 127.292375,
        "cortarName": "세종시",
        "cortarType": "city",
    }

    광주시 = {
        "cortarNo": "2900000000",
        "centerLat": 35.160032,
        "centerLon": 126.851338,
        "cortarName": "광주시",
        "cortarType": "city",
    }

    강원도 = {
        "cortarNo": "4200000000",
        "centerLat": 37.885399,
        "centerLon": 127.72975,
        "cortarName": "강원도",
        "cortarType": "city",
    }

    충청북도 = {
        "cortarNo": "4300000000",
        "centerLat": 36.636149,
        "centerLon": 127.491238,
        "cortarName": "충청북도",
        "cortarType": "city",
    }

    충청남도 = {
        "cortarNo": "4400000000",
        "centerLat": 36.63629,
        "centerLon": 126.68957,
        "cortarName": "충청남도",
        "cortarType": "city",
    }

    경상북도 = {
        "cortarNo": "4700000000",
        "centerLat": 36.518504,
        "centerLon": 128.437796,
        "cortarName": "경상북도",
        "cortarType": "city",
    }

    경상남도 = {
        "cortarNo": "4800000000",
        "centerLat": 35.238343,
        "centerLon": 128.6924,
        "cortarName": "경상남도",
        "cortarType": "city",
    }

    전라북도 = {
        "cortarNo": "4500000000",
        "centerLat": 35.820433,
        "centerLon": 127.108875,
        "cortarName": "전라북도",
        "cortarType": "city",
    }

    전라남도 = {
        "cortarNo": "4600000000",
        "centerLat": 34.816358,
        "centerLon": 126.462443,
        "cortarName": "전라남도",
        "cortarType": "city",
    }

    제주도 = {
        "cortarNo": "5000000000",
        "centerLat": 33.488976,
        "centerLon": 126.498238,
        "cortarName": "제주도",
        "cortarType": "city",
    }

    @staticmethod
    def list():
        return list(map(lambda c: c.name, CityEnum))


print(CityEnum.list())
