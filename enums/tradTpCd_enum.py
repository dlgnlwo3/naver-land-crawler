if 1 == 1:
    import sys
    import os

    sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from enum import Enum


class tradTpCdEnum(Enum):
    매매 = "A1"
    전세 = "B1"
    월세 = "B2"
    단기임대 = "B3"

    @staticmethod
    def list():
        return list(map(lambda c: c.name, tradTpCdEnum))


print(tradTpCdEnum.list())
