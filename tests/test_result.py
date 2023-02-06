from pages.product_check import ProductCheck
from pages.search import Search
import pytest


class TestProds:
    phrase = "Xiaomi"

    def test_products_existing(self, setup, url):
        self.driver = setup
        self.driver.get(url)
        search = Search(self.driver, self.phrase)
        search.change_to_electronics()
        search.search()
        product_check = ProductCheck(self.driver, self.phrase)
        assert len(product_check.get_products()) > 0
        self.driver.close()

    def test_looking_for_product(self, setup, url):
        self.driver = setup
        self.driver.get(url)
        search = Search(self.driver, self.phrase)
        search.change_to_electronics()
        search.search()
        product_check = ProductCheck(self.driver, self.phrase)
        assert product_check.check_phrase()
        self.driver.close()
