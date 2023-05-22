<script type="text/javascript">
    var imgUrl = "https://ssl.pstatic.net/static.land/static/space/2023032017";
    var pinfra = "https://landthumb-phinf.pstatic.net";
    var fromDA = "";
    var jsonPageData = {
        ipLat: '',
        ipLng: '',
        ipCortar: '',
        openKey: '',
        mkrType: '',
        sortType: '',
        isFromNaver: 'Y',
        subModule: '',
        isNnhscp: 'N',
        isAdd: '',
        isSmallSpcRent: '',
        pathParam: {},
        showon: '',
        
        filter: {
            lat: '37.59309',
            lon: '127.160938',
            z: '14',
            cortarNo: '4131010500',
            cortarNm: '수택동',
            rletTpCds: '*',
            tradTpCds: 'A1:B1:B2'
        },
        
    };
    var _iniFunc = function () {
        var _MapPageid = 'mapSearch';
        if (land.jpage) {
            if (land.jpage._pages[_MapPageid] && !land.jpage._pages[_MapPageid].mainobject) {
                if (land.map === undefined) {
                    //call lazy loader
                    land.jpage.scriptLazyLoader(_MapPageid)
                } else {
                    if (typeof naver === "undefined" || (typeof naver !== "undefined" && typeof naver.maps === "undefined")) {
                        baseScript.loadScript('https://oapi.map.naver.com/openapi/maps3.js?submodules=panorama&stamp=' + baseScript.panoTimeStamp, _iniFunc);
                    } else {
                        land.map.jsonPageData = jsonPageData;
                        land.jpage.appendOO(land.map, _MapPageid);
                    }
                }
            }
        }
        $(document).off("jPageReady", _iniFunc);
        $(document).off("_pushStateChanged", _iniFunc);
        $(document).off("_popStateChanged", _iniFunc);
    };
    $(document).on("jPageReady", _iniFunc);
    $(document).on("_pushStateChanged", _iniFunc);
    $(document).on("_popStateChanged", _iniFunc);
</script>