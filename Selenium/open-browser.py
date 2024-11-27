from selenium import webdriver
import time

# Specify the path to ChromeDriver
chromedriver_path = "P:\Chrome Driver Test\chrome-win64\chrome_proxy.exe"

# Set up Chrome options (optional)
chrome_options = webdriver.ChromeOptions()
# You can add options like headless, incognito, etc.
# Example: chrome_options.add_argument("--headless")

# Initialize the Chrome driver
driver = webdriver.Chrome(options=chrome_options)

# Navigate to a website
driver.get("https://www.youtube.com/watch?v=9eobh6IMSuI")

# Perform actions on the website
# ...

# Close the browser when done
time.sleep(10)
driver.quit()
