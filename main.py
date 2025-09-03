from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

link = 'https://www.imdb.com/'

driver = webdriver.Firefox()
driver.maximize_window()

driver.get(link)

menu = driver.find_element(By.XPATH, '//*[@id="imdbHeader-navDrawerOpen"]')
menu.click()

top_250_series = menu.find_element(By.XPATH, '/html/body/div[2]/nav/div/aside[1]/div/div[2]/div/div[2]/div[1]/span/div/div/ul/a[2]/span')
top_250_series.click()


