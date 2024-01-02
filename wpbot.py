from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 

user_data_path = "C:\\Users\\User\\AppData\\Local\\Google\\Chrome\\User Data" #Change "User" with the local user name
target='"Target User to send messeages"'
messeagesToSend = "messeages"



options = webdriver.ChromeOptions()
options.add_argument("--user-data-dir={}".format(user_data_path))

service = Service(executable_path="chromedriver.exe")


driver = webdriver.Chrome(service=service, options=options)
driver.get("https://web.whatsapp.com")
time.sleep(8)
#driver.get("https://www.instagram.com/direct/inbox/")
wait = WebDriverWait(driver, 100)


contact_path = '//span[contains(@title,' + target + ')]'
contact = wait.until(expected_conditions.presence_of_all_elements_located((By.XPATH, contact_path)))

print(contact)
contact[0].click()
time.sleep(2)

path = '"//*[@id="main"]/div[2]/div/div[2]/div[3]"'
path = '"//*[@id="main"]/div[2]/div/div[2]/div[3]"'

messeages = wait.until(expected_conditions.presence_of_all_elements_located((By.XPATH, path)))

print("*"*100)
print(messeages)

print("*"*100)
for i in contact:
    print(contact)
    
print("*"*100)
contact[0].click()
message_box_path='//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div[2]/div[1]'
time.sleep(3)
message_box = wait.until(expected_conditions.presence_of_all_elements_located((By.XPATH, message_box_path)))
message_box[0].send_keys(messeagesToSend + Keys.ENTER)
for i in range(5): 
    message_box[0].send_keys(messeagesToSend + Keys.ENTER)
    time.sleep(2)
input()
