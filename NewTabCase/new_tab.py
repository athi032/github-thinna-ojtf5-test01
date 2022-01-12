'''
Created on Jan 11, 2022

@author: Admin
'''
from selenium import webdriver 

driver = webdriver.Chrome(executable_path="E:\\FSoft\\Selenium\\chromedriver_win32\\chromedriver.exe")
driver.get("http://www.google.com/") 
assert "Google" in driver.title

driver.execute_script("window.open('');") 
driver.switch_to.window(driver.window_handles[1])    
driver.get("http://www.youtube.com/")
assert "YouTube" in driver.title
driver.close()

driver.switch_to.window(driver.window_handles[0])
assert "Google" in driver.title
driver.close()