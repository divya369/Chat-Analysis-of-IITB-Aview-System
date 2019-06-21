from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pandas as pd
import glob
from bs4 import BeautifulSoup

chromeOptions = Options()
chromeOptions.add_argument("--ignore-certificate-errors")
chromeOptions.add_argument("--incognito")

driver = webdriver.Chrome("/Users/divyapatel/Documents/IITB project/youtube chat web scraping/chromedriver", options=chromeOptions)

urls = []
with open("urls.txt",'r') as links:
    for url in links:
        url = url.rstrip('\n')
        urls.append(url)

for url in urls:
    driver.get(str(url))
    time.sleep(40)
    driver.find_element_by_tag_name('body').send_keys(Keys.NUMPAD9)
    time.sleep(5)
    driver.find_element_by_tag_name('body').send_keys('k')    # for video pause
    time.sleep(5)
    page_source_overview = driver.page_source
    iframe = driver.find_element_by_xpath("//iframe[@id='chatframe']")
    driver.switch_to.frame(iframe)
    chats = []
    innerHTML = driver.execute_script("return document.body.innerHTML")
    soup = BeautifulSoup(page_source_overview, 'lxml')
    title = soup.title.get_text()
    title = title[:-10]
    files = [f for f in glob.glob("*.txt")]
    for file in files:
        if file == title:
            continue
        else:
            with open(f"{title}.txt",'w') as fhand:
                for chat in driver.find_elements_by_css_selector('yt-live-chat-text-message-renderer'):
                #     author_name = list(chat.find_element_by_css_selector("#author-name").get_attribute('innerHTML').split('<'))
                    message = chat.find_element_by_css_selector("#message").get_attribute('innerHTML')
                    write_string = f"{message}\n"
                    fhand.write(write_string)
                #     author_name_encoded = author_name.encode('utf-8').strip()
                #     message_encoded = message.encode('utf-8').strip()
    driver.switch_to.default_content()
    driver.quit()
