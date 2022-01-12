'''
Created on Jan 12, 2022

@author: Admin
'''
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By  

class TestPopoutWindow(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome("E:\\FSoft\\Selenium\\chromedriver_win32\\chromedriver.exe")

    def test_popout_window_in_python(self):
        driver = self.driver
        driver.get("http://demo.guru99.com/popup.php")
        driver.maximize_window()
        
        main_page = driver.current_window_handle
        
        driver.find_element(By.XPATH, "//*[contains(@href,'popup.php')]").click()
        
        for handle in driver.window_handles:
            if handle != main_page:
                new_page = handle
                driver.switch_to.window(new_page)
                driver.find_element(By.NAME,'emailid').send_keys("blue0703t@gmail.com")
                driver.find_element(By.NAME,"btnLogin").click()
                driver.close() 
                
        driver.switch_to.window(main_page)
        
    def tearDown(self):
        self.driver.close()
        
if __name__ == "__main__":
    unittest.main()