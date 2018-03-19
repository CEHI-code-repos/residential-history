from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.keys import Keys
import pandas as pd
from bs4 import BeautifulSoup
import re
#from time import gmtime, strftime
import datetime
chrome_options = Options()  
chrome_options.add_argument("--headless")
#user = "leongmanchong@hotmail.com"
firstName = ""
lastName = ""
cityName = ""
chrome_path="C:\\Users\\ml69\\Desktop\\chromedriver.exe"
#chrome_path="/Users/manchongleong/Desktop/Taxonomy/chromedriver"
#fileName = ""
#fileName = "/Users/manchongleong/Desktop/Crate/Geodata/US/National_Provider_Identifier/NPIDatabase_2015/NPPES_Data_Dissemination_July_2015/Original_state/State_NJ.csv"
#fileName = ""
fileName = "C:\\Users\\ml69\\Desktop\\State_NJ.csv"
data = pd.read_csv(fileName, low_memory=False)[['NPI','Entity Type Code','Provider Last Name (Legal Name)','Provider First Name','Provider Business Practice Location Address City Name','Healthcare Provider Taxonomy Code_1']]
startTime=datetime.datetime.now()
#NPI = data['NPI'].tolist()
#firstName = data['Provider First Name'].tolist()
#lastName = data['Provider Last Name (Legal Name)'].tolist()
#cityName = data['Provider Business Practice Location Address City Name'].tolist()
#taxnCode = data['Healthcare Provider Taxonomy Code_1'].tolist()
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
numberSuccessfully = 1
for i in range(round(len(firstName)/2)):
#for i in range(20):
    if i % 10 ==0:
        datetime.datetime.now()
        print("Running i = %d" %(i))
        print(datetime.datetime.now()-startTime)
    if data['Entity Type Code'][i] == 1:
        try:
            numberSuccessfully +=1
            driver=webdriver.Chrome(chrome_path,chrome_options=chrome_options)
            driver.get("https://newjersey.mylicense.com/verification_4_6/Search.aspx?facility=N")
            elem = driver.find_element_by_id("t_web_lookup__first_name")
            elem.send_keys(data['Provider First Name'][i])
            elem = driver.find_element_by_id("t_web_lookup__last_name")
            elem.send_keys(data['Provider Last Name (Legal Name)'][i])
            elem = driver.find_element_by_id("t_web_lookup__addr_city")
            elem.send_keys(data['Provider Business Practice Location Address City Name'][i])
        except Exception as e:
            print("error is: ")
            print(e)
            driver.close()
            continue


        elem.send_keys(Keys.RETURN)
        html = driver.page_source
        bsObj = BeautifulSoup(html,"html.parser")
        for link in bsObj.find("table", {"role":"presentation"}).findAll("a", id=re.compile("^(datagrid_results).*")):
            outPutSubData.append(link.text)
        if len(outPutSubData)==1:
            for link in bsObj.find("table", {"id":"datagrid_results"}).findAll("span"):
                outPutSubData1.append(link.text)
            row = str(data['NPI'][i]) + ',' + outPutSubData1[1]+ ',' + outPutSubData1[2] + ',' + outPutSubData1[3] + ',' + str(data['Healthcare Provider Taxonomy Code_1'][i])
            outPutSubData1 = []
            csv.write(row)
        elif len(outPutSubData)==0:
            countCannotFind.append(i+2)
        elif len(outPutSubData)>1:
            multipleResult.append(i+2)
        outPutSubData = []
        driver.close()


print("There are totally %d samples were used\n%d of their information cannot be found\n%d of their information have more than one result" %(numberSuccessfully,len(countCannotFind),len(multipleResult)))
print("The rate for not having the information is %f \nThe rate for having multiple result is %f" %(len(countCannotFind)/numberSuccessfully, len(multipleResult)/numberSuccessfully))
print("It took " + str(datetime.datetime.now()-startTime) + " to run the script.")

csv1 = open('countCannotFind', "w")
csv1.write(','.join(str(x) for x in countCannotFind))
csv2 = open('multipleResult', "w")
csv2.write(','.join(str(x) for x in multipleResult))




