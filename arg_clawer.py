from urllib.request import urlopen
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="enter the website url")
    parser.add_argument("-url", help="enter the link")
    args = parser.parse_args()
    htmlcontext = urlopen(args.url)
    print(htmlcontext.read())

