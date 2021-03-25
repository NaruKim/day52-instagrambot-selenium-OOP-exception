from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from time import sleep

CHROME_DRIVER_PATH = "c:/development/chromedriver.exe"

INS_ID = ""
INS_PW = ""

class InstaFollwer:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
        self.following = []

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        sleep(2)
        username = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        password = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        username.send_keys(INS_ID)
        password.send_keys(INS_PW)
        password.send_keys(Keys.ENTER)
        sleep(4)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()

    def find_follower(self):
        self.driver.get("https://www.instagram.com/furumoo/")
        sleep(2)
        follower_btn = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        follower_btn.click()

        sleep(2)
        popup = self.driver.find_elements_by_class_name('sqdOP')
        self.following = popup[2:]
        self.following[0].send_keys(Keys.END)

    def follow(self):
        all_buttons = self.driver.find_elements_by_css_selector("li button")
        for i in all_buttons:
            try:
                i.click()
                sleep(1)
            except ElementClickInterceptedException:
                self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[1]').click()
            sleep(1)
