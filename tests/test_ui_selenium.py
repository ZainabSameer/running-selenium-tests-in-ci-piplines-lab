import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def setup_browser():
    """Configure browser differently for local vs CI (GitHub Actions)"""
    options = webdriver.ChromeOptions()
    if os.getenv("CI"):
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        return webdriver.Chrome(options=options)
    else:
        return webdriver.Chrome()

# Test 1
def test_successful_signup_shows_thank_you():
    driver = setup_browser()
    try:
        driver.get("http://localhost:8000/signup")
        driver.find_element(By.ID, "name").send_keys("Zainab")
        driver.find_element(By.ID, "email").send_keys("zainab@example.com")
        driver.find_element(By.TAG_NAME, "form").submit()
        time.sleep(1)  # adjust based on your app speed
        assert "Thanks for subscribing, Zainab!" in driver.page_source
    finally:
        driver.quit()

'''
# Test 2
def test_blank_password_prevents_submit():
    driver = setup_browser()
    try:
        driver.get("http://localhost:8000/signup")
        # TODO: Leave email blank
        # TODO: Submit form
        # TODO: Check form validation blocks submit
    finally:
        driver.quit()

# Test 3
def test_successful_signup_shows_thank_you():
    driver = setup_browser()
    try:
        driver.get("http://localhost:8000/signup")
        # TODO: Fill form with valid data
        # TODO: Submit
        # TODO: Check thank-you message with name
    finally:
        driver.quit()

# Test 4
def test_form_resets_after_submit():
    driver = setup_browser()
    try:
        driver.get("http://localhost:8000/signup")
        # TODO: Submit valid data
        # TODO: Confirm fields reset
    finally:
        driver.quit()
'''