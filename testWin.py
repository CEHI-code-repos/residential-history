from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import pandas as pd
from bs4 import BeautifulSoup
import re

#user = "leongmanchong@hotmail.com"
firstName = ""
lastName = ""
cityName = ""
chrome_path="C:\\Users\\ml69\\Desktop\\chromedriver.exe"

#fileName = ""
fileName = "C:\\Users\\ml69\\Desktop\\State_NJ.csv"
data = pd.read_csv(fileName, low_memory=False)[['NPI','Provider Last Name (Legal Name)','Provider First Name','Provider Business Practice Location Address City Name','Healthcare Provider Taxonomy Code_1']]
NPI = data['NPI'].tolist()
firstName = data['Provider First Name'].tolist()
lastName = data['Provider Last Name (Legal Name)'].tolist()
cityName = data['Provider Business Practice Location Address City Name'].tolist()
taxnCode = data['Healthcare Provider Taxonomy Code_1'].tolist()
#driver.implicitly_wait(5)
#driver.switch_to.frame('fraPCSearch')
#assert "Facebook" in driver.title
#outPutData = []
outPutSubData = []
#time.sleep(6)
outPutSubData1 = []
csv = open('123', "w") 
columnTitleRow = "NPI, 'Profession', 'License Type','License Status', 'Taxonomy Code' \n"
csv.write(columnTitleRow)
countCannotFind=[]
multipleResult=[]
#for i in range(len(firstName)):
for i in range(5000,5500,1)
    indicidor = 0
    try:
        driver=webdriver.Chrome(chrome_path)
        driver.get("https://newjersey.mylicense.com/verification_4_6/Search.aspx?facility=N")
        driver.maximize_window()
        elem = driver.find_element_by_id("t_web_lookup__first_name")
        elem.send_keys(firstName[i])
        elem = driver.find_element_by_id("t_web_lookup__last_name")
        elem.send_keys(lastName[i])
        elem = driver.find_element_by_id("t_web_lookup__addr_city")
        elem.send_keys(cityName[i])
    except TypeError as e:
        print("error is: ")
        print(e)
        driver.close()
        #outPutData.append([])
        continue


#elem = driver.find_element_by_id("pass")
#elem.send_keys(pwd)
    elem.send_keys(Keys.RETURN)
    #driver.implicitly_wait(5)
    html = driver.page_source
    bsObj = BeautifulSoup(html,"html.parser")
#for link in bsObj.find("td", {"id":"datagrip_results"}).findAll("a",id=re.compile("^(datagrip_results).*")):
#for link in bsObj.findAll("a", {"id":re.compile("^(datagrip_results).*")}):
#for link in bsObj:
    for link in bsObj.find("table", {"role":"presentation"}).findAll("a", id=re.compile("^(datagrid_results).*")):
#        print(link.text)
        outPutSubData.append(link.text)
    #outPutData.append(outPutSubData)
    if len(outPutSubData)==1:
        for link in bsObj.find("table", {"id":"datagrid_results"}).findAll("span"):
            outPutSubData1.append(link.text)
        #print(outPutSubData1)
        row = str(NPI[i]) + ',' + outPutSubData1[1]+ ',' + outPutSubData1[2] + ',' + outPutSubData1[3] + ',' + str(taxnCode[i]) + '\n'
        outPutSubData1 = []
        csv.write(row)
        print(row)
    elif len(outPutSubData)==0:
        countCannotFind.append(i)
    elif len(outPutSubData)>1:
        multipleResult.append(i)
    #print(outPutData)
    outPutSubData = []
    #for link in bsObj.find("table", {"id":"datagrid_results"}).findAll("span"):
        #print(link.text)
    #if link.findAll("a", id=re.compile("^(datagrip_results).*")):
    #    print("yes")
    print("\n")
    driver.close()


print("Those whose information cannot be find are:\n")
print(countCannotFind)
print("\n\n")
print("Those who have more than one results are: \n")
print(multipleResult)
