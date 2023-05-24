if 1 == 1:
    import sys
    import os

    sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))


class ArticleDto:
    def __init__(self):
        # article 그룹 7
        self.__totalDongCount = ""  # 동 수(아파트)
        self.__roomCount = ""  # 방 수
        self.__bathroomCount = ""  # 욕실 수
        self.__moveInTypeName = ""  # 입주가능여부
        self.__parkingCount = ""  # 총 주차 대수
        self.__parkingPossibleYN = ""  # 주차 가능 여부
        self.__floorLayerName = ""  # 층 구조

        # addition 그룹 12
        self.__articleNo = ""  # 매물번호
        self.__articleName = ""  # 매물제목
        self.__realEstateTypeName = ""  # 매물유형
        self.__articleRealEstateTypeName = ""  # 건물용도
        self.__tradeTypeName = ""  # 거래유형
        self.__floorInfo = ""  # 층 정보
        self.__dealOrWarrantPrc = ""  # 금액 (한글)
        self.__area1 = ""  # 공급면적
        self.__area2 = ""  # 전용면적
        self.__articleConfirmYmd = ""  # 게시일자
        self.__articleFeatureDesc = ""  # 글 내용
        self.__tagList = ""  # 태그목록

        # price 그룹 -> 해당 그룹은 검토가 많이 필요함 7
        self.__priceBySpace = ""  # 평당가격
        self.__rentPrice = ""  # 월세??
        self.__dealPrice = ""  # 거래가격
        self.__warrantPrice = ""  # 보증금
        self.__allWarrantPrice = ""  # 기보증금
        self.__financePrice = ""  # 융자금
        self.__allRentPrice = ""  # 월세???

        # articleTax 그룹 6
        self.__acquisitionTax = ""  # 취득세
        self.__brokerFee = ""  # 중개보수
        self.__maxBrokerFee = ""  # 중개보수 상한 요율
        self.__eduTax = ""  # 지방교육세
        self.__specialTax = ""  # 농어촌특별세
        self.__totalPrice = ""  # 세금 총 합계

        # realtor 그룹 6
        self.__realtorName = ""  # 중개사무소 이름
        self.__representativeName = ""  # 중개사무소 대표자
        self.__address = ""  # 중개사무소 주소
        self.__establishRegistrationNo = ""  # 중개사무소 등록번호
        self.__representativeTelNo = ""  # 중개사무소 전화번호
        self.__cellPhoneNo = ""  # 중개사무소 휴대전화번호

        # location 그룹 4
        self.__cityName = ""  # 시/도
        self.__divisionName = ""  # 시/군/구
        self.__sectionName = ""  # 읍/면/동
        self.__detailAddress = ""  # 상세주소

    @property
    def totalDongCount(self):  # getter
        return self.__totalDongCount

    @totalDongCount.setter
    def totalDongCount(self, value):  # setter
        self.__totalDongCount = value

    @property
    def roomCount(self):  # getter
        return self.__roomCount

    @roomCount.setter
    def roomCount(self, value):  # setter
        self.__roomCount = value

    @property
    def bathroomCount(self):  # getter
        return self.__bathroomCount

    @bathroomCount.setter
    def bathroomCount(self, value):  # setter
        self.__bathroomCount = value

    @property
    def moveInTypeName(self):  # getter
        return self.__moveInTypeName

    @moveInTypeName.setter
    def moveInTypeName(self, value):  # setter
        self.__moveInTypeName = value

    @property
    def parkingCount(self):  # getter
        return self.__parkingCount

    @parkingCount.setter
    def parkingCount(self, value):  # setter
        self.__parkingCount = value

    @property
    def parkingPossibleYN(self):  # getter
        return self.__parkingPossibleYN

    @parkingPossibleYN.setter
    def parkingPossibleYN(self, value):  # setter
        self.__parkingPossibleYN = value

    @property
    def floorLayerName(self):  # getter
        return self.__floorLayerName

    @floorLayerName.setter
    def floorLayerName(self, value):  # setter
        self.__floorLayerName = value

    @property
    def articleNo(self):  # getter
        return self.__articleNo

    @articleNo.setter
    def articleNo(self, value):  # setter
        self.__articleNo = value

    @property
    def articleName(self):  # getter
        return self.__articleName

    @articleName.setter
    def articleName(self, value):  # setter
        self.__articleName = value

    @property
    def realEstateTypeName(self):  # getter
        return self.__realEstateTypeName

    @realEstateTypeName.setter
    def realEstateTypeName(self, value):  # setter
        self.__realEstateTypeName = value

    @property
    def articleRealEstateTypeName(self):  # getter
        return self.__articleRealEstateTypeName

    @articleRealEstateTypeName.setter
    def articleRealEstateTypeName(self, value):  # setter
        self.__articleRealEstateTypeName = value

    @property
    def tradeTypeName(self):  # getter
        return self.__tradeTypeName

    @tradeTypeName.setter
    def tradeTypeName(self, value):  # setter
        self.__tradeTypeName = value

    @property
    def floorInfo(self):  # getter
        return self.__floorInfo

    @floorInfo.setter
    def floorInfo(self, value):  # setter
        self.__floorInfo = value

    @property
    def dealOrWarrantPrc(self):  # getter
        return self.__dealOrWarrantPrc

    @dealOrWarrantPrc.setter
    def dealOrWarrantPrc(self, value):  # setter
        self.__dealOrWarrantPrc = value

    @property
    def area1(self):  # getter
        return self.__area1

    @area1.setter
    def area1(self, value):  # setter
        self.__area1 = value

    @property
    def area2(self):  # getter
        return self.__area2

    @area2.setter
    def area2(self, value):  # setter
        self.__area2 = value

    @property
    def articleConfirmYmd(self):  # getter
        return self.__articleConfirmYmd

    @articleConfirmYmd.setter
    def articleConfirmYmd(self, value):  # setter
        self.__articleConfirmYmd = value

    @property
    def articleFeatureDesc(self):  # getter
        return self.__articleFeatureDesc

    @articleFeatureDesc.setter
    def articleFeatureDesc(self, value):  # setter
        self.__articleFeatureDesc = value

    @property
    def tagList(self):  # getter
        return self.__tagList

    @tagList.setter
    def tagList(self, value):  # setter
        self.__tagList = value

    @property
    def priceBySpace(self):  # getter
        return self.__priceBySpace

    @priceBySpace.setter
    def priceBySpace(self, value):  # setter
        self.__priceBySpace = value

    @property
    def rentPrice(self):  # getter
        return self.__rentPrice

    @rentPrice.setter
    def rentPrice(self, value):  # setter
        self.__rentPrice = value

    @property
    def dealPrice(self):  # getter
        return self.__dealPrice

    @dealPrice.setter
    def dealPrice(self, value):  # setter
        self.__dealPrice = value

    @property
    def warrantPrice(self):  # getter
        return self.__warrantPrice

    @warrantPrice.setter
    def warrantPrice(self, value):  # setter
        self.__warrantPrice = value

    @property
    def allWarrantPrice(self):  # getter
        return self.__allWarrantPrice

    @allWarrantPrice.setter
    def allWarrantPrice(self, value):  # setter
        self.__allWarrantPrice = value

    @property
    def financePrice(self):  # getter
        return self.__financePrice

    @financePrice.setter
    def financePrice(self, value):  # setter
        self.__financePrice = value

    @property
    def allRentPrice(self):  # getter
        return self.__allRentPrice

    @allRentPrice.setter
    def allRentPrice(self, value):  # setter
        self.__allRentPrice = value

    @property
    def acquisitionTax(self):  # getter
        return self.__acquisitionTax

    @acquisitionTax.setter
    def acquisitionTax(self, value):  # setter
        self.__acquisitionTax = value

    @property
    def brokerFee(self):  # getter
        return self.__brokerFee

    @brokerFee.setter
    def brokerFee(self, value):  # setter
        self.__brokerFee = value

    @property
    def maxBrokerFee(self):  # getter
        return self.__maxBrokerFee

    @maxBrokerFee.setter
    def maxBrokerFee(self, value):  # setter
        self.__maxBrokerFee = value

    @property
    def eduTax(self):  # getter
        return self.__eduTax

    @eduTax.setter
    def eduTax(self, value):  # setter
        self.__eduTax = value

    @property
    def specialTax(self):  # getter
        return self.__specialTax

    @specialTax.setter
    def specialTax(self, value):  # setter
        self.__specialTax = value

    @property
    def totalPrice(self):  # getter
        return self.__totalPrice

    @totalPrice.setter
    def totalPrice(self, value):  # setter
        self.__totalPrice = value

    @property
    def realtorName(self):  # getter
        return self.__realtorName

    @realtorName.setter
    def realtorName(self, value):  # setter
        self.__realtorName = value

    @property
    def representativeName(self):  # getter
        return self.__representativeName

    @representativeName.setter
    def representativeName(self, value):  # setter
        self.__representativeName = value

    @property
    def address(self):  # getter
        return self.__address

    @address.setter
    def address(self, value):  # setter
        self.__address = value

    @property
    def establishRegistrationNo(self):  # getter
        return self.__establishRegistrationNo

    @establishRegistrationNo.setter
    def establishRegistrationNo(self, value):  # setter
        self.__establishRegistrationNo = value

    @property
    def representativeTelNo(self):  # getter
        return self.__representativeTelNo

    @representativeTelNo.setter
    def representativeTelNo(self, value):  # setter
        self.__representativeTelNo = value

    @property
    def cellPhoneNo(self):  # getter
        return self.__cellPhoneNo

    @cellPhoneNo.setter
    def cellPhoneNo(self, value):  # setter
        self.__cellPhoneNo = value

    @property
    def cityName(self):  # getter
        return self.__cityName

    @cityName.setter
    def cityName(self, value):  # setter
        self.__cityName = value

    @property
    def divisionName(self):  # getter
        return self.__divisionName

    @divisionName.setter
    def divisionName(self, value):  # setter
        self.__divisionName = value

    @property
    def sectionName(self):  # getter
        return self.__sectionName

    @sectionName.setter
    def sectionName(self, value):  # setter
        self.__sectionName = value

    @property
    def detailAddress(self):  # getter
        return self.__detailAddress

    @detailAddress.setter
    def detailAddress(self, value):  # setter
        self.__detailAddress = value

    def to_print(self):
        print("detailAddress: ", self.detailAddress)
