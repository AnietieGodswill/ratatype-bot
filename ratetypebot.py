from selenium import webdriver
import pyautogui
import pyperclip
import time
# pyperclip to paste the content from the clipboard
browser = webdriver.Chrome("path") #change this path to your chromedriver path
username = 'email@example.com'#enter your email
password = 'password' #enter your password
browser.get('https://www.ratatype.com/login/')
browser.find_element_by_id('email').send_keys(username)
browser.find_element_by_id('password').send_keys(password)
time.sleep(15)
browser.get("https://www.ratatype.com/typing-test/test/")
time.sleep(3)
pyautogui.typewrite(['enter'])
start = input("Press y to start \n")
while(True):
    if(start == 'y'):
        copypath = (browser.find_elements_by_class_name("mainTxt"))
        for post in copypath:
            print(post.text) 
        time.sleep(10)
        twrite = pyperclip.paste()
        inp_time = float(input("Enter time"))
        time.sleep(5)
        pyautogui.typewrite(twrite,float(inp_time))
        time.sleep(5)
        end = input("Press y to start again\n")
        if(end == 'y'):
            continue

        

