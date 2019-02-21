from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re
import config

#INIT

chromedriver = 'C:\\Users\\Hanokri2\\Documents\\Python\\chromedriver.exe'
browser = webdriver.Chrome(chromedriver)
#URL Megadasa
base_url = 'https://ecarpolarion.gplm.siemens.com/polarion/'
issue_url = 'https://ecarpolarion.gplm.siemens.com/polarion/#/project/VW_MEB_Inverter/workitems/issue?query=NOT%20HAS_VALUE:resolution'

browser.get(issue_url)


##username = selenium.find_element_by_id("username")
##password = selenium.find_element_by_id("password")
##<span title="[VW Request] Lifetime simulations Power Module">[VW Request] Lifetime simulations Power Module</span>
##<span title="Safety DC-link voltage: analog value cannot be set to 5V">Safety DC-link voltage: analog value cannot be set to 5V</span>


username = browser.find_element_by_name('org.apache.jetspeed.login.username')
username.send_keys(config.POLARIN_USERNAME)
password = browser.find_element_by_name('org.apache.jetspeed.login.password')
password.send_keys(config.POLARIN_PASSWORD)

browser.find_element_by_name("submit").click()
##<span style="white-space:nowrap;" title="VWMEB-Inv-60113 - GIT server not reachable from HIL-053"><img style="vertical-align:middle;border:0px;margin-right:2px;"
##src="/polarion/icons/default/enums/type_improvement.gif?buildId=20161208-2238"><span style="color:null;">VWMEB-Inv-60113</span></span>

time.sleep(25)

#EOL: A2L Parameter for P14_HVLV voltage needed

##issues = browser.find_elements_by_xpath('//span[@title="GIT server not reachable from HIL-053"]')
issues = browser.find_elements_by_xpath('//span[@style="white-space:nowrap;"]')
#print(issues[0].text)

num_issues = len(issues)
##
##print(num_issues)
##
for i in range(num_issues):
 print(issues[i].text)


#browser.close()
