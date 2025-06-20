from selenium.webdriver.common.by import By
import time

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.zip_input = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.finish_button = (By.ID, "finish")

    def open(self):
        self.driver.get("https://www.saucedemo.com/checkout-step-one.html")

    def input_blank_data_checkout(self, firstname, lastname, zipcode):
        self.driver.find_element(*self.first_name_input).send_keys(firstname)
        self.driver.find_element(*self.last_name_input).send_keys(lastname)
        self.driver.find_element(*self.zip_input).send_keys(zipcode)
        self.driver.find_element(*self.continue_button).click()
        time.sleep(2)

    def input_valid_data_checkout(self, firstname, lastname, zipcode):
        self.driver.find_element(*self.first_name_input).send_keys(firstname)
        self.driver.find_element(*self.last_name_input).send_keys(lastname)
        self.driver.find_element(*self.zip_input).send_keys(zipcode)
        self.driver.find_element(*self.continue_button).click()
        time.sleep(2)
    
    def finish_checkout(self):
        self.driver.find_element(*self.finish_button).click()
        time.sleep(5)