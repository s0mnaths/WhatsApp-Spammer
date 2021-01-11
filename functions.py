import time
from selenium import webdriver

def spammer(name,message,count):
    driver = webdriver.Firefox()
    driver.get('https://web.whatsapp.com')
    driver.implicitly_wait(15)
    
    driver.find_element_by_css_selector("span[title='" + str(name) + "']").click()
    while count>0:
        driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(message)
        driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button').click()
        time.sleep(1) 
        count -= 1
    S='Spammed'+name
    return S
