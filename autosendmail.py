from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import os
import pyautogui
import pandas as pd

month = 10
year = 2024
monthString = f"{month:02d}"

chromeDriverPath = 'E:/Python/chromedriver.exe'

prefixNameFile = "_PL_"+ str(monthString) +"."+ str(year)+".pdf"


# filePathExcel = 'E:/Python/CYStaff.xlsx'
# filePath = 'D:\\COONG VIEEJC\\Barng luowng\\Phieesu thanh toasn tieefn luowng\\'+str(year)+'\\PL_'+str(monthString)+'.'+str(year)+'\\'
emailCC = 'nvietha6892@cyglobal.net, '
emailCC2 = 'nhka@cyglobal.net, '

filePathExcel = 'E:/Python/CYStaff2.xlsx'
filePath = 'E:\\Funny Animals\\415492660_906614560828361_1122957060696912363_n.jpg'
emailCC3 = 'chiphongteo1123@gmail.com,teothiphong@gmail.com,'

fullPathCreateNewMailButton = '/html/body/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[1]/div/div/span/button[1]/span/span[1]/span'
# fullPathCreateNewMailButton = '/html/body/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[1]/div/div/span/button[1]'

fullPathCCButton = '/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div[1]/div/div/div[3]/div/div/div[3]/div[1]/div/div/div/div/div[3]/div[1]/div/div[2]/div/span/span[1]/div/button[1]'
# fullPathCCButton = '/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div[1]/div/div/div[3]/div/div/div[3]/div[1]/div/div/div[2]/div/div[3]/div[1]/div/div[2]/div/span/span[1]/div/button[1]'

fullPathCCEmail= '/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div[1]/div/div/div[3]/div/div/div[3]/div[1]/div/div/div/div/div[3]/div[1]/div/div[4]/div/span/span[2]/div/div[1]'
# fullPathCCEmail= '/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div[1]/div/div/div[3]/div/div/div[3]/div[1]/div/div/div[2]/div/div[3]/div[1]/div/div[4]/div/span/span[2]/div/div[1]'

fullPathSendTo = '/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div[1]/div/div/div[3]/div/div/div[3]/div[1]/div/div/div/div/div[3]/div[1]/div/div[2]/div/span/span[2]/div/div[1]'
# fullPathSendTo = '/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div[1]/div/div/div[3]/div/div/div[3]/div[1]/div/div/div[2]/div/div[3]/div[1]/div/div[2]/div/span/span[2]/div/div[1]'

fullPathTitle = '/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div[1]/div/div/div[3]/div/div/div[3]/div[1]/div/div/div/div/div[3]/div[2]/span/input'
# fullPathTitle = '/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div[1]/div/div/div[3]/div/div/div[3]/div[1]/div/div/div[2]/div/div[3]/div[2]/span/input'

fullPathContent = '/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div[1]/div/div/div[3]/div/div/div[3]/div[1]/div/div/div[2]/div/div[4]/div/div/div'
# fullPathContent = '/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div[1]/div/div/div[3]/div/div/div[3]/div[1]/div/div/div[2]/div/div[4]/div/div/div'

fullPathButtonAddFile = '/html/body/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div[4]/div/div/div/div[1]/button'
# fullPathButtonAddFile = '/html/body/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div[4]/div/div/div/div[1]/button'

fullPathButtonSendMail = '/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div[1]/div/div/div[3]/div/div/div[3]/div[1]/div/div/div[2]/div/div[2]/div[1]/button[1]'
# fullPathButtonSendMail = '/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div[1]/div/div/div[3]/div/div/div[3]/div[1]/div/div/div[2]/div/div[2]/div[1]/button[1]'

def read_email_list_from_excel(file_path):
    df = pd.read_excel(file_path)
    email_list = df.values.tolist()
    return email_list

def send_mail(driver,name,email,fileName,id,email_list):
    time.sleep(1)

    driver.find_element(By.XPATH, fullPathSendTo).send_keys(email)
    print("Nhap email nguoi nhan la " + email)
    time.sleep(1) 

    driver.find_element(By.XPATH, fullPathCCButton).click()
    print("Click vao nut CC")
    time.sleep(1) 

    driver.find_element(By.XPATH, fullPathCCEmail).send_keys(emailCC)
    # time.sleep(1)
    driver.find_element(By.XPATH, fullPathCCEmail).send_keys(emailCC2)
    # driver.find_element(By.XPATH, fullPathCCEmail).click()
    # pyautogui.typewrite(emailCC, .01)
    print("Nhap email CC la " + emailCC )
    time.sleep(1)

    driver.find_element(By.XPATH, fullPathTitle).send_keys("[CY VIỆT NAM] [PHIẾU LƯƠNG THÁNG "+ monthString +"."+ str(year) +"]")
    print("Nhap tieu de email")
    time.sleep(1) 

    driver.find_element(By.XPATH, fullPathContent).send_keys("Thân gửi "+name+", \n" 
    +"\n"
    +"CY Việt Nam xin gửi tới bạn Phiếu lương của tháng "+ monthString + " năm "+ str(year) +". Trong phiếu lương có ghi số lương còn lại của tháng 2."
    +" Bạn kiểm tra kỹ và nếu như có bất kì thắc mắc nào xin hãy gửi mail phản hồi trước 12:00 sáng ngày 5/4, nếu không chúng tôi sẽ "
    +"thực hiện chuyển lương theo như phiếu lương mà bạn đã nhận."
    +"\n"
    +"Trân trọng và cảm ơn, \n"
    +"Liên. \n"
    +"\n"
    +"\n"
    )

    print("Nhap noi dung email xong")

    time.sleep(2)
    driver.find_element(By.XPATH, fullPathButtonAddFile).click()
    print("Click vao nut chon file dinh kem")
    time.sleep(1)

    pyautogui.hotkey('down')
    pyautogui.press('enter')

    print("Chon loai file dinh kem")
    time.sleep(1)

    # pyautogui.typewrite(filePath + fileName, .01) 
    pyautogui.typewrite(filePath, .01) 

    pyautogui.press('enter')
    print("Chon xong file dinh kem "+ fileName)
    time.sleep(2) 

    # Click gui email
    driver.find_element(By.XPATH, fullPathButtonSendMail).click()
    print("Gui email cho "+ name +" thanh cong !")
    if (id+1) >= len(email_list):
        print("Ket thuc chuong trinh")
        raise SystemExit
    # print("Tiep tuc gui mail sau 10s nua")
    time.sleep(1)

def read_mail_list(driver, email_list):
    idAuto = 0
    for i in email_list:
        try:
            send_mail(driver, i[0], i[1], i[2] + prefixNameFile, idAuto, email_list)
            idAuto += 1
        except Exception as e:
            print(f"Error: Loi khong the gui mail cho {i[1]} !!!")
            raise SystemExit

def login_to_email(driver):
    # Mo trang dang nhap email
    driver.get('https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1671623728&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3dd5f4f7c0-c32f-f7c8-7570-3bd4aac42bde&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015')
    print('Mo trang dang nhap email')
    time.sleep(10)

    # Nhap email
    driver.find_element(By.ID, "i0116").send_keys(emailLogin + Keys.ENTER)
    print('Nhap email')
    time.sleep(10) 

    # Nhap password
    driver.find_element(By.ID, 'i0118').send_keys(passLogin + Keys.ENTER) 
    print('Nhap password')
    time.sleep(10)

    # Chon khong the mo ung dung authen 
    driver.find_element(By.ID, 'signInAnotherWay').click()
    print('Nhap password')
    time.sleep(10)  

    # Chon gui ma ve sdt 
    driver.find_element(By.XPATH, '//*[@id="idDiv_SAOTCS_Proofs"]/div[3]/div').click()
    print('Chon gui ma ve sdt')
    
     
    print('Nhan ma xac thuc o dien thoai va nhap ma')
    print('Thoi gian cho thao tac nhap ma xac thuc la 30s')
    time.sleep(30)

    # Duy tri dang nhap
    driver.find_element(By.ID, 'idSIButton9').click()
    print('Chon duy tri dang nhap')
    #time.sleep(3)

    print("Dang nhap thanh cong")
    time.sleep(3)

# def main():
#     # Kill any existing Chrome processes
#     os.system("taskkill /f /im chrome.exe")

    # chrome_options = Options()
#     chrome_options.add_argument("user-data-dir=C:/Users/teoth/AppData/Local/Google/Chrome/User Data")  # Change this to your Chrome user data path
#     chrome_options.add_argument("profile-directory=Profile 2")  # Change this to your specific profile directory
#     chrome_options.add_argument("--no-sandbox")
#     chrome_options.add_argument("--disable-dev-shm-usage")
#     chrome_options.add_argument("--remote-debugging-port=9222")
#     chrome_options.add_argument("--disable-extensions")
#     # chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
#     # chrome_options.add_experimental_option('useAutomationExtension', False)
#     # chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
#     # chrome_options.add_argument("--headless")  # Optional: Run Chrome in headless mode
#     chrome_options.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"  # Explicitly set the binary location

#     try:
#         service = Service(chromeDriverPath)  # Change this to the path of your ChromeDriver
#         driver = webdriver.Chrome(service=service, options=chrome_options)
#     except Exception as e:
#         print(f"Error initializing WebDriver: {e}")
#         exit(1)

#     try:
#         driver.get('https://outlook.live.com/mail/0/')
#     except Exception as e:
#         print(f"Error navigating to URL: {e}")
#         driver.quit()
#         exit(1)
    
    
    
#     time.sleep(30)

#     # driver.get('https://outlook.live.com/mail/0/')

#     # time.sleep(5)

#     driver.find_element(By.XPATH, fullPathCreateNewMailButton).click()
#     driver.find_element(By.XPATH, fullPathCreateNewMailButton).click()

#     print("Click vao nut tao moi email")
#     time.sleep(1)

#     email_list = read_email_list_from_excel(filePathExcel)
#     read_mail_list(driver, email_list)
import undetected_chromedriver as uc

def main():
    options = uc.ChromeOptions()
    driver = uc.Chrome(options=options, version_main=131)
    login_to_email(driver)

    # chay_danh_sach_mail(driver)
    email_list = read_email_list_from_excel(filePathExcel)
    read_mail_list(driver, email_list)


main()