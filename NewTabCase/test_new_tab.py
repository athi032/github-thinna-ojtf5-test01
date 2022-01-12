'''
Created on Jan 11, 2022

@author: Admin
'''

import unittest
from selenium import webdriver  

class TestNewTab(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="E:\\FSoft\\Selenium\\chromedriver_win32\\chromedriver.exe")
        
    def test_new_tab_in_python(self):
        driver = self.driver
        driver.get("http://www.google.com/")
        self.assertIn("Google", driver.title)
        
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
        driver.get("http://www.youtube.com/")
        self.assertIn("YouTube", driver.title)
        driver.close()
       
        driver.switch_to.window(driver.window_handles[0])
        self.assertIn("Google", driver.title)
        
    def tearDown(self):
        self.driver.close()
        
if __name__ == "__main__":
    unittest.main()