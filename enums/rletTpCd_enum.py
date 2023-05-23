if 1 == 1:
    import sys
    import os

    sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from enum import Enum


class rletTpCdEnum(Enum):
    아파트 = "APT"
    오피스텔 = "OPST"
    빌라 = "VL"
    # 아파트분양권 = "ABYG"
    # 오피스텔분양권 = "OBYG"
    # 재건축 = "JGC"
    전원주택 = "JWJT"
    단독다가구 = "DDDGG"
    상가주택 = "SGJT"
    한옥주택 = "HOJT"
    # 재개발 = "JGB"
    # 원룸 = "OR"
    # 고시원 = "GSW"
    상가 = "SG"
    사무실 = "SMS"
    공장창고 = "GJCG"
    건물 = "GM"
    토지 = "TJ"
    지식산업센터 = "APTHGJ"

    @staticmethod
    def list():
        return list(map(lambda c: c.name, rletTpCdEnum))


if __name__ == "__main__":
    print(rletTpCdEnum.list())
