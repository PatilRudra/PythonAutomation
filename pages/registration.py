from pages.basePage import BasePage
from pages.carBasePage import TestPage

class Registration(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    #locators in the registartion Page
    _name = 'name'
    _phone = "//input[@name='phone']"
    _email = 'email'
    _city = 'city'
    _password = "//div[@id='load_box']//input[@name='password']"
    _username = "//div[@id='load_box']//input[@name='username']"
    _submitBtn = "//div[@id='load_box']//input[@value='Submit']"
    _country = "//select[@name='country']"
    _enterTestPage = "//div[@id='load_box']//a[@class='fancybox'][normalize-space()='ENTER TO THE TESTING WEBSITE']"



    #operations on registartion page
    def enterName(self, name):
        self.typeEnter(name,self._name,'name')

    def enterPhoneNumber(self,phoneNumber):
        self.typeEnter(phoneNumber,self._phone,'xpath')

    def enterEmail(self,email):
        self.typeEnter(email,self._email,'name')

    def enterCity(self,city):
        self.typeEnter(city,self._city,'name')

    def selectCountry(self,country):
        self.selectValue(country,self._country,'xpath')

    def enterUserName(self,userName):
        self.typeEnter(userName,self._username,'xpath')

    def enterPwd(self,password):
        self.typeEnter(password,self._password,'xpath')

    def clickSubmitBtn(self):
        self.clickElement(self._submitBtn,'xpath')

    def clickEnterTestPage(self):
        self.clickElement(self._enterTestPage,"xpath")
        return TestPage

    # complete registration
    def enterAllDetailsSubmit(self, name, phoneNumber, email, country, city, username, password):
        self.enterName(name)
        self.enterPhoneNumber(phoneNumber)
        self.enterEmail(email)
        self.selectCountry(country)
        self.enterCity(city)
        self.enterUserName(username)
        self.enterPwd(password)
        self.clickSubmitBtn()





