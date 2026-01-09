# TASK 2: Automated Login Test
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup Chrome Driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

def test_login_flow():
    try:
        # Using a public demo site for testing
        driver.get("https://the-internet.herokuapp.com/login")
        
        # 1. Find Elements
        username_field = driver.find_element(By.ID, "username")
        password_field = driver.find_element(By.ID, "password")
        login_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

        # 2. Perform Action (Invalid Login)
        username_field.send_keys("wrongUser")
        password_field.send_keys("wrongPass")
        login_btn.click()
        time.sleep(1)

        # 3. Validation
        flash_message = driver.find_element(By.ID, "flash").text
        if "Your username is invalid!" in flash_message:
            print("✅ Test Passed: Invalid login detected correctly.")
        else:
            print("❌ Test Failed: Error message not found.")

    except Exception as e:
        print(f"Test Crashed: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    test_login_flow()