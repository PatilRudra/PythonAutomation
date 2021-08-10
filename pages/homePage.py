from pages.basePage import BasePage
from pages.newCarPage import NewCarPage
from pages.carBasePage import CarBasePage

class HomePage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    #Locators
    _newCars = "//div[normalize-space()='NEW CARS']"
    _findNewCars = "//div[@id='root']//div[contains(text(),'Find New Cars')]"

    def moveToNewCars(self):
        self.moveToElement(self._newCars,"xpath")

    def clickFindNewCar(self):
        self.clickElement(self._findNewCars,"xpath")


    def goAndClickFindNewCar(self):
        self.moveToNewCars()
        self.clickFindNewCar()
        return NewCarPage(self.driver)