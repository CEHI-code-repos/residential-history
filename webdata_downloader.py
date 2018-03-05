from urllib.request import urlopen
from urllib.error import HTTPError
import argparse
from bs4 import BeautifulSoup
import re
from urllib.request import urlretrieve
import subprocess
import os
if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser(description = "enter a link")
        parser.add_argument("-url", help = "enter a link")
        parser.add_argument("-years", help="Enter a range of years. For example: 2002-2012")
        args = parser.parse_args()
        indicator = 1
        yearsPeriod = args.years.split("-")
        beginningYear = yearsPeriod[0]
        endYear = yearsPeriod[-1]
    except HTTPError as e:
        print("the error is as followings:/n", e)
        indicator = None
    else:
        htmlcontext = urlopen(args.url)
        bsObj = BeautifulSoup(htmlcontext,"html.parser")
        context = bsObj.findAll("a",{"href":re.compile(".*\.(csv|zip)")})
        currentWorkingDirectory = os.getcwd()
        for currentYears in range(int(beginningYear), int(endYear)+1):
            subprocess.call(['mkdir',str(currentYears)])
        for files in context:
            downLink = files["href"]
            fileName = downLink.split("/")[-1]
            for currentYears in range(int(beginningYear), int(endYear)+1):
                if str(currentYears) in downLink:
                    if "36km" in downLink:
                        print("There is a file including 36km, it will be skipped \n")
                    else:
                        print("The file going to be downloaded is: " + files["href"])
                        #print("\n")
                        #subprocess.call(['mkdir',str(currentYears)])
                        print("It will be in: " + currentWorkingDirectory + "/" + str(currentYears) + "/")
                        #subprocess.call(['cd',str(currentYears)])
                        os.chdir(currentWorkingDirectory + "/" + str(currentYears))
                        urlretrieve(files["href"], fileName)
                        print("Download " + fileName + " successfully! \n")
                        #os.chdir(currentWorkingDirectory + "/")
                        #subprocess.call(['cd',str(currentYears)])
