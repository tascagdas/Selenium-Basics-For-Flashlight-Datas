from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException


driver = webdriver.Chrome()

driver.get("http://flashlights.parametrek.com/index.html")

driver.maximize_window()

driver.quit()


