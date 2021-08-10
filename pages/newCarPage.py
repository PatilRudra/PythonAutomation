from pages.basePage import BasePage
from pages.carBasePage import CarBasePage

class NewCarPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    #Locators
    _hynduai = "//a[@title='Hyundai']"
    _toyota = "//a[@title='Toyota']"
    _bMw = "//a[@title='BMW']"
    _honda = "//a[@title='Honda']"

    def clickHyundai(self):
        self.clickElement(self._hynduai,"xpath")
        return CarBasePage(self.driver)

    def clickHonda(self):
        self.clickElement(self._honda,"xpath")
        return CarBasePage(self.driver)

    def clickToyota(self):
        self.clickElement(self._toyota,"xpath")
        return CarBasePage(self.driver)

    def clickBMW(self):
        self.clickElement(self._bMw,"xpath")
        return CarBasePage(self.driver)