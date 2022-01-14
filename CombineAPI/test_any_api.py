'''
Created on Jan 14, 2022

@author: Admin
'''
import unittest
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestAnyAPI(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        
    def test_any_api_in_python(self):
        driver = self.driver
        
        driver.get("https://any-api.com/")
        driver.maximize_window()
        self.assertIn("AnyAPI", driver.title)
        
        leftNav = driver.find_elements(By.XPATH, '//*[@id="Gallery"]/div[3]/div[1]/div[2]/ul/li/a')
        
        for link in leftNav:
            time.sleep(0.5)
            wait = WebDriverWait(driver, 10)
            wait.until(expected_conditions.element_to_be_clickable(link))
            link.click()
            
            sc = requests.get(driver.current_url)
            assert sc.status_code == 200   
        
    def tearDown(self):
        self.driver.close()
        
if __name__ == "__main__":
    unittest.main()     