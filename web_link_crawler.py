from urllib.request import urlopen
from urllib.error import HTTPError
import argparse
from bs4 import BeautifulSoup

if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser(description="Enter the link")
        parser.add_argument("-url", help="Enter a link")
        #parser.add_argument("-tag", help="Enter a tag")
        args = parser.parse_args()
    except HTTPError as e:
        print("The error message is the followings:\n", p)
        htmlcontext = None
    else:
        htmlcontext = urlopen(args.url)
        bsObj = BeautifulSoup(htmlcontext, "html.parser")
        #for link in bsObj.findAll(args.tag):
        for link in bsObj.findAll('a'):
            if 'href' in link.attrs:
                print(link.attrs['href'])
