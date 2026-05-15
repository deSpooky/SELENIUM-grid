import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def test_chrome_search():

    chrome_options = ChromeOptions()

    driver = webdriver.Remote(
        command_executor="http://localhost:4444",
        options=chrome_options
    )

    try:
        driver.get("https://google.com")

        search = driver.find_element(By.NAME, value="q")
        search.send_keys("Selenium Grid Chrome")

        time.sleep(10)

        assert "Google" in driver.title

    finally:
        driver.quit()


def test_firefox_search():

    firefox_options = FirefoxOptions()

    driver = webdriver.Remote(
        command_executor="http://localhost:4444",
        options=firefox_options
    )

    try:
        driver.get("https://google.com")

        search = driver.find_element(By.NAME, value="q")
        search.send_keys("Selenium Grid Firefox")

        time.sleep(10)

        assert "Google" in driver.title

    finally:
        driver.quit()