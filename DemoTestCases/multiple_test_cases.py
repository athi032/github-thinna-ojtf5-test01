'''
Created on Jan 14, 2022

@author: Admin
''' 
import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions 
from webdriver_manager.chrome import ChromeDriverManager 

class MultiTests(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=(ChromeDriverManager().install()))
                
    def tearDown(self):
        self.driver.close()
        
    def test_upload_file_in_python(self):
        driver = self.driver
         
        driver.get("https://www.w3schools.com/howto/howto_html_file_upload_button.asp")
        driver.maximize_window()
        
        self.assertIn("File Upload", driver.title)
        
        element = driver.find_element(By.ID,"myFile")
        element.send_keys("C:\\Users\\OneDrive\\Pictures\\blue ocean waves.jpeg")
        time.sleep(3)
        self.assertIn("blue ocean waves.jpeg", driver.find_element(By.ID,'myFile').get_attribute('value'))
        
    def test_iframe(self):  
        driver = self.driver
        
        driver.get("https://www.w3schools.com/html/html_iframe.asp") 
        
        self.assertIn("Iframe", driver.title)
        h1element = driver.find_element(By.CSS_SELECTOR,'#main > h1') 
        self.assertIn("HTML Iframe", h1element.text)
        
        driver.switch_to.frame(driver.find_element(By.XPATH, '//*[@id="main"]/div[3]/iframe'))
        h1element = driver.find_element(By.CSS_SELECTOR,'#main > h1') 
        self.assertIn("HTML Tutorial", h1element.text)
        
        linkElement=driver.find_element(By.CSS_SELECTOR,'#topnav > div > div > a:nth-child(5)')
        linkElement.click()          
        
        time.sleep(3)        
        wait = WebDriverWait(driver, 20)
        h1element = driver.find_element(By.CSS_SELECTOR,'#main > h1')
        wait.until(expected_conditions.visibility_of(h1element)) 
        self.assertIn("JavaScript Tutorial", h1element.text)
        
        driver.switch_to.default_content()
        
    def test_new_tab(self):  
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
        
        
    def test_popout_windows(self):  
        driver = self.driver
        
        driver.get("https://www.encodedna.com/javascript/demo/open-new-window-using-javascript-method.htm")
        driver.maximize_window()
        driver.execute_script("window.scrollTo(0, 500)")
        
        self.assertIn("Open a New Browser Window", driver.title)
                
        main_page = driver.current_window_handle
          
        new_windown_btn = driver.find_element(By.XPATH, '//*[@id="content"]/div[3]/p[2]/input[1]')  
        new_windown_btn.click()
        
        for handle in driver.window_handles:
            if handle != main_page:
                new_window = handle
                
                driver.switch_to.window(new_window)                
                self.assertIn("Open a New Window using JavaScript window.open()", driver.title)
                
                driver.get("http://www.google.com/")
                self.assertIn("Google", driver.title) 
                driver.switch_to.window(main_page)
                

        self.assertIn("Open a New Browser Window", driver.title)  

        
if __name__ == "__main__":
    unittest.main()