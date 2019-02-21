import webbrowser, sys, pyperclip ,string, os
import pyautogui
import time
import config
# 1 explorer nyitas
# 2 link nyitassal
ie = webbrowser.get(webbrowser.iexplore)
ie.open('https://myportal.connect.valeo.com/mobility/master/userportal/login.jsp')

#webbrowser.open()
time.sleep(1.5)
# 3 get OTP
get_otp_pic = 'F:/02_SOURCEs/EVO/System_/get_otp.PNG'
pyautogui.screenshot()
get_otp = pyautogui.locateCenterOnScreen(get_otp_pic)
#pyautogui.moveTo(get_otp_pic)
pyautogui.click(get_otp)
print(get_otp)