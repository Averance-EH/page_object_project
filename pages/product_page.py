from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

	def get_product_name_and_price(self):
		self.get_product_name()
		self.get_product_price()

	def get_product_name(self):
		product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
		return product_name

	def get_product_price(self):
		product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
		return product_price

	def add_product_to_basket(self):
		add_product = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
		add_product.click()


	def should_be_added_product(self, product_name):
		assert product_name in self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_MSG).text

	def should_be_right_price(self, product_price):
		assert product_price in self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_COST).text
