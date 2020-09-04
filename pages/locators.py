from selenium.webdriver.common.by import By

class MainPageLocators():
	LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocators():
	LOGIN_FORM = (By.CSS_SELECTOR, 'form#login_form')
	REGISTER_FORM = (By.CSS_SELECTOR, 'form#register_form')

class ProductPageLocators():
	PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
	PRODUCT_PRICE = (By.CLASS_NAME, 'price_color')
	ADD_TO_BASKET = (By.CLASS_NAME, 'btn-add-to-basket')
	ADDED_PRODUCT_MSG = (By.CSS_SELECTOR, '.alertinner strong:nth-child(1)')
	ADDED_PRODUCT_COST = (By.CSS_SELECTOR, '.alertinner p strong')
