class ProductCheck:
    products_xpath = '//*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]/div//*[@class="a-section a-spacing-none s-grid-status-badge-container s-expand-height s-padding-micro"]//parent::div/div[2]'

    def __init__(self, driver, phrase):
        self.driver = driver
        self.phrase = phrase

    def get_products(self) -> []:
        return self.driver.find_elements_by_xpath(self.products_xpath)

    def check_phrase(self) -> bool:
        prods = self.get_products()
        for i in prods:
            if self.phrase.lower() not in i.text.lower():
                return False
        return True
