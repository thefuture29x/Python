from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import keyboard
import sys
import pyautogui
import pandas as pd

file_path = 'E:/Python/Bot Tele/Hotmail.xlsx'

def read_email_list_from_excel(file_path):
    df = pd.read_excel(file_path)
    email_list = df.values.tolist()
    return email_list

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

def wait_for_keypress(key='q'):
    """Waits for a specific key press to continue."""
    print(f"Press '{key}' to stop...")
    while True:
        if keyboard.is_pressed(key):
            print(f"'{key}' key pressed! Stopping...")
            break
        time.sleep(0.1)  # Prevents high CPU usage

def open_new_tab():
    """Simulates Ctrl + N to open a new tab."""
    keyboard.press_and_release('ctrl+shift+n')
    time.sleep(2)

    email_list = read_email_list_from_excel(file_path)

    keyboard.write('https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=165&ct=1732089544&rver=7.5.2211.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26cobrandid%3dab0455a0-8d03-46b9-b18b-df2f57b9e44c%26RpsCsrfState%3daaccb550-12d6-1696-e947-e7052e1416e7&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=ab0455a0-8d03-46b9-b18b-df2f57b9e44c')
    keyboard.press_and_release('enter')
    print("email: ", email_list[0][0])
    print("passw: ", email_list[0][1])

    time.sleep(5)
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/form/div[2]/div/div/input').click()
    time.sleep(1)

    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/form/div[4]/div/div/div/div/button').send_keys(email_list[0][0])   
    time.sleep(1)
    
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/form/div[4]/div/div/div/div/button').click()
    time.sleep(1)

    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div[2]/div[2]/div/form/div[3]/div/div/input').send_keys(email_list[0][1])   
    time.sleep(1)

    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div[2]/div[2]/div/form/div[5]/div/div/div/div/button').click()
    time.sleep(1)

def open_youtube():
    """Opens YouTube in a new tab."""
    
    email_list = read_email_list_from_excel(file_path)
    driver2.get("https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=165&ct=1732089544&rver=7.5.2211.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26cobrandid%3dab0455a0-8d03-46b9-b18b-df2f57b9e44c%26RpsCsrfState%3daaccb550-12d6-1696-e947-e7052e1416e7&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=ab0455a0-8d03-46b9-b18b-df2f57b9e44c")

    print("email: ", email_list[0][0])
    print("passw: ", email_list[0][1])

    time.sleep(5)
    driver2.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/form/div[2]/div/div/input').click()
    time.sleep(1)

    driver2.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/form/div[2]/div/div/input').send_keys(email_list[0][0])   
    time.sleep(1)
    
    driver2.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/form/div[4]/div/div/div/div/button').click()
    time.sleep(1)

    driver2.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div[2]/div[2]/div/form/div[3]/div/div/input').send_keys(email_list[0][1])   
    time.sleep(1)

    driver2.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div[2]/div[2]/div/form/div[5]/div/div/div/div/button').click()
    time.sleep(1)

if __name__ == "__main__":
    CHROME_DRIVER_PATH = 'E:/Python/chromedriver.exe'
    CHROME_DRIVER_PATH2 = 'E:/Python/chromedriver2.exe'
    driver = setup_driver(CHROME_DRIVER_PATH)
    driver2 = setup_driver(CHROME_DRIVER_PATH2)

    try:
        driver.get("https://www.youtube.com/")
        print("Navigated to TikTok.")

        time.sleep(2)  # Wait for the page to load
        pyautogui.press('tab')
        pyautogui.press('enter')

        # open_form_sign_up() 

        # open_new_tab()
        open_youtube()

        # Wait for 'q' keypress to quit
        wait_for_keypress('q')

    finally:
        driver.quit()
        print("Browser closed.")
