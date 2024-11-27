import time
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui

month = 3
year = 2023
monthString = ""

if month < 10:
    monthString = "0"+ str(month)
else:
    monthString = str(month)

prefixNameFile = "_PL_"+ str(monthString) +"."+ str(year)+".pdf"
emailLogin = 'b.tranlien2810@cyglobal.net'
passLogin = 'Tran28bich10lien@96'
filePath = 'D:\\COONG VIEEJC\\Barng luowng\\Phieesu thanh toasn tieefn luowng\\'+str(year)+'\\PL_'+str(monthString)+'.'+str(year)+'\\'
emailCC = 'nvietha6892@cyglobal.net'

listEmailTest = [
    ['Phong',"teothiphong@gmail.com","DDinh Hair Phong"],
    ['Phong',"dinhhaiphong2910@gmail.com","DDinh Hair Phong"]
]

listEmailTest2 = [
    ['Mạnh',"contact@manh.com.vn","Traanf Hoangf Manhj"],
    ['Hiếu',"hieumm.work@gmail.com","Mai Minh Hieeus"],
    ['Đăng',"haidang14727@gmail.com","Nguyeenx Hair DDawng"],
    ['Thuận',"thuan.nv035@gmail.com","Nguyeenx Vawn Thuaajn"],
    ['Hậu',"haunv1503@gmail.com","Nguyeenx Vawn Haauj"],
    ['Quyền',"nguyenquyen5120@gmail.com","Nguyeenx Huwux Quyeenf"],
    ['Minh',"minhtranconglis@gmail.com","Traanf Coong Minh"],
    ['Vũ',"thevu091193@gmail.com","DDinh Thees Vux"],
    ['Hiếu',"hieu.vm.0512@gmail.com","Vux Minh Hieeus"],
    ['Sinh',"hadangsinh1911@gmail.com","Haf DDawng Sinh"],
    ['Duy',"rudbich1999@gmail.com","Traafn Coong Duy"],
    ['Tâm Anh',"htamanh@gmail.com","Hoof Thij Taam Anh"],
    ['Tiến',"hoangtrungtien99@gmail.com","Hoangf Trung Tieens"],
    ['Miên',"2502mien@gmail.com","Nguyeenx Cao Mieen"],
    ['Quang',"HuuQuangHN2000@gmail.com","Nguyeenx Huwux Quang"],
    ['Khánh',"duongkhanh.uliskorean@gmail.com","Duowng Thij Khanhs"],
    ['Hiếu',"shivershady0@gmail.com","Traanf Xuaan Hieeus"],
    ['Thầy Luân',"Luann4099@gmail.com","Nguyeenx Thanhf Luaan"],
    ['Thầy Vấn',"vanbkat14121102@gmail.com","DDoafn Vawn Vaans"]
]

def send_mail(driver,name,email,fileName,id):
    time.sleep(25)
    dockingInitVisiblePart = 'docking_InitVisiblePart_' + str(id)
    editorParent = 'editorParent_' + str(id+1)
    
    # Click vao nut tao moi email
    pyautogui.press('n')
    print("Click vao nut tao moi email")
    time.sleep(10)

    # Click nut CC                   //*[@id="docking_InitVisiblePart_1"]/div/div[3]/div[1]/div/div[3]/div
    # driver.find_element(By.XPATH, '//*[@id="'+dockingInitVisiblePart+'"]/div/div[3]/div[1]/div/div[4]/button[1]').click()
    # print("Click vao nut CC")
    # time.sleep(2) 

    # Nhap email nguoi nhan        //*[@id="docking_InitVisiblePart_0"]/div/div[3]/div[1]/div/div[4]/div/div/div[2]
    driver.find_element(By.XPATH, '//*[@id="'+dockingInitVisiblePart+'"]/div/div[3]/div[1]/div/div[4]/div/div/div[2]').send_keys(email)
    print("Nhap email nguoi nhan la " + email)
    time.sleep(2) 

    # Nhap email CC                //*[@id="docking_InitVisiblePart_1"]/div/div[3]/div[1]/div/div[6]/div/div/div[2]
    driver.find_element(By.XPATH, '//*[@id="'+dockingInitVisiblePart+'"]/div/div[3]/div[1]/div/div[6]/div/div/div[2]').send_keys(emailCC)
    print("Nhap email CC la " + emailCC )
    time.sleep(2)

    # Nhap tieu de email           //*[@id="docking_InitVisiblePart_0"]/div/div[3]/div[2]/div[2]/div/div/div
    driver.find_element(By.XPATH, '//*[@id="'+dockingInitVisiblePart+'"]/div/div[3]/div[2]/div[2]/div/div/div/input').send_keys("[CY VIỆT NAM] [PHIẾU LƯƠNG THÁNG "+ monthString +"."+ str(year) +"]")
    print("Nhap tieu de email")
    time.sleep(2) 

    # Nhap noi dung email          //*[@id="editorParent_2"]/div/div[1]
    driver.find_element(By.XPATH, '//*[@id="'+editorParent+'"]/div/div[1]').send_keys("Thân gửi "+name+", \n" 
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
    time.sleep(10)
    #//*[@id="620_21_8"]/span/i[1]/span/i
    #//*[@id="620_21_14"]
    #//*[@id="620_21_8"]/span/i[1]/span/i
    #//*[@id="innerRibbonContainer"]/div[3]/div/div/div/div[1]
    #//*[@id="innerRibbonContainer"]/div[3]/div/div/div/div[1]
    driver.find_element(By.XPATH, '//*[@id="innerRibbonContainer"]/div[3]/div/div/div/div[1]/button').click()
    print("Click vao nut chon file dinh kem")
    time.sleep(8)

    pyautogui.hotkey('down')
    #pyautogui.hotkey('up')
    #pyautogui.hotkey('up')
    pyautogui.press('enter')
    print("Chon loai file dinh kem")
    time.sleep(10)

    pyautogui.typewrite(filePath + fileName, .01) 
    pyautogui.press('enter')
    print("Chon xong file dinh kem "+ fileName)
    time.sleep(15) 

    # Click gui email              //*[@id="docking_InitVisiblePart_0"]/div/div[2]/div[1]/div/span/button[1]
    driver.find_element(By.XPATH, '//*[@id="'+dockingInitVisiblePart+'"]/div/div[2]/div[1]/div/span/button[1]').click()
    print("Gui email cho "+ name +" thanh cong !")
    if (id+1) >= len(listEmailTest):
        print("Ket thuc chuong trinh")
        raise SystemExit
    print("Tiep tuc gui mail sau 10s nua")



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

def chay_danh_sach_mail(driver):
    idAuto = 0;
    for i in listEmailTest:
        try:
            # Chay danh sach nhung nguoi can gui email
            send_mail(driver,i[0],i[1],i[2] + prefixNameFile,idAuto)
            idAuto = idAuto + 1
        except:
            print("Error : Loi khong the gui mail cho " + i[1] + " !!!")
            raise SystemExit
import sys 
def main():
    options = uc.ChromeOptions()
    driver = uc.Chrome(options=options, version_main=110)
    login_to_email(driver)
    chay_danh_sach_mail(driver)



main()

#time.sleep(10000)