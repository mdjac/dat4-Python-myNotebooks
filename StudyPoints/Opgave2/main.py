''' 
1. Gå ind på boligportal.dk med selenium
2. Søg på københavn 
3. Hent alle annoncer fra de seneste 24 timer
4. Del annoncer op i kategorier fx. Lejlighed, rækkehus
5. Hvis en graf med antal annoncer ud fra de forskellige kategorier
6. Hvis en graf med gennemsnits lejepris/m2 ud fra de forskellige kategorier 
'''
from xml.etree.ElementTree import TreeBuilder
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import bs4
import requests

import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.use("pdf")



def boligportal_postings_newer_than_1_day(city):
    url = 'https://www.boligportal.dk/lejeboliger/' + city + '/'
    profile = webdriver.FirefoxProfile()
    profile.set_preference("general.useragent.override", "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:81.0) Gecko/20100101 Firefox/81.0")
    
    # headless is needed here because we do not have a GUI version of firefox
    options = Options()
    options.headless = True
    # driver = webdriver.Firefox(options=options, executable_path=r'/tmp/geckodriver')
    browser = webdriver.Firefox(options=options, executable_path=r'/tmp/geckodriver')
    
    
    
    # browser = webdriver.Firefox()
    browser.get(url)
    browser.implicitly_wait(2)

    accept_cookies_button = browser.find_element_by_xpath(r'//*[@id="coiPage-1"]/div[3]/div/button[3]')
    accept_cookies_button.click()

    keep_fetching = True
    result = []
    #While loop til at håndtere side skift.
    while keep_fetching:
        #Selve div hvor alle annoncerne findes
        outer_div = browser.find_element_by_xpath(r'//*[@id="app"]/div[2]/div[1]/div/div/div[2]/div[8]/div')
        #Liste af de enkelte annoncer
        inner_divs = outer_div.find_elements(By.CLASS_NAME, "temporaryFlexColumnClassName")

        #Kig i hver enkelt annonce og returner hvornår den er oprettet og link til selve annoncen.
        #Tilføjer til slut resultatet hvis annoncen er under 1 dag gammel.
        #Og stopper while loop hvis den støder på en annonce der er ældre.
        for x in inner_divs:
            href_ele = x.find_element(By.CLASS_NAME, "AdCardSrp__Link")
            lines = href_ele.text.splitlines()
            created = lines[-2]
            created_validation = ["timer","min","time","minut"]
            #check if created contains any string from created_validation
            #if so, append to result
            if any(x in created for x in created_validation):
                result.append([href_ele.get_attribute("href"), created])
            else:
                keep_fetching = False
                break

        #Går til næste side og kører igen
        if(keep_fetching == True):
            next_page_button = browser.find_element_by_xpath(r'//*[@id="app"]/div[2]/div[1]/div/div/div[2]/div[9]/div/div/button[2]')
            next_page_button.click()
    
    return result

def scrape_boligportal_posting(url):
    r = requests.get(url)
    r.raise_for_status()
    soup = bs4.BeautifulSoup(r.text, 'html.parser')

    #Main blocks, 0 = Detaljer om bolig, 1 = Detaljer om udlejning
    info_blocks = soup.select('.css-1l19u69')

    #Kategori
    category = info_blocks[0].select('.css-uzgi25')[0].getText()



    #Lejepris pr m2
    size = info_blocks[0].select('.css-uzgi25')[1].getText()
    #Only keep numbers infront of m2
    size = size.split(' ')[0]
    size = int(size)
    #Convert price to int
    monthly_price = info_blocks[1].select('.css-uzgi25')[2].getText()
    monthly_price = monthly_price.split(' ')[0]
    monthly_price = monthly_price.replace('.', '')
    #if , in monthly_price, remove it and the following characters
    if ',' in monthly_price:
        monthly_price = monthly_price.replace(',', '')
        monthly_price = monthly_price[:-3]
    monthly_price = int(monthly_price)

    #Double // means integer division
    price_per_m2 = monthly_price//size
    return [category,price_per_m2]


print("Main file executing!")
#Gets all new posts using selenium
new_postings = boligportal_postings_newer_than_1_day("københavn")
print("printing function output")
print(len(new_postings))

#Scrapes each post individually for details using beautifulSoup
#And adds it's m2 price to its category
result = {"Lejlighed":[],"Værelse":[],"Hus":[],"Rækkehus":[]}
for x in new_postings:
    _tmp = scrape_boligportal_posting(x[0])
    result[_tmp[0]].append(_tmp[1])


#Just for validation!
print(result)
#loop over key and value in result
for key, value in result.items():
    print(key)
    print(len(value))


#Graf med antal annoncer ud fra de forskellige kategorier
x_values = list(result.keys())
y_values = [len(x) for x in result.values()]
plt.bar(x_values, y_values)
for i in range(len(x_values)):
    plt.text(x_values[i], y_values[i], y_values[i], ha='center', va='bottom')
plt.savefig('Antal_boliger_pr_kategory.png', bbox_inches='tight')
plt.clf()


#Graf med pris pr m2 ud fra de forskellige kategorier
x_values = list(result.keys())
y_values = [sum(x)/len(x) if len(x) > 0 else 0 for x in result.values()]
plt.bar(x_values, y_values)
for i in range(len(x_values)):
    plt.text(x_values[i], y_values[i], y_values[i], ha='center', va='bottom')
plt.savefig('Gennemsnits_m2pris_pr_kategori.png', bbox_inches='tight')




