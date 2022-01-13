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
        driver.get("https://www.encodedna.com/javascript/demo/open-new-window-using-javascript-method.htm")
        
        self.assertIn("Open a New Browser Window", driver.title)
        #driver.maximize_window()
        
        main_page = driver.current_window_handle
        
        driver.find_element(By.XPATH, '//*[@id="content"]/div[3]/p[2]/input[1]').click()
        
        for handle in driver.window_handles:
            if handle != main_page:
                new_window = handle
                
                driver.switch_to.window(new_window)                
                self.assertIn("Open a New Window using JavaScript window.open()", driver.title)
                
                driver.get("http://www.google.com/")
                self.assertIn("Google", driver.title)
                
                driver.switch_to.window(main_page)
                self.assertIn("Open a New Browser Window", driver.title) 
                #driver.close() 
                
        driver.switch_to.window(main_page)
        
    def tearDown(self):
        self.driver.close()
        
if __name__ == "__main__":
    unittest.main()