import pytest
from pages.homePage import HomePage
from pages.newCarPage import NewCarPage
from utilities import readxl
from pages.carBasePage import CarBasePage

@pytest.mark.usefixtures("oneTimeSetup")
class Test_CarWale:

    @pytest.mark.parametrize("cars",readxl.getAlldata("Cars"))
    def test_getCarPrice(self,cars):
        hp = HomePage(self.driver)
        np = hp.goAndClickFindNewCar()
        if cars == ['honda'] :
            np.clickHonda().getPriceOfCars()
        if cars == ['hyndaui'] :
            np.clickHyundai().getPriceOfCars()
        if cars == ['BMW'] :
            np.clickBMW().getPriceOfCars()
        if cars == ['toyota'] :
            np.clickToyota().getPriceOfCars()


