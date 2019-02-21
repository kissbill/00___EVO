import webbrowser, sys, pyperclip ,string, os
import pyautogui
import time
import config
# 1 explorer nyitas
# 2 link nyitassal
ie = webbrowser.get(webbrowser.iexplore)
ie.open('https://myportal.connect.valeo.com/mobility/master/userportal/login.jsp')

webbrowser.close()