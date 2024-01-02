from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time 
from selenium.webdriver.common.keys import Keys


username = "username of the person that the bot will send the messeages"
messeageToSend = "messeage"
user_data_path = "C:\\Users\\User\\AppData\\Local\\Google\\Chrome\\User Data" #Change "User" with the local user name


options = webdriver.ChromeOptions()
options.add_argument("--user-data-dir={}".format(user_data_path))

service = Service(executable_path="chromedriver.exe")


driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.instagram.com/direct/inbox/")
wait = WebDriverWait(driver, 100)

time.sleep(5)

test = driver.find_elements(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div')
print(test)

for i in test:
    if username in i.text:
        time.sleep(3)
        i.click()
        time.sleep(3)
        path = '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]'
        keyd = driver.find_element(By.XPATH, path)
        
        keyd.send_keys(messeageToSend + Keys.ENTER)
        time.sleep(3)
        for j in range(3):
            keyd.send_keys(messeageToSend + Keys.ENTER)
            time.sleep(3)
        print("==============")
        break
exit()

contact = wait.until(expected_conditions.presence_of_all_elements_located((By.XPATH, contact_path)))
print(contact)
exit()

