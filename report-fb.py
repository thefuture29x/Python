from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import keyboard  # Make sure to install this package

def wait_for_keypress(key='s'):
    """Waits for a specific key press to continue."""
    print(f"Press '{key}' to continue...")
    while True:
        if keyboard.is_pressed(key):
            print("Key pressed! Continuing...")
            break
        time.sleep(0.1)  # Sleep briefly to avoid high CPU usage

def select_by_xpath(driver, xpath):
    """Selects an element by XPath."""
    try:
        element = driver.find_element(By.XPATH, xpath)
        return element
    except Exception as e:
        print(f"Error selecting element: {e}")
        return None

def open_new_tab():
    """Simulates Ctrl + N to open a new tab."""
    keyboard.press_and_release('ctrl+t')
    keyboard.write('https://www.facebook.com/damducduongduong')

def open_report_tab():
    
    print("open rp tab")
    time.sleep(3)
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[3]/div/div/div/div[2]/div/div/div').click()
    
    print("choose report ")
    time.sleep(3)
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[3]/div[2]').click()
    
    print("choose type report")
    time.sleep(3)
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div[1]/div/div/div/div[1]/div/div[1]/div/div/div/div/span').click()  
    
    print("choose detail type report")
    time.sleep(3)
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div[4]/div/div[2]/div/div/div/div[2]/div/div/div/div[1]/div/div[1]/div/div/div/div/span').click()
    
    print("click to send button")
    time.sleep(3)
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div[5]/div[2]/div/div/div/div').click()
    
    print("click to continue button")
    time.sleep(3)
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div').click()

    print("click to done button")
    time.sleep(3)
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div[5]/div[2]/div/div/div/div').click()
# Example usage
if __name__ == "__main__":
    # Set up the driver
    service = Service('C:/Users/Admin/Desktop/chromedriver-win64/chromedriver.exe')
    driver = webdriver.Chrome(service=service)

    # Navigate to Facebook
    driver.get("https://www.facebook.com/")

    # Allow time for the page to load
    time.sleep(2)

    # Find and fill the login fields
    email_xpath = '//*[@id="email"]'
    password_xpath = '//*[@id="pass"]'
    email_field = select_by_xpath(driver, email_xpath)
    password_field = select_by_xpath(driver, password_xpath)

    if email_field and password_field:
        email_field.send_keys("narayanjustin@hotmail.com")
        password_field.send_keys("Beobe141201")

        # Click the login button
        login_button = select_by_xpath(driver, '//*[@name="login"]')
        if login_button:
            login_button.click()

    # Wait for user to finish authentication
    time.sleep(45)
    wait_for_keypress('s')
    # open_new_tab()
    driver.get("https://www.facebook.com/damducduongduong")

    # Now you can continue with your automation
    print("Continuing with the next steps...")

    open_report_tab()

    time.sleep(10)
    # Close the browser when done
    driver.quit()
