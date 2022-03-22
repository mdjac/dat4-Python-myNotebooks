import bs4
import os
import sys
import requests
import shutil
import re

def scrape_levels(inputUrls, depth=1):
    final_urls = [[]]
    final_urls[0] = inputUrls

    index = 1;
    while index <= depth:
        print("hi")
        index += 1

    return final_urls
url = "https://www.cphbusiness.dk/"

r = requests.get(url)
r.raise_for_status()
soup = bs4.BeautifulSoup(r.text, 'html.parser')

href_tags = soup.find_all(href=True)

http_or_https = re.compile(r"https?:.*$")

hrefs = [tag.get('href') for tag in href_tags]

print(type(hrefs))
urls = []

for href in hrefs:
    match = http_or_https.search(href)
    if match:
        urls.append(match.group())

print(urls)


result = scrape_levels(urls)
print(result)


