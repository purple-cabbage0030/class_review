from selenium import webdriver
import time

driver = webdriver.Chrome("c:/driver/chromedriver")
driver.get("https://www.google.com/")

tag = driver.find_element_by_name("q")
tag.clear()

tag.send_keys("AI")
tag.submit()

time.sleep(5)
driver.quit()
