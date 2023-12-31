

from selenium.webdriver.common.by import By

from pageObject.CheckoutPage import CheckOutPage


class HomePage:
    def __init__(self, driver):
        self.driver= driver
    shop=(By.CSS_SELECTOR,"a[href*='shop']")
    name= (By.XPATH, "//input[@name='name']")
    email=(By.XPATH, "//input[@name='email']")
    check=(By.ID, "exampleCheck1")
    gender=(By.ID, "exampleFormControlSelect1")
    submit=(By.CSS_SELECTOR, "input[value='Submit']")
    successMessage=(By.CLASS_NAME, "alert-success")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkOutPage = CheckOutPage(self.driver)
        return  checkOutPage
    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getCheckBox(self):
        return self.driver.find_element(*HomePage.check)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def submitForm(self):
        return self.driver.find_element(*HomePage.submit)

    def getSuccessMessage(self):
        return self.driver.find_element(*HomePage.successMessage)



