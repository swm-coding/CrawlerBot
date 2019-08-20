def isLaptopPost(title):
    title = title.lower()
    LaptopDeclares = ["노트북","맥북","macbook","넷북","탭북","그램"]

    for Declare in LaptopDeclares:
        if Declare in title:
            return True
    
    return False
