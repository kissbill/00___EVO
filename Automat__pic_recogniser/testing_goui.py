import webbrowser, sys, pyperclip ,string, os
import pyautogui
import time



start_gomb = 'F:/02_SOURCEs/EVO/Proba/start.PNG'


pyautogui.screenshot()
#pyautogui.locateOnScreen(start_gomb)
start_gomb = pyautogui.locateCenterOnScreen(start_gomb)

pyautogui.moveTo(start_gomb)
pyautogui.click()