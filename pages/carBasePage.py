from pages.basePage import BasePage

class CarBasePage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    #Locators
    _cars = "//div/div/div/a[1]/h3"
    _onwards = "//div/div/div/div/span[text()='onwards']"
    _prices = "//div/div/div/div[2]/span[1]"

    # def clickCar(self,carName):
    #     self.clickElement("","xpath")

    def getPriceOfCars(self):
        cars = self.driver.find_elements_by_xpath(self._cars)
        onwards = self.driver.find_elements_by_xpath(self._onwards)
        prices = self.driver.find_elements_by_xpath(self._prices)
        for i in range(len(onwards)):
            print(("car name: "+cars[i].text+" and price: "+prices[i].text).encode('utf8'))





