import pytest
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by  import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObject.CheckoutPage import CheckOutPage
from pageObject.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log=self.getLogger()
        homePage=HomePage(self.driver)
        checkOutPage=homePage.shopItems()
        log.info("getting all the card titles")
        cards=checkOutPage.getCardTitle()

        i=-1
        for card in cards:
            i=i+1
            cardText=card.text
            log.info(cardText)
            if cardText=="Blackberry":
                checkOutPage.getCardFooter()[i].click()

        checkOutPage.checkOutLink().click()
        confirmpage=checkOutPage.checkOutItems()
        log.info("entering country name as ind")
        self.driver.find_element(By.ID,"country").send_keys('ind')
        self.verifyLinkPresence("India")
        self.driver.find_element(By.LINK_TEXT, "India").click()
        time.sleep(7)
        # self.driver.find_element(By.XPATH,"//input[@name='name']").send_keys("afzal")
        # self.driver.find_element(By.XPATH,"//input[@name='email']").send_keys("hello@gmail.com")
        # self.driver.find_element(By.XPATH, "//input[@type='password']").send_keys("afzal123")
        # self.driver.find_element(By.ID,"exampleCheck1").click()
        # self.driver.find_element(By.ID,"inlineRadio1").click()
        # self.driver.find_element(By.XPATH,"//input[@type='submit']").click()
        # time.sleep(5)
        #
        #
        #
