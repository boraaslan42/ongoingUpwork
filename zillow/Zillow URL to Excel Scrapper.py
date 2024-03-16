import requests
import json
import pandas as pd

# https://www.zillow.com/ny/?searchQueryState=%7B"pagination"%3A%7B%7D%2C"isMapVisible"%3Afalse%2C"mapBounds"%3A%7B"west"%3A-79.76259%2C"east"%3A-71.777491%2C"south"%3A40.477399%2C"north"%3A45.015865%7D%2C"usersSearchTerm"%3A"NY"%2C"regionSelection"%3A%5B%7B"regionId"%3A43%2C"regionType"%3A2%7D%5D%2C"filterState"%3A%7B"sort"%3A%7B"value"%3A"days"%7D%2C"ah"%3A%7B"value"%3Atrue%7D%7D%2C"isListVisible"%3Atrue%7D
url=input("Enter the url: ")
fileName=input("Enter the file name: ")
headers = {
    "authority": "www.zillow.com",
    "accept": "*/*",
    "accept-language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
    "content-type": "application/json",
    "cookie": 'zguid=24|%24abac79bb-72ad-4d9e-9dde-b1751e59deae; _ga=GA1.2.680147625.1692801387; zjs_anonymous_id=%22abac79bb-72ad-4d9e-9dde-b1751e59deae%22; zjs_user_id=null; zg_anonymous_id=%22a2ea7840-c28b-4f1b-8a00-69913b909e63%22; _hp2_id.1215457233=%7B%22userId%22%3A%222522749834967336%22%2C%22pageviewId%22%3A%226913396349729521%22%2C%22sessionId%22%3A%22503083603946677%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D; __pdst=c1df509b570446c28d6bf779e3e32721; _pxvid=729a779c-41c2-11ee-a58d-0dbd2da9169f; _pin_unauth=dWlkPU56azFOalJqWVRBdE5tUmtNaTAwWldZd0xXRXhOVEV0TjJRM01HWTJNbVUxTkdJeQ; JSESSIONID=D50653869FEDC01AC352F4F8369937DF; zgsession=1|ec6c4446-4ae0-4492-98df-e3b878930d6f; _gid=GA1.2.1968072043.1706285815; AWSALB=xRKyk0l88mL8RY57Yel+w3B/nab1GWQNxoht/Mu2hxABpTULFbnTG3SAsw+oma1ba/yjo2+mvN/f96CESJFJM7uP5WDeuOKAkI6KgJ/O0pAWu7PEUfVWN4GArDD5; AWSALBCORS=xRKyk0l88mL8RY57Yel+w3B/nab1GWQNxoht/Mu2hxABpTULFbnTG3SAsw+oma1ba/yjo2+mvN/f96CESJFJM7uP5WDeuOKAkI6KgJ/O0pAWu7PEUfVWN4GArDD5; g_state={"i_p":1706372217990,"i_l":2}; _gcl_au=1.1.217113811.1706285818; DoubleClickSession=true; _uetsid=54e2c690bc6611ee80e08bb598d45fbc; _uetvid=736f3ff041c211ee80bd31235bff95e5; _clck=1a2goaf%7C2%7Cfiq%7C0%7C1330; _gat=1; search=6|1708877940455%7Crect%3D44.28919455063632%2C-106.45264509375001%2C29.855816427991694%2C-132.16065290625%26rid%3D9%26disp%3Dmap%26mdm%3Dauto%26p%3D1%26z%3D1%26listPriceActive%3D1%26price%3D2500000-%26mp%3D12488-%26fs%3D1%26fr%3D0%26mmm%3D0%26rs%3D0%26ah%3D0%26singlestory%3D0%26housing-connector%3D0%26abo%3D0%26garage%3D0%26pool%3D0%26ac%3D0%26waterfront%3D0%26finished%3D0%26unfinished%3D0%26cityview%3D0%26mountainview%3D0%26parkview%3D0%26waterview%3D0%26hoadata%3D1%26zillow-owned%3D0%263dhome%3D0%26featuredMultiFamilyBuilding%3D0%26student-housing%3D0%26income-restricted-housing%3D0%26military-housing%3D0%26disabled-housing%3D0%26senior-housing%3D0%26commuteMode%3Ddriving%26commuteTimeOfDay%3Dnow%09%099%09%7B%22isList%22%3Atrue%2C%22isMap%22%3Afalse%7D%09%09%09%09%09; _clsk=s4ie5e%7C1706285940967%7C8%7C0%7Cu.clarity.ms%2Fcollect; search=6|1708878079065%7Crect%3D44.28919455063632%2C-106.45264509375001%2C29.855816427991694%2C-132.16065290625%26rid%3D9%26disp%3Dmap%26mdm%3Dauto%26p%3D2%26z%3D1%26listPriceActive%3D1%26price%3D2500000-%26mp%3D12488-%26fs%3D1%26fr%3D0%26mmm%3D0%26rs%3D0%26ah%3D0%26singlestory%3D0%26housing-connector%3D0%26abo%3D0%26garage%3D0%26pool%3D0%26ac%3D0%26waterfront%3D0%26finished%3D0%26unfinished%3D0%26cityview%3D0%26mountainview%3D0%26parkview%3D0%26waterview%3D0%26hoadata%3D1%26zillow-owned%3D0%263dhome%3D0%26featuredMultiFamilyBuilding%3D0%26student-housing%3D0%26income-restricted-housing%3D0%26military-housing%3D0%26disabled-housing%3D0%26senior-housing%3D0%26commuteMode%3Ddriving%26commuteTimeOfDay%3Dnow%09%099%09%7B%22isList%22%3Atrue%2C%22isMap%22%3Afalse%7D%09%09%09%09%09; x-amz-continuous-deployment-state=AYABeA+m5kqw1F2aYT7PqxaVvGsAPgACAAFEAB1kM2Jsa2Q0azB3azlvai5jbG91ZGZyb250Lm5ldAABRwAVRzA3MjU1NjcyMVRZRFY4RDcyVlpWAAEAAkNEABpDb29raWUAAACAAAAADFT6ITIB595nsyjWgAAwJ8Gb9978%2FXPm59tRlUQuYcNI3OEGGKWI+NuXrBhEgj3xfrb4XMoW37XSx0Fu79FGAgAAAAAMAAQAAAAAAAAAAAAAAAAAAJ2PhuYpbN2WZs9Kcsl0pez%2F%2F%2F%2F%2FAAAAAQAAAAAAAAAAAAAAAQAAAAwyMKdAzfZUh%2F+Vml+zi6CWm5YE84qyzaP4MfID',
    "origin": "https://www.zillow.com",
    "referer": "https://www.zillow.com/ca/?searchQueryState=%7B%22isMapVisible%22%3Afalse%2C%22mapBounds%22%3A%7B%22north%22%3A44.28919455063632%2C%22south%22%3A29.855816427991694%2C%22east%22%3A-106.45264509375001%2C%22west%22%3A-132.16065290625%7D%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22price%22%3A%7B%22min%22%3A2500000%7D%2C%22mp%22%3A%7B%22min%22%3A12488%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A6%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A9%2C%22regionType%22%3A2%7D%5D%2C%22pagination%22%3A%7B%7D%7D",
    "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
}

def processSeleniumUrl(originalUrl):
    url=requests.utils.unquote(originalUrl).split("?")[-1]
    if "wants" not in url:
        processedUrl='{"searchQueryState"'+":"+url[17:]+',"wants": {"cat1": ["listResults"], "cat2": ["total"]},"requestId": 8,"isDebugRequest": false}'
    return processedUrl

def getTotalPageNumber(payload=processSeleniumUrl(url)):
    url = "https://www.zillow.com/async-create-search-page-state"
    response = requests.request("PUT", url, headers=headers, data=payload)
    json_data = json.loads(response.text)
    return json_data["cat1"]["searchList"]["totalPages"]

def getHousesPerPage(pagination, payload=processSeleniumUrl(url), headers=headers):
    url = "https://www.zillow.com/async-create-search-page-state"
    json_data = json.loads(payload)
    json_data["searchQueryState"]["pagination"]["currentPage"] = pagination
    payload = json.dumps(json_data)
    response = requests.request("PUT", url, headers=headers, data=payload)
    json_data = json.loads(response.text)
    return json_data["cat1"]["searchResults"]["listResults"]

def append_toXlsx(dictionaryList, fileName):
    try:
        df_existing = pd.read_excel(fileName)
        print(fileName + " exists")
    except:
        print("File does not exist creating file: " + fileName)
        df_existing = None
    df_new = pd.DataFrame(dictionaryList)
    df_combined = pd.concat([df_existing, df_new], ignore_index=True)
    with pd.ExcelWriter(fileName, engine="openpyxl") as writer:
        df_combined.to_excel(writer, index=False, sheet_name="Sheet")
    print("Data is appended to", fileName)


excelList=[]

totalPageNumber = 30

for i in range(1, totalPageNumber + 1):
    print("Scraping page:", i, "/", totalPageNumber)    
    houseList = getHousesPerPage(i)
    for house in houseList:
        data = {}
        testWords = [
            "address",
            "brokerName",
            "detailUrl",
            "imgSrc",
            "price",
            "marketingStatusSimplifiedCd",
            "address",
            "addressZipcode",
            "beds",
            "baths",
            "area",
        ]
        DictWords = [
            "Address",
            "Agent",
            "Listing Url",
            "Main Image Url",
            "Price",
            "Marketing Status",
            "Address",
            "Address Zipcode",
            "Beds",
            "Baths",
            "Sqft Area",
        ]
        for dictWord, testWord in zip(DictWords, testWords):
            try:
                if dictWord == "Baths":
                    data[dictWord] = int(house[testWord])

                else:
                    data[dictWord] = house[testWord]
            except:
                data[dictWord] = "NA"
        testWords2 = ["homeType", "zestimate", "rentZestimate", "daysOnZillow"]
        dictWords2 = ["Home Type", "Zestimate", "Rent Zestimate", "Days On Zillow"]
        for dictWord, testWord in zip(dictWords2, testWords2):
            try:
                if testWord == "zestimate" or testWord == "rentZestimate":

                    data[dictWord] = "$" + processCommas(
                        house["hdpData"]["homeInfo"][testWord]
                    )

                else:
                    data[dictWord] = house["hdpData"]["homeInfo"][testWord]
            except:
                data[dictWord] = "NA"
        try:            
            cp=house["carouselPhotos"]
            listt=[]
            for url in cp:
                listt.append(url["url"])
            data["House Photos"]=listt
        except:
            data["Carousel Photos"] = "NA"
        excelList.append(data)
        
# given data MUST be a LIST that has DICTS with same key names as ELEMENTS

#appends data to xlsx file, does not deletes the existing data

#creates a new file if the file does not exist in cd



append_toXlsx(excelList, fileName+".xlsx")