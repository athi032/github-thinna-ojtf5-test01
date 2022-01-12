'''
Created on Jan 11, 2022

@author: Admin
'''
import unittest
from selenium import webdriver 
from selenium.webdriver.common.by import By

class TestUploadFile(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome("E:\\FSoft\\Selenium\\chromedriver_win32\\chromedriver.exe")
        
    def test_upload_file_in_python(self):
        driver = self.driver
        driver.get("https://www.w3schools.com/howto/howto_html_file_upload_button.asp")
        self.assertIn("File Upload", driver.title)
        
        element = driver.find_element(By.ID,"myFile")
        element.send_keys("E:\\FSoft\\EIV\\XmasTree.png")
        self.assertIn("XmasTree.png", driver.find_element(By.ID,'myFile').get_attribute('value'))
        
    def tearDown(self):
        self.driver.close()
        
if __name__ == "__main__":
    unittest.main()