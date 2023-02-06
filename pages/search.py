from selenium.webdriver.support.ui import Select


class Search:
    dropdown_id = "searchDropdownBox"
    electronics_value = "search-alias=electronics-intl-ship"
    search_field_id = "twotabsearchtextbox"

    def __init__(self, driver, phrase):
        self.driver = driver
        self.phrase = phrase

    def get_category_dropdown(self):
        return Select(self.driver.find_element_by_id(self.dropdown_id))

    def change_to_electronics(self):
        self.get_category_dropdown().select_by_value(self.electronics_value)

    def get_search_field(self):
        return self.driver.find_element_by_id(self.search_field_id)

    def search(self):
        search_field = self.get_search_field()
        search_field.clear()
        search_field.send_keys(self.phrase)
        search_field.submit()
