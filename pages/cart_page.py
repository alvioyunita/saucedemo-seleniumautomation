from selenium.webdriver.common.by import By
import time

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.shopping_cart_button = (By.CLASS_NAME, "shopping_cart_link")
        self.remove_light_button = (By.ID, "remove-sauce-labs-bike-light")
        self.checkout_button = (By.ID, "checkout")

    def open(self):
        self.driver.get("https://www.saucedemo.com/cart.html")
        time.sleep(3)

    def remove_light_on_cart(self):
        self.driver.find_element(*self.remove_light_button).click()
        time.sleep(2)
    
    def checkout_items(self):
        self.driver.find_element(*self.checkout_button).click()
        time.sleep(2)    
