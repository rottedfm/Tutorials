from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

def open_knowyourmeme(headless=False, wait_time=10):
    """Launches Firefox with Geckodriver and opens knowyourmeme.com."""
    options = Options()
    options.headless = headless  # Set to True if you don't want the browser to open visibly

    try:
        driver = webdriver.Firefox(options=options)
        driver.get("https://knowyourmeme.com/editorials/collections")
        print(f"Opened: {driver.title}")
        time.sleep(wait_time)  # Keep the browser open for a few seconds
    finally:
        driver.quit()


