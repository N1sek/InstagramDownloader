from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

post_url = input('Photo link:')
download_url = 'https://instadownloader.co/es/'

driver = webdriver.Chrome()

driver.get(download_url)
driver.find_element_by_id('link').send_keys(post_url)
driver.find_element_by_id('submit').click()
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Download file"))
    )
    element.click()
except:
    driver.quit()
else:
    time.sleep(3)
    driver.quit()



