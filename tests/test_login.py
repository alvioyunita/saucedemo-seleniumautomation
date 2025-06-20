from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_login_success(driver):
    login = LoginPage(driver)
    inventorypage = InventoryPage(driver)
    cartpage = CartPage(driver)
    checkoutpage = CheckoutPage(driver)

# TC-01 open website
    login.open()

# TC-02 login input blank data
    login.blanklogin()

# TC-03 login locked data
    login.lockedlogin("locked_out_user", "secret_sauce")

# TC-04 login valid data
    login.login("standard_user", "secret_sauce")

# TC-05 add backpack to cart
    inventorypage.add_backpack_to_cart()

# TC-06 remove backpack to cart
    inventorypage.remove_backpack_to_cart()

# TC-07 add light to cart
    inventorypage.add_light_to_cart()

# TC-08 add t-shirt to cart
    inventorypage.add_tshirt_to_cart()

# TC-09 remove and checkout
    cartpage.open()
    cartpage.remove_light_on_cart()
    cartpage.checkout_items()

# TC-10 input data checkout
    checkoutpage.open()
    checkoutpage.input_blank_data_checkout("", "", "")
    checkoutpage.input_valid_data_checkout("Alvio", "Yunita", "12345")

# TC-11 finish checkout
    checkoutpage.finish_checkout()