import pytest

from pages.search import Search


class TestSearch:

    phrase = "Xiaomi"

    def test_home_page_title(self, setup, url):
        self.driver = setup
        self.driver.get(url)
        assert self.driver.title == "Amazon.com. Spend less. Smile more.", "Can't find Amazon page"
        self.driver.close()

    def test_search(self, setup, url):
        self.driver = setup
        self.driver.get(url)
        search = Search(self.driver, self.phrase)
        search.change_to_electronics()
        search.search()
        assert self.driver.title == "Amazon.com : Xiaomi", "Can't find Xiaomi in amazon page"
        self.driver.close()
