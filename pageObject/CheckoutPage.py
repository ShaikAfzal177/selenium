from selenium.webdriver.common.by import By

from pageObject.ConfirmPage import ConfirmPage


class CheckOutPage:

    def __init__(self,driver):
        self.driver=driver

    cardTitle=(By.CSS_SELECTOR,".card-title a")
    cardFooter=(By.CSS_SELECTOR,".card-footer button")
    checkOut=(By.XPATH,"//a[@class='nav-link btn btn-primary']")
    confirmCheck=(By.XPATH, "//button[@class='btn btn-success']")

    def getCardTitle(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)

    def getCardFooter(self):
        return self.driver.find_elements(*CheckOutPage.cardFooter)

    def checkOutLink(self):
        return self.driver.find_element(*CheckOutPage.checkOut)

    def checkOutItems(self):
        self.driver.find_element(*CheckOutPage.confirmCheck).click()
        confirmPage=ConfirmPage(self.driver)
        return confirmPage
