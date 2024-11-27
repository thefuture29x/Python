from selenium import webdriver

# Specify the path to ChromeDriver
chromedriver_path = "P:\Selenium\chromedriver"

# Set up Chrome options (optional)
chrome_options = webdriver.ChromeOptions()
# You can add options like headless, incognito, etc.
# Example: chrome_options.add_argument("--headless")

# Initialize the Chrome driver
driver = webdriver.Chrome(executable_path=chromedriver_path, options=chrome_options)

# Navigate to a website
driver.get("https://www.youtube.com/watch?v=0FGUFK0UZnE")

# Perform actions on the website
# ...

# Close the browser when done
driver.quit()
