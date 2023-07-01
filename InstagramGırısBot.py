from instaBilgileri import kullanıcıAdı,Sifre
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
# bu bazı bilgisayarlarda haa oluşturuyormuş o yüzden aldık her zaman almamıza gerek yok
from selenium.webdriver.chrome.options import Options 

options=Options()

options.add_experimental_option('excludeSwitches',['enable-logging'])

driver=webdriver.Chrome(executable_path=r"/Users/sevketugurel/Desktop/Python Kişisel Notlarım/chromedriver.exe",chrome_options=options)

url="https://www.instagram.com/"

driver.get(url)
time.sleep(2)

# burada 0.indeksi almazsak hata verir nereyi seçeceğini bilemez
ka=driver.find_elements(By.XPATH,"//*[@id='loginForm']/div/div[1]/div/label/input")[0]

time.sleep(2)
ka.send_keys(kullanıcıAdı)

sif=driver.find_elements(By.XPATH,"//*[@id='loginForm']/div/div[2]/div/label/input")[0]
time.sleep(2)
sif.send_keys(Sifre)
time.sleep(2)
sif.send_keys(Keys.ENTER)
time.sleep(4)
driver.maximize_window()






