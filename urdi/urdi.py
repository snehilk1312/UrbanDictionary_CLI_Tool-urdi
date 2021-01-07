#! /usr/bin/env python3

banner_art=''' _   _        _                     ____   _        _    _                                   
| | | | _ __ | |__    __ _  _ __   |  _ \ (_)  ___ | |_ (_)  ___   _ __    __ _  _ __  _   _ 
| | | || '__|| '_ \  / _` || '_ \  | | | || | / __|| __|| | / _ \ | '_ \  / _` || '__|| | | |
| |_| || |   | |_) || (_| || | | | | |_| || || (__ | |_ | || (_) || | | || (_| || |   | |_| |
 \___/ |_|   |_.__/  \__,_||_| |_| |____/ |_| \___| \__||_| \___/ |_| |_| \__,_||_|    \__, |
                                                                                       |___/ 
'''

print(banner_art)

from bs4 import BeautifulSoup
import requests
import re
import sys

term = sys.argv[1]
source_code = requests.get(f"https://www.urbandictionary.com/define.php?term={term}").text

soup = BeautifulSoup(source_code, 'lxml')

# print(soup.prettify())
divs = soup.find_all('div', class_="meaning")


print(f"\nMeaning for word {term}:	", '\n')


count = 0
num = 1
for div in divs:
    if count != 1:
        a = str(div)
        a = re.sub("[\<].*?[\>]","", a)
        print(f"Definition number {num}:")
        print(a, end='\n'*3)
        num += 1
    count += 1

