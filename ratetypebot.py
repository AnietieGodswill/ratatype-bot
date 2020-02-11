from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui
import pyperclip
import time
browser = webdriver.Chrome("C:/Users/Aaditya/Downloads/chromedriver")#change this path to your chromedriver path

print('RataType Bot (ratatype.com)')
print('Created By : dx4iot')
username = input("Enter Email: ")#enter your email
password = input("Enter Password: ") #enter your password
browser.get('https://www.ratatype.com/login/')
browser.find_element_by_id('email').send_keys(username)
browser.find_element_by_id('password').send_keys(password,Keys.RETURN)
time.sleep(10)
browser.get("https://www.ratatype.com/typing-test/test/")
while(True):
    browser.find_element_by_xpath("//*[contains(text(),'start typing now')]").click()
    start = input("Press s to start: ")
    if(start == 's'):
        copyPath = (browser.find_elements_by_class_name("mainTxt"))
        for post in copyPath:
            print(post.text)
            copyTo = post.text    
        pyperclip.copy(copyTo)
        time.sleep(10)
        twrite = pyperclip.paste()
        inp_time = float(input("Enter time: "))
        time.sleep(5)
        pyautogui.FAILSAFE=False
        pyautogui.typewrite(twrite,float(inp_time))
        time.sleep(5)
        browser.find_element_by_xpath('//*[@id="complete"]/div[2]/div/div[2]/div/button').click()
        end = input("continue? (y or n)")
        if(end == 'y'):
            continue
        

        



        

