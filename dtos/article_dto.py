if 1 == 1:
    import sys
    import os

    sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))


class ArticleDto:
    def __init__(self):
        # article 그룹
        self.__totalDongCount = ""  # 동 수(아파트)
        self.__roomCount = ""  # 방 수
        self.__bathroomCount = ""  # 욕실 수
        self.__moveInTypeName = ""  # 입주가능여부
        self.__parkingCount = ""  # 총 주차 대수
        self.__parkingPossibleYN = ""  # 주차 가능 여부
        self.__floorLayerName = ""  # 층 구조

        # addition 그룹
        self.__articleNo = ""  # 매물번호
        self.__articleName = ""  # 매물제목
        self.__realEstateTypeName = ""  # 매물유형
        self.__articleRealEstateTypeName = ""  # 건물용도
        self.__tradeTypeName = ""  # 거래유형
        self.__floorInfo = ""  # 층 정보
        self.__dealOrWarrantPrc = ""  # 금액 (한글)
        self.__area1 = ""  # 대지면적
        self.__area2 = ""  # 연면적
        self.__articleConfirmYmd = ""  # 게시일자
        self.__articleFeatureDesc = ""  # 글 내용
        self.__tagList = ""  # 태그목록

        # facility 그룹
        self.__directionTypeName = ""  # 방향
        self.__heatMethodTypeName = ""  # 난방방식
        self.__heatFuelTypeName = ""  # 난방연료
        self.__buildingUseAprvYmd = ""  # 사용승인일
        self.__buildingCoverageRatio = ""  # 매물정보/건폐율
        self.__floorAreaRatio = ""  # 매물정보/용적률

        # buildingRegister 그룹
        self.__allHoCnt = ""  # 총세대수
        self.__mainPurpsCdNm = ""  # 건축물용도
        self.__strctCdNm = ""  # 주구조
        self.__jiyukNm = ""  # 지역
        self.__generationUnit = ""  # 세대단위
        self.__jiguNm = ""  # 지구
        self.__guyukNm = ""  # 구역
        self.__useAprDay = ""  # 사용승인일
        self.__elvtInfo = ""  # 엘리베이터
        self.__etcParkInfo = ""  # 주차장
        self.__totalParkingCnt = ""  # 주차장대수
        self.__ugrndFlrCnt = ""  # 지하
        self.__grndFlrCnt = ""  # 지상
        self.__archArea = ""  # 건축면적
        self.__platArea = ""  # 대지면적
        self.__vlRatEstmTotArea = ""  # 연면적
        self.__bcRat = ""  # 건폐율
        self.__vlRat = ""  # 용적률

        # space 그룹
        self.__groundSpace = ""  # 대지지분

        # price 그룹
        self.__priceBySpace = ""  # 평당가격
        self.__rentPrice = ""  # 월세 (없는 경우가 더 많음)
        self.__dealPrice = ""  # 거래가격
        self.__warrantPrice = ""  # 보증금
        self.__allWarrantPrice = ""  # 기보증금
        self.__financePrice = ""  # 융자금
        self.__allRentPrice = ""  # 월세

        # articleTax 그룹
        self.__acquisitionTax = ""  # 취득세
        self.__brokerFee = ""  # 중개보수
        self.__maxBrokerFee = ""  # 중개보수 상한 요율
        self.__eduTax = ""  # 지방교육세
        self.__specialTax = ""  # 농어촌특별세
        self.__totalPrice = ""  # 세금 총 합계

        # realtor 그룹
        self.__realtorName = ""  # 중개사무소 이름
        self.__representativeName = ""  # 중개사무소 대표자
        self.__address = ""  # 중개사무소 주소
        self.__establishRegistrationNo = ""  # 중개사무소 등록번호
        self.__representativeTelNo = ""  # 중개사무소 전화번호
        self.__cellPhoneNo = ""  # 중개사무소 휴대전화번호

        # location 그룹
        self.__cityName = ""  # 시/도
        self.__divisionName = ""  # 시/군/구
        self.__sectionName = ""  # 읍/면/동
        self.__detailAddress = ""  # 상세주소

    @property
    def ugrndFlrCnt(self):  # getter
        return self.__ugrndFlrCnt

    @ugrndFlrCnt.setter
    def ugrndFlrCnt(self, value):  # setter
        self.__ugrndFlrCnt = value

    @property
    def bcRat(self):  # getter
        return self.__bcRat

    @bcRat.setter
    def bcRat(self, value):  # setter
        self.__bcRat = value

    @property
    def vlRat(self):  # getter
        return self.__vlRat

    @vlRat.setter
    def vlRat(self, value):  # setter
        self.__vlRat = value

    @property
    def vlRatEstmTotArea(self):  # getter
        return self.__vlRatEstmTotArea

    @vlRatEstmTotArea.setter
    def vlRatEstmTotArea(self, value):  # setter
        self.__vlRatEstmTotArea = value

    @property
    def platArea(self):  # getter
        return self.__platArea

    @platArea.setter
    def platArea(self, value):  # setter
        self.__platArea = value

    @property
    def archArea(self):  # getter
        return self.__archArea

    @archArea.setter
    def archArea(self, value):  # setter
        self.__archArea = value

    @property
    def floorAreaRatio(self):  # getter
        return self.__floorAreaRatio

    @floorAreaRatio.setter
    def floorAreaRatio(self, value):  # setter
        self.__floorAreaRatio = value

    @property
    def buildingCoverageRatio(self):  # getter
        return self.__buildingCoverageRatio

    @buildingCoverageRatio.setter
    def buildingCoverageRatio(self, value):  # setter
        self.__buildingCoverageRatio = value

    @property
    def grndFlrCnt(self):  # getter
        return self.__grndFlrCnt

    @grndFlrCnt.setter
    def grndFlrCnt(self, value):  # setter
        self.__grndFlrCnt = value

    @property
    def totalParkingCnt(self):  # getter
        return self.__totalParkingCnt

    @totalParkingCnt.setter
    def totalParkingCnt(self, value):  # setter
        self.__totalParkingCnt = value

    @property
    def etcParkInfo(self):  # getter
        return self.__etcParkInfo

    @etcParkInfo.setter
    def etcParkInfo(self, value):  # setter
        self.__etcParkInfo = value

    @property
    def elvtInfo(self):  # getter
        return self.__elvtInfo

    @elvtInfo.setter
    def elvtInfo(self, value):  # setter
        self.__elvtInfo = value

    @property
    def useAprDay(self):  # getter
        return self.__useAprDay

    @useAprDay.setter
    def useAprDay(self, value):  # setter
        self.__useAprDay = value

    @property
    def guyukNm(self):  # getter
        return self.__guyukNm

    @guyukNm.setter
    def guyukNm(self, value):  # setter
        self.__guyukNm = value

    @property
    def jiguNm(self):  # getter
        return self.__jiguNm

    @jiguNm.setter
    def jiguNm(self, value):  # setter
        self.__jiguNm = value

    @property
    def generationUnit(self):  # getter
        return self.__generationUnit

    @generationUnit.setter
    def generationUnit(self, value):  # setter
        self.__generationUnit = value

    @property
    def jiyukNm(self):  # getter
        return self.__jiyukNm

    @jiyukNm.setter
    def jiyukNm(self, value):  # setter
        self.__jiyukNm = value

    @property
    def strctCdNm(self):  # getter
        return self.__strctCdNm

    @strctCdNm.setter
    def strctCdNm(self, value):  # setter
        self.__strctCdNm = value

    @property
    def mainPurpsCdNm(self):  # getter
        return self.__mainPurpsCdNm

    @mainPurpsCdNm.setter
    def mainPurpsCdNm(self, value):  # setter
        self.__mainPurpsCdNm = value

    @property
    def allHoCnt(self):  # getter
        return self.__allHoCnt

    @allHoCnt.setter
    def allHoCnt(self, value):  # setter
        self.__allHoCnt = value

    @property
    def buildingUseAprvYmd(self):  # getter
        return self.__buildingUseAprvYmd

    @buildingUseAprvYmd.setter
    def buildingUseAprvYmd(self, value):  # setter
        self.__buildingUseAprvYmd = value

    @property
    def heatMethodTypeName(self):  # getter
        return self.__heatMethodTypeName

    @heatMethodTypeName.setter
    def heatMethodTypeName(self, value):  # setter
        self.__heatMethodTypeName = value

    @property
    def heatFuelTypeName(self):  # getter
        return self.__heatFuelTypeName

    @heatFuelTypeName.setter
    def heatFuelTypeName(self, value):  # setter
        self.__heatFuelTypeName = value

    @property
    def groundSpace(self):  # getter
        return self.__groundSpace

    @groundSpace.setter
    def groundSpace(self, value):  # setter
        self.__groundSpace = value

    @property
    def directionTypeName(self):  # getter
        return self.__directionTypeName

    @directionTypeName.setter
    def directionTypeName(self, value):  # setter
        self.__directionTypeName = value

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

    def get_dict(self) -> dict:
        return {
            "게시일자": self.articleConfirmYmd,
            "구분": self.articleRealEstateTypeName,
            "매물유형": self.realEstateTypeName,
            "매물제목": self.articleName,
            "거래유형": self.tradeTypeName,
            "표시금액": self.dealOrWarrantPrc,
            "평당가격": self.priceBySpace,
            "층 정보": self.floorInfo,
            "층 구조": self.floorLayerName,
            "방 수": self.roomCount,
            "향": self.directionTypeName,
            "대지면적": self.area1,
            "연면적": self.area2,
            "소재지": self.detailAddress,
            "매물특징": self.articleFeatureDesc,
            "대지/연면적": f"{self.area1}/{self.area2}",
            "해당층/총층": f"{self.floorInfo}층",
            "대지지분": self.groundSpace,
            "용적률/건폐율": f"{self.buildingCoverageRatio}/{self.floorAreaRatio}",
            "방수/욕실수": f"{self.roomCount}/{self.bathroomCount}",
            "월관리비": f"원",
            "관리비 포함": f"",
            "입주가능일": self.moveInTypeName,
            "융자금": self.financePrice,
            "기보증금/월세": f"{self.allWarrantPrice}/{self.allRentPrice}",
            "방향": f"{self.directionTypeName}",
            "주차가능여부": self.parkingPossibleYN,
            "난방(방식/연료)": f"{self.heatMethodTypeName}/{self.heatFuelTypeName}",
            "사용승인일": f"{self.buildingUseAprvYmd}",
            "총세대수": self.allHoCnt,
            "총주차대수": self.parkingCount,
            "용도지역": f"",
            "건축물 용도": self.mainPurpsCdNm,
            "주구조": self.strctCdNm,
            "매물번호": self.articleNo,
            "중개사 이름": self.realtorName,
            "중개사 대표자": self.representativeName,
            "중개사 등록번호": self.establishRegistrationNo,
            "중개사 주소": self.address,
            "중개사 전화번호": self.representativeTelNo,
            "중개사 휴대전화번호": self.cellPhoneNo,
            "중개보수": self.brokerFee,
            "상한 요율": self.maxBrokerFee,
            "세금 합계": self.totalPrice,
            "취득세": self.acquisitionTax,
            "지방교육세": self.eduTax,
            "농어촌특별세": self.specialTax,
            "주 용도": self.mainPurpsCdNm,
            "총 세대": f"{self.allHoCnt}{self.generationUnit}",
            "지역": self.jiyukNm,
            "지구": self.jiguNm,
            "구역": self.guyukNm,
            "사용승인일": self.useAprDay,
            "층정보": f"지하 {self.ugrndFlrCnt}층 / 지상 {self.grndFlrCnt}층",
            "주구조": self.strctCdNm,
            "주차장": f"총 {self.totalParkingCnt}대{self.etcParkInfo}",
            "엘리베이터": f"{self.elvtInfo}",
            "건축면적": f"{self.archArea}",
            "대지면적_2": f"{self.platArea}",
            "연면적_2": f"{self.vlRatEstmTotArea}",
            "건폐율": f"{self.bcRat}",
            "용적률": f"{self.vlRat}",
            # "시/도": self.cityName,
            # "시/군/구": self.divisionName,
            # "읍/면/동": self.sectionName,
            # "동 수": self.totalDongCount,
            # "욕실 수": self.bathroomCount,
            # "거래가격": self.dealPrice,
            # "태그목록": self.tagList,
        }
