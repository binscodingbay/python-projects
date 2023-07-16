from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import os

USERNAME = os.environ.get('USERNAME')
PASSWORD = os.environ.get('PASSWORD')
SIMILAR_ACCOUNT = "chefsteps"
CHROME_DRIVER_PATH="C:\Development\chromedriver.exe"

# driver.get("https://www.instagram.com/")

class InstaFollower:
    def __init__(self,path):
        service = Service(path)
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)
        # self.driver.quit()

    def login(self):
        username=self.driver.find_element(By.NAME,"username")
        username.send_keys(USERNAME)
        password=self.driver.find_element(By.NAME,"password")
        password.send_keys(PASSWORD)
        password.send_keys(Keys.ENTER)
        time.sleep(5)

    def find_followers(self):
        # time.sleep(2)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/")
        time.sleep(10)
        following=self.driver.find_element(By.XPATH,'//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        following.click()
        time.sleep(2)
        modal = self.driver.find_element(By.XPATH,'/html/body/div[4]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR,"li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH,'/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()


bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
# time.sleep(2)
bot.find_followers()
# bot.follow()






# time.sleep(6000)
# driver.quit()

