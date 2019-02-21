from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re
import config
#INIT

chromedriver = 'D:/Projects/LOG/Python/chromedriver.exe'
browser = webdriver.Chrome(chromedriver)
#URL Megadasa
base_url = 'https://erl1-sv04053.vnet.valeo.com/login?from=%2Fjob%2FSWT%2Fjob%2FSWT_VW%2Fview%2FSWT_VW_Status%2F'

browser.get(base_url)

username = browser.find_element_by_xpath('//*[@id="j_username"]')
username.send_keys(config.POLARIN_USERNAME)
#password = browser.find_element_by_name('j_password')
password = browser.find_element_by_xpath('//*[@id="main-panel"]/div/form/table/tbody/tr[2]/td[2]/input')

password.send_keys(config.POLARIN_PASSWORD)

browser.find_element_by_xpath('//*[@id="yui-gen1-button"]').click()


time.sleep(3)

browser.find_element_by_xpath('//*[@id="swt_vw_baseplus_releasenightly_p220"]/header/h2/a').click()
time.sleep(3)
browser.find_element_by_xpath('//*[@id="main-panel"]/ul[3]/li[1]/a').click()
time.sleep(2)
browser.find_element_by_xpath('//*[@id="main-panel"]/ul/li/a[2]').click()

browser.find_element_by_xpath('//*[@id="tasks"]/div[9]/a[2]').click()
