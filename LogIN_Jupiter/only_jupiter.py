import pyautogui
import webbrowser, sys, pyperclip ,string, os ,subprocess
#os.system("F:/02_SOURCEs/EVO/System_/dsNetworkConnect__Shortcut.lnk")
os.startfile('F:/02_SOURCEs/EVO/System_/dsNetworkConnect__Shortcut.lnk')
pyautogui.screenshot()
print('1')
pyautogui.locateOnScreen('F:/02_SOURCEs/EVO/System_/jupiter_link.PNG')
print('2')
#pyautogui.locateCenterOnScreen('F:/02_SOURCEs/EVO/System_/jupiter_link.PNG')
jupiter_link = pyautogui.locateCenterOnScreen('F:/02_SOURCEs/EVO/System_/jupiter_link.PNG')
print('3')
print(jupiter_link)
pyautogui.moveTo(jupiter_link)