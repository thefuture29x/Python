from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import keyboard
import sys
import pyautogui
import pandas as pd
import os

file_path = 'E:/Python/TiktokAcount.xlsx'

CHROME_DRIVER_PATH = 'E:/Python/chromedriver.exe'

FULL_PATH_BT_LOGIN = '/html/body/div[1]/div[2]/div[1]/div/div[3]/div[2]/button'

FULL_PATH_BT_LOGIN_TYPE = '/html/body/div[6]/div[3]/div/div/div[1]/div[1]/div/div/div/div[2]/div[2]'

FULL_PATH_BT_LOGIN_EMAIL_TEXT = '/html/body/div[6]/div[3]/div/div/div[1]/div[1]/div/form/div[1]/a'

FULL_PATH_IP_EMAIL = '/html/body/div[6]/div[3]/div/div/div[1]/div[1]/div[2]/form/div[1]/input'

FULL_PATH_IP_PASSWORD = '/html/body/div[6]/div[3]/div/div/div[1]/div[1]/div[2]/form/div[2]/div/input'

FULL_PATH_BT_LOGIN_SUBMIT = '/html/body/div[6]/div[3]/div/div/div[1]/div[1]/div[2]/form/button'

def read_email_list_from_excel(file_path):
    df = pd.read_excel(file_path)
    email_list = df.values.tolist()
    return email_list

def wait_for_keypress(key='q'):
    """Waits for a specific key press to continue."""
    print(f"Press '{key}' to stop...")
    while True:
        if keyboard.is_pressed(key):
            print(f"'{key}' key pressed! Stopping...")
            break
        time.sleep(0.1)  # Prevents high CPU usage

def setup_driver(chrome_path):
    """Sets up the Chrome driver."""
    try:
        service = Service(chrome_path)
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")  # Start browser maximized
        # options.add_argument("--headless")  # Uncomment to run headlessly
        driver = webdriver.Chrome(service=service, options=options)
        print("ChromeDriver initialized successfully.")
        return driver
    except Exception as e:
        print(f"Error initializing ChromeDriver: {e}")
        sys.exit(1)  # Exit if the driver setup fails

def handle_login_account(email, password):

    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    service = Service(CHROME_DRIVER_PATH)  # Change this to the path of your ChromeDriver
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get("https://www.tiktok.com/")
    print("Navigated to TikTok.")

    time.sleep(7)  # Wait for the page to load
    pyautogui.press('tab')
    pyautogui.press('enter')


    print(FULL_PATH_BT_LOGIN)
    driver.find_element(By.XPATH,FULL_PATH_BT_LOGIN).click()
    time.sleep(1)
    
    print(FULL_PATH_BT_LOGIN_TYPE)
    driver.find_element(By.XPATH,FULL_PATH_BT_LOGIN_TYPE).click()
    time.sleep(1)

    print(FULL_PATH_BT_LOGIN_EMAIL_TEXT) 
    driver.find_element(By.XPATH,FULL_PATH_BT_LOGIN_EMAIL_TEXT).click()
    time.sleep(1)

    print(FULL_PATH_IP_EMAIL) 
    driver.find_element(By.XPATH,FULL_PATH_IP_EMAIL).send_keys(email)
    time.sleep(1)

    print(FULL_PATH_IP_PASSWORD)
    driver.find_element(By.XPATH,FULL_PATH_IP_PASSWORD).send_keys(password)
    time.sleep(1)

    print(FULL_PATH_BT_LOGIN_SUBMIT)
    driver.find_element(By.XPATH,FULL_PATH_BT_LOGIN_SUBMIT).click()
    time.sleep(1)
    
def handle_login_multi_account(email_list):
    for email in email_list:
        handle_login_account(email[0], email[1].strip())

if __name__ == "__main__":
    # chrome_options = Options()
    # chrome_options.add_argument("--start-maximized")
    # chrome_options.add_argument('--disable-gpu')
    # chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument('--disable-dev-shm-usage')
    # chrome_options.add_argument("--headless")

    # service = Service(CHROME_DRIVER_PATH)  # Change this to the path of your ChromeDriver
    # driver = webdriver.Chrome(service=service, options=chrome_options)
    try:
        # driver.get("https://www.tiktok.com/")
        # print("Navigated to TikTok.")

        # time.sleep(7)  # Wait for the page to load
        # pyautogui.press('tab')
        # pyautogui.press('enter')

        email_list =  read_email_list_from_excel(file_path)
        
        handle_login_multi_account(email_list)

        # login_account() 

        # Wait for 'q' keypress to quit
        wait_for_keypress('q')

    finally:
        # driver.quit()
        print("Browser closed.")
