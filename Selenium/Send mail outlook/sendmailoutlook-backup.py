import time
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui

listEmail = [
    ['Teo Thi Phong',"chiphongteo1123@gmail.com","chitietdonhang1.png"],
    ['Dinh Hai Phong',"dinhhaiphong2910@gmail.com","chitietdonhang1.png"]
]

listEmailReal = [
    ['Mạnh',"hi@manhne.com",""],
    ['Hiếu',"hieumm.work@gmail.com",""],
    ['Đăng',"haidang14727@gmail.com",""],
    ['Thuận',"thuan.nv035@gmail.com",""],
    ['Hậu',"haunv1503@gmail.com",""],
    ['Quyền',"nguyenquyen5120@gmail.com",""],
    ['Phong',"teothiphong@gmail.com",""],
    ['Minh',"minhtranconglis@gmail.com",""],
    ['Vũ',"thevu091193@gmail.com",""],
    ['Hiếu',"hieu.vm.0512@gmail.com",""],
    ['Sinh',"hadangsinh1911@gmail.com",""],
    ['Duy',"rudbich1999@gmail.com",""],
    ['Tâm Anh',"htamanh@gmail.com",""],
    ['Tiến',"hoangtrungtien99@gmail.com",""],
    ['Miên',"2502mien@gmail.com",""],
    ['Quang',"coolquanghuu@gmail.com",""],
    ['Khánh',"duongkhanh.uliskorean@gmail.com",""],
    ['Hiếu',"shivershady0@gmail.com",""],
    ['Thầy Luân',"Luann4099@gmail.com",""],
    ['Chị Hà',"nvietha6892@cyglobal.net",""],
    ['Thầy Vấn',"vanbkat14121102@gmail.com",""],
    ['Huyền',"nguyentranghuyen68@cyglobal.net",""]
]
emailLogin = 'teothiphong@gmail.com'
passLogin = ''
filePath = 'C:\\Users\\Administrator\\Pictures\\Bugs\\'
emailCC = 'chiphongteo1123@gmail.com'

def send_mail(driver,name,email,fileName,id):
    time.sleep(5)
    dockingInitVisiblePart = 'docking_InitVisiblePart_' + str(id)
    editorParent = 'editorParent_' + str(id+1)
    
    # Click vao nut tao moi email
    pyautogui.press('n')
    print("Click vao nut tao moi email")
    time.sleep(3)

    # Click nut CC
    driver.find_element(By.XPATH, '//*[@id="'+dockingInitVisiblePart+'"]/div/div[1]/div[1]/div/div[4]/button[1]').click()
    print("Click vao nut CC")
    time.sleep(1) 

    # Nhap email nguoi nhan
    driver.find_element(By.XPATH, '//*[@id="'+dockingInitVisiblePart+'"]/div/div[1]/div[1]/div/div[7]/div/div/div[1]').send_keys(email)
    print("Nhap email nguoi nhan la " + email)
    time.sleep(1) 

    # Nhap email CC
    driver.find_element(By.XPATH, '//*[@id="'+dockingInitVisiblePart+'"]/div/div[1]/div[1]/div/div[9]/div/div/div[1]').send_keys(emailCC)
    print("Nhap email CC la chiphongteo1123@gmail.com" )
    time.sleep(1)

    # Nhap tieu de email
    driver.find_element(By.XPATH, '//*[@id="'+dockingInitVisiblePart+'"]/div/div[1]/div[2]/div[2]/div/div/div/input').send_keys("[CY VIỆT NAM] [PHIẾU LƯƠNG THÁNG 12.2022]")
    print("Nhap tieu de email")
    time.sleep(1) 

    # Nhap noi dung email
    driver.find_element(By.XPATH, '//*[@id="'+editorParent+'"]/div').send_keys("Thân gửi "+name+", \n" 
    +"\n"
    +"CY Việt Nam gửi tới em Phiếu lương của tháng 12 năm 2022. Em kiểm tra và phản hồi lại nếu có thông tin chưa chính xác, nếu trước 12:00 hôm nay công ty không nhận được phản hồi từ em nghĩa là các thông tin đã chính xác và công ty sẽ tiến hành chuyển lương.\n"
    +"\n"
    +"Trân trọng và cảm ơn, \n"
    +"Liên. \n"
    +"\n"
    +"\n"
    )
    print("Nhap noi dung email")
    time.sleep(1)

    driver.find_element(By.XPATH, '//*[@id="'+dockingInitVisiblePart+'"]/div/div[3]/div[3]/div[2]/div/div/div/div/div[1]/div/div[1]/button/span/div/div').click()
    print("Click vao nut chon file dinh kem")
    time.sleep(1)

    pyautogui.hotkey('down')
    pyautogui.press('enter')
    print("Chon loai file dinh kem")
    time.sleep(3)

    pyautogui.typewrite(filePath + fileName, .001) 
    pyautogui.press('enter')
    print("Chon xong file dinh kem "+ fileName)
    time.sleep(3) 

    # Click gui email
    driver.find_element(By.XPATH, '//*[@id="'+dockingInitVisiblePart+'"]/div/div[3]/div[3]/div[1]/div/div/span/button[1]').click()
    print("Gui email cho "+ name +" thanh cong !")
    print("Tiep tuc gui mail sau 10s nua")
    time.sleep(5)



def login_to_email(driver):
    # Mo trang dang nhap email
    driver.get('https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1671623728&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3dd5f4f7c0-c32f-f7c8-7570-3bd4aac42bde&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015')
    time.sleep(1)

    # Nhap email
    driver.find_element(By.ID, "i0116").send_keys(emailLogin + Keys.ENTER)
    time.sleep(3) 

    # Nhap password
    driver.find_element(By.ID, 'i0118').send_keys(passLogin + Keys.ENTER) 
    time.sleep(10)

    # Duy tri dang nhap
    driver.find_element(By.ID, 'idSIButton9').click()
    time.sleep(3)

    print("Dang nhap thanh cong")
    time.sleep(3)




def main():
    try:
        options = uc.ChromeOptions()
        driver = uc.Chrome(options=options, version_main=108)
        login_to_email(driver)
        idAuto = 0;
        for i in listEmail:
            try:
                # Chay danh sach nhung nguoi can gui email
                send_mail(driver,i[0],i[1],i[2],idAuto)
                idAuto = idAuto + 1
            except:
                print("Error : Loi khong the gui mail cho " + i[1])
    except:
        print("Error : Khong the tiep tuc chay main()")
   



main()

time.sleep(1000000)