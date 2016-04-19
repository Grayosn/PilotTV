# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://172.16.2.9:8081/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("Account").clear()
        driver.find_element_by_id("Account").send_keys("grayson")
        driver.find_element_by_id("Password").clear()
        driver.find_element_by_id("Password").send_keys("123456")
        driver.find_element_by_id("btnSubmit").click()
        self.assertEqual(u"登入成功", self.close_alert_and_get_its_text())
        driver.find_element_by_css_selector("b").click()
        driver.find_element_by_id("customer_Link_M").click()
        time.sleep(1)
        driver.find_element_by_id("customer_Link").click()
        time.sleep(1)
        driver.find_element_by_id("store_Link_M").click()
        time.sleep(2)
        driver.find_element_by_id("store_Link").click()
        time.sleep(1)
        self.assertEqual(u"店家資料載入失敗", self.close_alert_and_get_its_text())
        time.sleep(1)
        driver.find_element_by_id("store_Link_M").click()
        time.sleep(1)
        driver.find_element_by_id("player_Link").click()
        time.sleep(1)
        driver.find_element_by_id("sales_Link_M").click()
        time.sleep(1)
        driver.find_element_by_id("sales_Link").click()
        time.sleep(1)
        Select(driver.find_element_by_id("searchWay")).select_by_visible_text(u"英語名稱")
        time.sleep(1)
        Select(driver.find_element_by_id("searchStatus")).select_by_visible_text(u"離職")
        time.sleep(1)
        Select(driver.find_element_by_id("searchStatus_All")).select_by_visible_text(u"離職")
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
