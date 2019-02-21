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

#OTP kod kimasolasa
x = get_otp[0]
y = get_otp[1]
x = x-80
time.sleep(1)
pyautogui.doubleClick(x,y)
time.sleep(0.5)
# 4 copy
pyautogui.keyDown('ctrl')
pyautogui.keyDown('c')
pyautogui.keyUp('c')
pyautogui.keyUp('ctrl')


#------------------------------------------------------------------------
# 5 jupter nyitas
os.startfile("F:/02_SOURCEs/EVO/System_/dsNetworkConnect__Shortcut.lnk")
time.sleep(1)
# 6 link beilesztes
jupiter_link_pic = 'F:/02_SOURCEs/EVO/System_/jupiter_link.PNG'
pyautogui.screenshot()
pyautogui.locateOnScreen(jupiter_link_pic)
jupiter_link = pyautogui.locateCenterOnScreen(jupiter_link_pic)
pyautogui.moveTo(jupiter_link)

x1 = jupiter_link[0]
y1 = jupiter_link[1]
x1 = x1 + 80
pyautogui.moveTo(x1, y1)
pyautogui.click()
time.sleep(0.5)
pyautogui.typewrite('https://europe.connect.valeo.com/EXT')
# 7 go
pyautogui.screenshot()
jupiter_go_pic = 'F:/02_SOURCEs/EVO/System_/jupiter_go.PNG'
pyautogui.locateOnScreen(jupiter_go_pic)
jupiter_go = pyautogui.locateCenterOnScreen(jupiter_go_pic)
pyautogui.moveTo(jupiter_go)
pyautogui.click()

# 8 user 
time.sleep(0.5)
jupiter_user_pic = 'F:/02_SOURCEs/EVO/System_/jupiter_user.PNG'
pyautogui.screenshot()
pyautogui.locateOnScreen(jupiter_user_pic)
jupiter_user = pyautogui.locateCenterOnScreen(jupiter_user_pic)
x2 = jupiter_link[0]
y2 = jupiter_link[1]
x2 = x2 + 80
pyautogui.moveTo(jupiter_user)
pyautogui.click()
pyautogui.typewrite(config.POLARIN_USERNAME)

#9 otp + pass
jupiter_pass_pic = 'F:/02_SOURCEs/EVO/System_/jupiter_pass.PNG'
pyautogui.locateOnScreen(jupiter_pass_pic)
jupiter_pass = pyautogui.locateCenterOnScreen(jupiter_pass_pic)
x3 = jupiter_link[0]
y3 = jupiter_link[1]
x3 = x3 + 80
pyautogui.moveTo(jupiter_pass)
pyautogui.click()
pyautogui.typewrite(pyperclip.paste() + config.POLARIN_PASSWORD)

# 9 login
jupiter_signIn_pic = 'F:/02_SOURCEs/EVO/System_/jupiter_signIn.PNG'
pyautogui.locateOnScreen(jupiter_signIn_pic)
jupiter_signIn = pyautogui.locateCenterOnScreen(jupiter_signIn_pic)
pyautogui.moveTo(jupiter_signIn)
pyautogui.click()