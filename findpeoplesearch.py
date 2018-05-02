from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.keys import Keys
import time
fileName = '/Users/manchongleong/Desktop/nameCEHI.csv'
rawData = pd.read_csv(fileName, low_memory=False)
inputData = rawData['Name'].tolist()
for i in range(len(inputData)):
    dr = webdriver.Chrome('/Users/manchongleong/Desktop/chromedriver')
    dr.get("https://www.findpeoplesearch.com/")
    elem = dr.find_element_by_id("full_name")
    print(inputData[i])
    elem.send_keys(inputData[i])
    elem.send_keys(Keys.RETURN)
    time.sleep(2)
    #dr.find_element_by_xpath('//*[@id="match_results"]/div[2]/div[1]/div[2]/div[1]/a').click()
    with open('./' + inputData[i] + '.html', "w") as f:
        f.write(dr.page_source)
    dr.close()
