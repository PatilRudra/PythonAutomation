from utilities.logger import log
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class BasePage:

    def __init__(self,driver):
        self.driver = driver


    def getByType(self,locatorType):
        locatorType = locatorType.lower()
        if locatorType == 'id':
            return By.ID
        elif locatorType == 'name':
            return By.NAME
        elif locatorType == 'css':
            return By.CSS_SELECTOR
        elif locatorType == 'xpath':
            return By.XPATH
        elif locatorType == 'linktext':
            return By.LINK_TEXT
        elif locatorType == 'partiallinktext':
            return By.PARTIAL_LINK_TEXT
        elif locatorType == 'tagname':
            return By.TAG_NAME
        elif locatorType == 'class':
            return By.CLASS_NAME
        else:
            log().error("Locator type: {} is not correct".format(locatorType))



    def getElement(self,locator,locatorType):
        byTpe = self.getByType(locatorType)
        try:
            return self.driver.find_element(byTpe,locator)
        except:
            log().error("Typing values failed for the element: "+ locator +' '+locatorType)



    def clickElement(self,locator,locatorType):
        element = self.getElement(locator,locatorType)
        try :
            element.click()
        except:
            log().error("Element click failed for the element: "+ locator +' '+locatorType)

    def typeEnter(self,data,locator,locatorType):
        elmt = self.getElement(locator,locatorType)
        try:
            elmt.send_keys(data)
        except:
            log().error("Typing values failed for the element: "+ locator +' '+locatorType)

    def selectValue(self,visibleText,locator,locatorType):
        element = self.getElement(locator,locatorType)
        try:
            select = Select(element)
            select.select_by_visible_text(visibleText)
        except:
            log().error("Country selection failed")

    def moveToElement(self,locator,locatorType):
        element = self.getElement(locator,locatorType)
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()


    def getPageTitle(self):
        return self.driver.title
