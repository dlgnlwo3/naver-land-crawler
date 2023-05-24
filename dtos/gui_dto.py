if 1 == 1:
    import sys
    import os

    sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))


class GUIDto:
    def __init__(self):
        self.__city = ""
        self.__tradTpCd = ""
        self.__rletTpCd = ""

    @property
    def city(self):  # getter
        return self.__city

    @city.setter
    def city(self, value):  # setter
        self.__city = value

    @property
    def tradTpCd(self):  # getter
        return self.__tradTpCd

    @tradTpCd.setter
    def tradTpCd(self, value):  # setter
        delimiter = ","
        value = delimiter.join(value)
        self.__tradTpCd = value

    @property
    def rletTpCd(self):  # getter
        return self.__rletTpCd

    @rletTpCd.setter
    def rletTpCd(self, value):  # setter
        delimiter = ","
        value = delimiter.join(value)
        self.__rletTpCd = value

    def to_print(self):
        print("city: ", self.city)
        print("tradTpCd: ", self.tradTpCd)
        print("rletTpCd: ", self.rletTpCd)
