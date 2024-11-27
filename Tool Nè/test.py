from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

# File paths
file_path = 'E:/Python/TiktokAcount.xlsx'
CHROME_DRIVER_PATH = 'E:/Python/chromedriver.exe'

# XPaths
FULL_PATH_BT_LOGIN = '/html/body/div[1]/div[2]/div[1]/div/div[3]/div[2]/button'
FULL_PATH_BT_LOGIN_TYPE = '/html/body/div[6]/div[3]/div/div/div[1]/div[1]/div/div/div/div[2]/div[2]'
FULL_PATH_BT_LOGIN_EMAIL_TEXT = '/html/body/div[6]/div[3]/div/div/div[1]/div[1]/div/form/div[1]/a'
FULL_PATH_IP_EMAIL = '/html/body/div[6]/div[3]/div/div/div[1]/div[1]/div[2]/form/div[1]/input'
FULL_PATH_IP_PASSWORD = '/html/body/div[6]/div[3]/div/div/div[1]/div[1]/div[2]/form/div[2]/div/input'
FULL_PATH_BT_LOGIN_SUBMIT = '/html/body/div[6]/div[3]/div/div/div[1]/div[1]/div[2]/form/button'

# Function to read email list from an Excel file
def read_email_list_from_excel(file_path):
    df = pd.read_excel(file_path)
    return df.values.tolist()

# Function to set up a new Chrome browser instance
def setup_driver():
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    service = Service(CHROME_DRIVER_PATH)
    driver = webdriver.Chrome(service=service, options=options)
    return driver

# Function to log in to TikTok
def handle_login_account(email, password):
    driver = setup_driver()  # Create a new browser instance for each account
    try:
        driver.get("https://www.tiktok.com/")
        print(f"Navigated to TikTok for {email}.")

        time.sleep(10)  # Wait for the page to load

        driver.find_element(By.XPATH, FULL_PATH_BT_LOGIN).click()
        time.sleep(1)

        driver.find_element(By.XPATH, FULL_PATH_BT_LOGIN_TYPE).click()
        time.sleep(1)

        driver.find_element(By.XPATH, FULL_PATH_BT_LOGIN_EMAIL_TEXT).click()
        time.sleep(1)

        driver.find_element(By.XPATH, FULL_PATH_IP_EMAIL).send_keys(email)
        driver.find_element(By.XPATH, FULL_PATH_IP_PASSWORD).send_keys(password)
        driver.find_element(By.XPATH, FULL_PATH_BT_LOGIN_SUBMIT).click()

        print(f"Successfully logged in with {email}")
        # Keep the browser open after successful login
    except Exception as e:
        print(f"Error logging in with {email}: {e}")
        driver.quit()  # Close the browser only if there's an error

    return driver  # Return the driver to keep the browser open

# Function to handle multiple accounts
def handle_login_multi_account(email_list):
    drivers = []  # List to store driver instances
    for email, password in email_list:
        print(f"Starting login for {email}")
        driver = handle_login_account(email, password.strip())  # Open a new browser and log in
        if driver:  # If the login succeeds, keep the browser open
            drivers.append(driver)

    print(f"All accounts processed. {len(drivers)} browsers are open.")
    input("Press Enter to close all browsers...")  # Wait for user input before closing browsers

    # Close all browsers after user confirmation
    for driver in drivers:
        driver.quit()

# Main execution
if __name__ == "__main__":
    email_list = read_email_list_from_excel(file_path)
    handle_login_multi_account(email_list)
