import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def setup_browser():
    """Configure browser differently for local vs CI (GitHub Actions)"""
    options = webdriver.ChromeOptions()

    if os.getenv("CI"):  # Running in GitHub Actions
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        return webdriver.Chrome(options=options)
    else:
        # Local (assumes chromedriver is on PATH)
        return webdriver.Chrome()

# Test 1
def test_invalid_email_shows_error_message():
    driver = setup_browser()
    try:
        print("Navigating to signup page...")
        driver.get("http://localhost:8000/signup")
        print(f"Page title: {driver.title}")
        print(f"Current URL: {driver.current_url}")
        
        # TODO: Enter valid name, invalid email
        driver.find_element(By.ID, "name").send_keys("zanoob")
        driver.find_element(By.ID,"email").send_keys("zainab")
        # TODO: Submit form
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        # TODO: Confirm success message does NOT appear
        # Wait briefly and confirm message stays empty
        time.sleep(2)  # Give time for any potential message
        message_text = driver.find_element(By.ID, "message").text
        print(f"Message text: '{message_text}'")
        assert message_text == ""

    except Exception as e:
        print(f"Error: {e}")
        print(f"Page source: {driver.page_source[:500]}...")
        raise
    finally:
        driver.quit()

# Test 2
def test_blank_password_prevents_submit():
    driver = setup_browser()
    try:
        driver.get("http://localhost:8000/signup")
        # TODO: Leave email blank
        driver.find_element(By.ID, "name").send_keys("John Doe")
        # TODO: Submit form
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        # Check that form validation prevents submission by verifying form is still visible
        form = driver.find_element(By.TAG_NAME, "form")
        assert form.is_displayed(), "Form should still be visible after invalid submit"    
    finally:
        driver.quit()

# Test 3
def test_successful_signup_shows_thank_you():
    driver = setup_browser()
    try:
        driver.get("http://localhost:8000/signup")
        # TODO: Fill form with valid data
        driver.find_element(By.ID, "name").send_keys("John Doe")
        driver.find_element(By.ID, "email").send_keys("john@example.com")
        # TODO: Submit
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        # TODO: Check thank-you message with name
        assert "Thanks for subscribing, John Doe!" in driver.find_element(By.ID, "message").text
    finally:
        driver.quit()

# Test 4
def test_form_resets_after_submit():
    driver = setup_browser()
    try:
        driver.get("http://localhost:8000/signup")
        # TODO: Submit valid data
        driver.find_element(By.ID, "name").send_keys("John Doe")
        driver.find_element(By.ID, "email").send_keys("john@example.com")
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        # TODO: Confirm fields reset
        assert driver.find_element(By.ID, "name").get_attribute("value") == ""
        assert driver.find_element(By.ID, "email").get_attribute("value") == ""
    finally:
        driver.quit()