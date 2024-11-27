import time
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui


def import_content(driver):
    # Chay danh sach nhung nguoi can gui email
    # for i in ["111","222","333"]:

    # Click vao nut tao moi email
    driver.find_element(By.XPATH, '/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div/div').click()
    time.sleep(1) 

    # Nhap email nguoi nhan
    driver.find_element(By.CLASS_NAME, "agP").send_keys("chiphongteo1123@gmail.com")
    time.sleep(1) 

    # Nhap tieu de email 
    driver.find_element(By.CLASS_NAME, "aoT").send_keys("[CY VIỆT NAM] [PHIẾU LƯƠNG THÁNG 12.2022]")
    time.sleep(1) 

    ActionChains(driver)\
        .key_down(Keys.CONTROL)\
        .key_down(Keys.SHIFT)\
        .send_keys('C')\
        .key_up(Keys.CONTROL)\
        .key_up(Keys.SHIFT)\
        .send_keys("chiphongteo1123@gmail.com")\
        .perform()
    time.sleep(1) 
    # Nhap noi dung email
    
    driver.find_element(By.CLASS_NAME, "editable").send_keys("Thân gửi Phong, \n" 
    +"\n"
    +"CY Việt Nam gửi tới em Phiếu lương của tháng 9 năm 2022. Em kiểm tra và phản hồi lại nếu có thông tin chưa chính xác, nếu trước 12:00 hôm nay công ty không nhận được phản hồi từ em nghĩa là các thông tin đã chính xác và công ty sẽ tiến hành chuyển lương.\n"
    +"\n"
    +"Trân trọng và cảm ơn, \n"
    +"Liên. \n"
    +"\n"
    +"\n"
    +"\n"
    ) 
    pyautogui.keyDown('win')
    pyautogui.keyDown('e')
    pyautogui.keyUp('win')
    pyautogui.keyUp('e')

    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('f')
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('f')

    pyautogui.typewrite('C:\\Users\\Administrator\\Pictures\\Bugs\\logoCYEmail.jpg', interval=.001)
    time.sleep(2)
    pyautogui.hotkey('down')
    pyautogui.hotkey('down')

    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('c')
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('c')

    pyautogui.keyDown('alt')
    pyautogui.keyDown('f4')
    pyautogui.keyUp('alt')
    pyautogui.keyUp('f4')

    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('v')
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('v')

    driver.find_element(By.CLASS_NAME, "editable").send_keys(""
    +"Ms. TRẦN BÍCH LIÊN ADMINISTRATOR |  CY Vietnam \n"
    +"Công ty TNHH Phát triển Phần mềm CY Việt Nam \n"
    +"Office  : +84 24-2248-9977\n"
    +"Mobile : +84 38-206-5699     Email : b.tranlien2810@cyglobal.net \n"
    +"SNS:  https://www.facebook.com/cysoftwarevietnam/ \n"
    +"Website: www.cyvietnam.com \n"
    +"Address : \n"
    +"      안양 본사 | 경기도 안양시 동안구 시민대로 248번길 25, 경기창조산업안양센터 504/505/506/406호 [14067] \n"
    +"      호남 지사 | 광주광역시 북구 추암로 249, 광주이노비즈센터 410호  [61003]\n"
    +"      Vietnam Corp. | 11th, Detech Tower, 8 Ton That Thuyet, My Dinh 2, Nam Tu Liem, Ha Noi, Vietnam"
    )
    time.sleep(1)

    driver.find_element(By.CLASS_NAME, "a1").click()
    time.sleep(3)
    pyautogui.typewrite('C:\\Users\\Administrator\\Pictures\\Bugs\\chitietdonhang1.png', .001) 
    pyautogui.press('enter') #Presses enter
    time.sleep(1) 


def login_to_email(driver):

    # Mo trang dang nhap email
    driver.get('https://accounts.google.com/v3/signin/identifier?dsh=S822373787%3A1671424546912433&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&rip=1&sacu=1&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&ifkv=AeAAQh4idrktHbdoCz8voyFjHT2SYfSA_RzWmfSGY2OVCfJepDOJ3hls_prF03eTmD4Wp-NVZh0BaQ')   # my own test test site with max anti-bot protection
    # Nhap email
    driver.find_element(By.ID, "identifierId").send_keys("teothiphong@gmail.com" + Keys.ENTER)
    time.sleep(5) 

    # Nhap password
    driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input').send_keys("phongTeo@#2910" + Keys.ENTER) 
    time.sleep(5) 


def send_mail(driver):
    # Click nut loai bo thong bao sau khi dang nhap thanh cong 
    if driver.find_element(By.CLASS_NAME, "bBe"):
        driver.find_element(By.CLASS_NAME, "bBe").click()

    # Click gui email
    driver.find_element(By.CLASS_NAME, "aoO").click()
    driver.implicitly_wait(5)


options = uc.ChromeOptions()

# version_main allows to specify your chrome version instead of following chrome global version
driver = uc.Chrome(options=options, version_main=108)

login_to_email(driver)

import_content(driver)

send_mail(driver)


time.sleep(10000)