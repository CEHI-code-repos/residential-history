from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
fileName = '/Users/manchongleong/Desktop/nameCEHI.csv'
rawData = pd.read_csv(fileName, low_memory=False)
inputData = rawData['Name'].tolist()
for i in range(len(inputData)):
    dr = webdriver.Chrome('/Users/manchongleong/Desktop/chromedriver')
    dr.get("https://www.beenverified.com/people/")
    elemFirstName = dr.find_element_by_id("fn")
    elemLastName = dr.find_element_by_id("ln")
    print(inputData[i])
    elemFirstName.send_keys(inputData[i].split(" ")[0])
    elemLastName.send_keys(inputData[i].split(" ")[1])
    elemLastName.send_keys(Keys.RETURN)
    time.sleep(60)
    #dr.find_element_by_xpath('//*[@id="beenverified_results_list"]/ul/li/div[2]/p[1]/a[1]').click()
    with open('./' + inputData[i] + '.html', "w") as f:
        f.write(dr.page_source)
    dr.close()
