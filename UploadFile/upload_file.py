'''
Created on Jan 11, 2022

@author: Admin
'''
from selenium import webdriver 
from selenium.webdriver.common.by import By
 
driver = webdriver.Chrome(executable_path="E:\\FSoft\\Selenium\\chromedriver_win32\\chromedriver.exe")
driver.get("https://www.w3schools.com/howto/howto_html_file_upload_button.asp")
assert "File Upload" in driver.title
element = driver.find_element(By.ID,"myFile")
element.clear()
element.send_keys("E:\\FSoft\\EIV\\XmasTree.png")  
assert "XmasTree.png" in driver.find_element(By.ID,'myFile').get_attribute('value')
driver.close()