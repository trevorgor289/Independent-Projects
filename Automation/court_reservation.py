from selenium import webdriver
from selenium.common import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pyautogui import *




service = Service("/Users/fengchen/Development/chromedriver")
driver = webdriver.Chrome(service=service)
driver.maximize_window()


website = "https://kildairefarmsrs.playbypoint.com/"

driver.get(website)


time.sleep(5)
login = driver.find_element(By.XPATH, value='/html/body/div[1]/div/header/div[1]/div/div[1]/div[4]/a')
login.click()
time.sleep(10)

email = driver.find_element(By.XPATH, value='/html/body/div[1]/div[2]/div/div[2]/div/div[2]/form/div/div/div[1]/input')
email.send_keys("ggordon@kowaus.com")
time.sleep(5)

password = driver.find_element(By.XPATH, value="/html/body/div[1]/div[2]/div/div[2]/div/div[2]/form/div/div/div[2]/input")
password.send_keys("K6549722")
password.send_keys(Keys.ENTER)
time.sleep(5)

booknow = driver.find_element(By.XPATH, value="/html/body/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div/div/div[1]/div[2]/a/span")
booknow.click()
time.sleep(6)


selectdate = driver.find_element(By.XPATH, value="/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/div[2]/table/tbody/tr/td[2]/div[1]/div[1]/div/div/div/button[2]/div[1]")
selectdate.click()
time.sleep(6)

selecttype = driver.find_element(By.XPATH, value="/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/div[2]/table/tbody/tr/td[2]/div[1]/div[3]/div[2]/div/button[2]")
selecttype.click()
time.sleep(6)

selecttime = driver.find_element(By.XPATH, value="/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/div[2]/table/tbody/tr/td[2]/div[1]/div[4]/div[2]/button[6]")
selecttime.click()
time.sleep(6)

selectdetail = driver.find_element(By.XPATH, value="/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/div[2]/table/tbody/tr/td[2]/div[1]/div[5]/div/div/button[1]")
selectdetail.click()
time.sleep(6)

clicknext = driver.find_element(By.XPATH, value="/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/div[2]/table/tbody/tr/td[2]/div[2]/div[2]/button/span")
clicknext.click()
time.sleep(6)

selectgary = driver.find_element(By.XPATH, value="/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/div/div[2]/div[2]/table/tbody/tr/td[2]/div[2]/div/button/span")
selectgary.click()
time.sleep(6)


checkout = driver.find_element(By.XPATH, value="/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/div/div[3]/div[2]/table/tbody/tr/td[2]/div[1]/div[4]/div/div/div/button")
print('done')