import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions

chrome_options = ChromeOptions()

driver = webdriver.Remote(
    command_executor="http://192.168.1.100:4444",
    options=chrome_options
)

try:
    driver.get("https://google.com")

    driver.find_element(
        By.NAME,
        value="q"
    ).send_keys("Selenium Grid Remote Hub")

    time.sleep(20)

finally:
    driver.quit()