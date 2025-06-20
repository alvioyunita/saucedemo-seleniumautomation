from selenium.webdriver.common.by import By
import time

class InventoryPage:

    def __init__(self, driver):
        self.driver = driver
        self.add_backpack_cart_button = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.add_light_cart_button = (By.ID, "add-to-cart-sauce-labs-bike-light")
        self.add_tshirt_cart_button = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        self.remove_cart_button = (By.ID, "remove-sauce-labs-backpack")  

    def open(self):
        self.driver.get("https://www.saucedemo.com/inventory.html")
        time.sleep(2)

    def scroll_down(self):
        # Scroll down the page
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_up(self):
        # Scroll up the page
        self.driver.execute_script("window.scrollTo(0, 0);")

    def add_backpack_to_cart(self):
        self.driver.find_element(*self.add_backpack_cart_button).click()
        self.scroll_down()
        self.scroll_up()
        time.sleep(2)

    def remove_backpack_to_cart(self):
        self.driver.find_element(*self.remove_cart_button).click()
        # time.sleep(2)
    
    def add_light_to_cart(self):
        self.driver.find_element(*self.add_light_cart_button).click()
        # time.sleep(2)   

    def add_tshirt_to_cart(self):
        self.driver.find_element(*self.add_tshirt_cart_button).click()
        # time.sleep(2)      

