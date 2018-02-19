from urllib.request import urlopen
from urllib.error import HTTPError
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="enter the website url")
    parser.add_argument("-url", help="enter the link")
    args = parser.parse_args()
    try:
        htmlcontext = urlopen(args.url)
    except HTTPError as e:
        print("Error appears as followings: \n", e)
        htmlcontext = None
    else:
        print(htmlcontext.read())
    if htmlcontext == None:
        print("Somethings went wrong, please check the entered url.")
