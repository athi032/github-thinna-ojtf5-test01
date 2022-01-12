'''
Created on Jan 11, 2022

@author: Admin
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By  

driver = webdriver.Chrome(executable_path="E:\\FSoft\\Selenium\\chromedriver_win32\\chromedriver.exe")
driver.get("https://www.w3schools.com/html/html_iframe.asp")
assert "HTML Iframe" in driver.title 
driver.switch_to.frame(driver.find_element(By.XPATH, '//*[@id="main"]/div[3]/iframe'))  
assert "HTML Tutorial" in driver.find_element(By.CSS_SELECTOR,'#main > h1').text
linkElement = driver.find_element(By.CSS_SELECTOR,'#topnav > div > div > a:nth-child(5)')
linkElement.click()
assert "HTML Tutorial" not in driver.find_element(By.CSS_SELECTOR,'#main > h1').text 
driver.switch_to.default_content()

driver.close()