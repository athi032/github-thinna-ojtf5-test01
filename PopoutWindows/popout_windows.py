'''
Created on Jan 12, 2022

@author: Admin
'''
from selenium import webdriver
from selenium.webdriver.common.by import By 
  
driver = webdriver.Chrome(executable_path="E:\\FSoft\\Selenium\\chromedriver_win32\\chromedriver.exe")
  
driver.get('http://demo.guru99.com/popup.php')
driver.maximize_window()

main_page = driver.current_window_handle
 
driver.find_element(By.XPATH, "//*[contains(@href,'popup.php')]").click()
 

for handle in driver.window_handles:
    if handle != main_page:
        new_page = handle
        driver.switch_to.window(new_page)
        driver.find_element(By.NAME,'emailid').send_keys("gaurav.3n@gmail.com")
        driver.find_element(By.NAME,"btnLogin").click()
        driver.close()

driver.switch_to.window(main_page)
driver.quit()