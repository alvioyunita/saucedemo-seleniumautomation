from selenium.webdriver.common.by import By
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def open(self):
        self.driver.get("https://www.saucedemo.com/")
        time.sleep(1)

    def blanklogin(self):
        self.driver.find_element(*self.login_button).click()
        time.sleep(1)
    
    def lockedlogin(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()
        time.sleep(1)


    def login(self, username, password):
        self.driver.find_element(*self.username_input).clear() 
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).clear() 
        self.driver.find_element(*self.password_input).send_keys(password)
        time.sleep(1)
        self.driver.find_element(*self.login_button).click()