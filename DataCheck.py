import DataProcess

def DataCheck(title, price, URL, time, text, site):

    SmartPhoneDeclares = ["아이폰", "갤럭시", "갤럭시 노트", "갤럭시노트", "LG V50", "LG V40", "LG V35", "LG V30", "LG G8", "LG G7"]
    TabletDeclares = ["아이패드", "태블릿", "갤탭", "갤럭시탭"]
    SmartWatchDeclares = ["스마트워치", "애플워치"]

    DigitalCameraDeclares = ["디지털카메라", "디지털 카메라"]
    DSLRDeclares = ["DSLR"]
    ActionCameraDeclares = ["액션캠", "액션 캠"]

    KimchiRefrigeratorDeclares = ["김치냉장고", "김치 냉장고"]
    RefrigeratorDeclares = ["냉장고"]
    ElectronicRiceDeclares = ["전기밥솥"]
    InductionDeclares = ["인덕션", "전기레인지"]
    ElectronicDeclares = ["전자레인지"]
    OvenDeclares = ["오븐"]
    ElctronicPortDeclares = ["전기포트", "전기주전"]
    MixerDeclares = ["믹서기"]
    CoffeeMachineDeclares = ["커피머신"]
    DishesWashingDeclares = ["식기세척기"]
    DishesDryingDeclares = ["식기건조기"]
    FoodTrashDeclares = ["음식물처리기", "음식물 처리기"]

    WasherDeclares = ["세탁기", "통돌이"]
    ElectronicCleaningDeclares = ["청소기"]

    TVDeclares = ["TV", "텔레비젼", "텔레비전"]
    AirConditionDeclares = ["에어컨"]
    HeaterDeclares = ["난방기"]
    AirWasherDeclares = ["공기청정기"]
    HumidificationDeclares = ["가습기"]
    DehumidificationDeclares = ["제습기"]
    WaterPuriferDeclares = ["정수기"]

    DeskTopDeclares = ["데스크탑", "PC", "게이밍PC", "컴퓨터 본체", "컴퓨터본체"]
    MonitorDeclares = ["모니터"]
    KeyboardDeclares = ["키보드"]
    MouseDeclares = ["마우스"]
    efmDeclares = ["공유기"]

    LaptopDeclares = ["노트북", "맥북", "MACBOOK", "넷북", "탭북", "그램"]
    PrinterScannerDeclares = ["복합기"]
    PrinterDeclares = ["프린터"]
    ScannerDeclares = ["스캐너"]

    GameMachineDeclares = ["닌텐도", "PSP", "PS4", "플스4", "플레이스테이션", "XBOX"]
    SpeakerDeclares = ["스피커"]
    HeadPhoneDeclares = ["이어폰", "헤드셋", "헤드폰", "에어팟", "갤럭시버즈", "차이팟"]

    title = title.upper()
    text = text.upper()


    for Declare in SmartPhoneDeclares:
        if Declare in title:
            DataProcess.SmartPhone(title, price, URL, time, text, site)
            return
    for Declare in TabletDeclares:
        if Declare in title:
            DataProcess.Tablet(title, price, URL, time, text, site)
            return
    for Declare in SmartWatchDeclares:
        if Declare in title:
            DataProcess.SmartWatch(title, price, URL, time, text, site)
            return

    for Declare in DigitalCameraDeclares:
        if Declare in title:
            DataProcess.DigitalCamera(title, price, URL, time, text, site)
            return
    for Declare in DSLRDeclares:
        if Declare in title:
            DataProcess.DSLR(title, price, URL, time, text, site)
            return
    for Declare in ActionCameraDeclares:
        if Declare in title:
            DataProcess.ActionCamera(title, price, URL, time, text, site)
            return

    for Declare in KimchiRefrigeratorDeclares:
        if Declare in title:
            DataProcess.KimchiRefrigerator(title, price, URL, time, text, site)
            return
    for Declare in RefrigeratorDeclares:
        if Declare in title:
            DataProcess.Refrigerator(title, price, URL, time, text, site)
            return
    for Declare in ElectronicRiceDeclares:
        if Declare in title:
            DataProcess.ElectronicRice(title, price, URL, time, text, site)
            return
    for Declare in InductionDeclares:
        if Declare in title:
            DataProcess.Induction(title, price, URL, time, text, site)
            return
    for Declare in ElectronicDeclares:
        if Declare in title:
            DataProcess.Electronic(title, price, URL, time, text, site)
            return
    for Declare in OvenDeclares:
        if Declare in title:
            DataProcess.Oven(title, price, URL, time, text, site)
            return
    for Declare in ElctronicPortDeclares:
        if Declare in title:
            DataProcess.ElctronicPort(title, price, URL, time, text, site)
            return
    for Declare in MixerDeclares:
        if Declare in title:
            DataProcess.Mixer(title, price, URL, time, text, site)
            return
    for Declare in CoffeeMachineDeclares:
        if Declare in title:
            DataProcess.CoffeeMachine(title, price, URL, time, text, site)
            return
    for Declare in DishesWashingDeclares:
        if Declare in title:
            DataProcess.DishesWashing(title, price, URL, time, text, site)
            return
    for Declare in DishesDryingDeclares:
        if Declare in title:
            DataProcess.DishesDrying(title, price, URL, time, text, site)
            return
    for Declare in FoodTrashDeclares:
        if Declare in title:
            DataProcess.FoodTrash(title, price, URL, time, text, site)
            return

    for Declare in WasherDeclares:
        if Declare in title:
            DataProcess.Washer(title, price, URL, time, text, site)
            return
    for Declare in ElectronicCleaningDeclares:
        if Declare in title:
            DataProcess.ElectronicCleaning(title, price, URL, time, text, site)
            return

    for Declare in TVDeclares:
        if Declare in title:
            DataProcess.TV(title, price, URL, time, text, site)
            return
    for Declare in AirConditionDeclares:
        if Declare in title:
            DataProcess.AirCondition(title, price, URL, time, text, site)
            return
    for Declare in HeaterDeclares:
        if Declare in title:
            DataProcess.Heater(title, price, URL, time, text, site)
            return
    for Declare in AirWasherDeclares:
        if Declare in title:
            DataProcess.AirWasher(title, price, URL, time, text, site)
            return
    for Declare in HumidificationDeclares:
        if Declare in title:
            DataProcess.Humidification(title, price, URL, time, text, site)
            return
    for Declare in DehumidificationDeclares:
        if Declare in title:
            DataProcess.Dehumidification(title, price, URL, time, text, site)
            return
    for Declare in WaterPuriferDeclares:
        if Declare in title:
            DataProcess.WaterPurifer(title, price, URL, time, text, site)
            return

    for Declare in GameMachineDeclares:
        if Declare in title:
            DataProcess.GameMachine(title, price, URL, time, text, site)
            return
    for Declare in DeskTopDeclares:
        if Declare in title:
            DataProcess.DestkTop(title, price, URL, time, text, site)
            return
    for Declare in MonitorDeclares:
        if Declare in title:
            DataProcess.Monitor(title, price, URL, time, text, site)
            return
    for Declare in KeyboardDeclares:
        if Declare in title:
            DataProcess.Keyboard(title, price, URL, time, text, site)
            return
    for Declare in MouseDeclares:
        if Declare in title:
            DataProcess.Mouse(title, price, URL, time, text, site)
            return
    for Declare in efmDeclares:
        if Declare in title:
            DataProcess.efm(title, price, URL, time, text, site)
            return

    for Declare in LaptopDeclares:
        if Declare in title:
            DataProcess.Laptop(title, price, URL, time, text, site)
            return
    for Declare in PrinterScannerDeclares:
        if Declare in title:
            DataProcess.PrinterScanner(title, price, URL, time, text, site)
            return
    for Declare in PrinterDeclares:
        if Declare in title:
            DataProcess.Printer(title, price, URL, time, text, site)
            return
    for Declare in ScannerDeclares:
        if Declare in title:
            DataProcess.Scanner(title, price, URL, time, text, site)
            return

    for Declare in SpeakerDeclares:
        if Declare in title:
            DataProcess.Speaker(title, price, URL, time, text, site)
            return
    for Declare in HeadPhoneDeclares:
        if Declare in title:
            DataProcess.HeadPhone(title, price, URL, time, text, site)
            return

    return False