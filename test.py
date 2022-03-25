from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
ser_obj=Service("C:\\browserdriver\chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)
driver.get("https://www.google.com/")
driver.find_element(by=By.ID,value="#input").send_keys("7673950025")
driver.find_element(by=By.CSS_SELECTOR,value="")
