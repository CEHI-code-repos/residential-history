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
#chrome_options.add_argument("--headless")
chrome_path="C:\\Users\\ml69\\Desktop\\chromedriver.exe"
fileName = "C:\\Users\\ml69\\Desktop\\nameCEHI.csv"
rawData = pd.read_csv(fileName, low_memory=False)
inputData = rawData['Name'].tolist()
startTime=datetime.datetime.now()
#driver.implicitly_wait(5)
#driver.switch_to.frame('fraPCSearch')
outPutSubData = []
#time.sleep(6)
outPutSubData1 = []
numberSuccessfully = 1
for i in range(len(inputData)):
#for i in range(20):
    if i % 10 ==0:
        datetime.datetime.now()
        print("Running i = %d" %(i))
        print(datetime.datetime.now()-startTime)
    try:
        numberSuccessfully +=1
        driver=webdriver.Chrome(chrome_path,chrome_options=chrome_options)
        driver.get("https://pipl.com/")
        elem = driver.find_element_by_id("findall")
        elem.send_keys(inputData)
    except Exception as e:
        print("error is: ")
        print(e)
        driver.close()
        continue
    elem.send_keys(Keys.RETURN)
    time.sleep(6)
    html = driver.page_source
    bsObj = BeautifulSoup(html,"html.parser")
    with open("./" + inputData[i] + ".html", "w") as f:
        f.write(html)
        '''
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
            csv1.write(data['NPI'][i])
        elif len(outPutSubData)>1:
            multipleResult.append(i+2)
            csv2.write(data['NPI'][i])
        outPutSubData = []
        '''
    driver.close()

'''
print("There are totally %d samples were used\n%d of their information cannot be found\n%d of their information have more than one result" %(numberSuccessfully,len(countCannotFind),len(multipleResult)))
print("The rate for not having the information is %f \nThe rate for having multiple result is %f" %(len(countCannotFind)/numberSuccessfully, len(multipleResult)/numberSuccessfully))
print("It took " + str(datetime.datetime.now()-startTime) + " to run the script.")
'''


