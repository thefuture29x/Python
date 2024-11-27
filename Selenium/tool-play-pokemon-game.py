import time
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui


def main():
    print("Run Main")
    options = uc.ChromeOptions()
    driver = uc.Chrome(options=options, version_main=108)
    driver.get('https://pokemon-game-by-vudt.netlify.app/?utm_source=zalo&utm_medium=zalo&utm_campaign=zalo')
    # Chon ma 4x4
    time.sleep(3)
    test = driver.find_element(By.XPATH,'//*[@id="app"]/div/div/button[1]').click()
   
    for i in range(1,16):
        for j in range(0,10):
            driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div['+str(i)+']/div[1]').click()
            print("Click ")


    time.sleep(60)


main()