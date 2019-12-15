import pytest
import time
import json
import random 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class Platform():
  def setup_method_Chrome(self):
    self.driver = webdriver.Chrome()
    self.vars = {}

  def setup_method_Safari(self):
    self.driver = webdriver.Safari()
    self.vars = {}

  def setup_method_Firefox(self):
    self.driver = webdriver.Firefox()
    self.vars = {}

  def setup_method_Ie(self):
    self.driver = webdriver.Ie()
    self.vars = {}
  

class TestList(Platform):
  def __init__(self, class_a):
    self.driver = class_a.driver

  def teardown_method(self):
    time.sleep(3)
    self.driver.quit()

  def get_site(self):
    self.driver.get("https://vast-dawn-73245.herokuapp.com/")
    self.driver.set_window_size(1212, 777)
  
  def InputNumberRandom_FirstElement(self):
    i = 2
    while i <= 10:
        j = 1
        while j <= 10:
            self.driver.find_element(By.NAME, "firstNumber").click()
            self.driver.find_element(By.NAME, "firstNumber").send_keys(int(random.random()*10**i))
            self.driver.find_element(By.NAME, "secondNumber").click()
            self.driver.find_element(By.NAME, "secondNumber").send_keys("1")
            self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
            
            result = int(self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div').text)
            print result

            time.sleep(1)
            j = j + 1
        i = i + 1


  def InputNumberRandom_TwoElement(self):
    i = 2
    while i <= 10:
        j = 1
        while j <= 10:
            self.driver.find_element(By.NAME, "firstNumber").click()
            self.driver.find_element(By.NAME, "firstNumber").send_keys(int(random.random()*10**i))
            self.driver.find_element(By.NAME, "secondNumber").click()
            self.driver.find_element(By.NAME, "secondNumber").send_keys(int(random.random()*10**i))
            self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
            
            result = int(self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div').text)
            print result

            time.sleep(1)
            j = j + 1
        i = i + 1


  def InputCharacter(self):
    i = 2 ; k = 0
    while i <= 10:
        j = 1 ; Word = ["Hello", "ChineseWord" , "JapaneseWord" , "#"]
        while j <= 10:
            self.driver.find_element(By.NAME, "firstNumber").click()
            self.driver.find_element(By.NAME, "firstNumber").send_keys(int(random.random()*10**i))
            self.driver.find_element(By.NAME, "secondNumber").click()
            self.driver.find_element(By.NAME, "secondNumber").send_keys(Word[k])
            self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
            
            result = str(self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div').text)
            print result

            time.sleep(1)
            j = j + 1

            if i > 2 :
              k = 1
            elif i > 4 :
              k = 2
            elif i > 6 :
              k = 3

        i = i + 1


  def Load_Performance(self):
    navigationStart = int(self.driver.execute_script("return window.performance.timing.navigationStart"))
    responseStart = int(self.driver.execute_script("return window.performance.timing.responseStart"))
    domComplete = int(self.driver.execute_script("return window.performance.timing.domComplete"))
    
    backendPerformance_calc = responseStart - navigationStart
    frontendPerformance_calc = domComplete - responseStart
     
    print("Back End: %s ms" % backendPerformance_calc)
    print("Front End: %s ms" % frontendPerformance_calc)


  def PressLink(self):
    i = 1
    while i < 100: 
      self.driver.find_element(By.XPATH, "/html/body/div[1]/div/a/img").click()
      i = i + 1












