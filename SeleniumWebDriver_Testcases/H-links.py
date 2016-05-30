# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import unittest, time, re

class HLinks(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.base_url = "http://deanza.edu/"
        self.verificationErrors = []
    
    def test_h_links(self):
        link_title = {
            "High School Students" : "De Anza College :: Outreach :: High School Students", 
            "High Tech Center Training Unit" : "High Tech Center Training Unit Main Page",
            "Hindi Department" : "De Anza College :: Hindi :: Home",
            "History Department" : "De Anza College :: History :: Home",
            "Honors Program" : "De Anza College :: Honors Program :: Home",
            "HOPE - De Anza" : "De Anza College :: Hope-De Anza :: Home",
            "Housing" : "De Anza College :: De Anza College Housing :: Home",
            "Humanities Department" : "De Anza College :: Humanities :: Home"
            }
        
        driver = self.driver
        driver.get(self.base_url + "directory/dir-az.html")

        for link in link_title:
            title = link_title[link]
            driver.find_element_by_link_text(link).click()
            try: self.assertEqual(title, driver.title)
            except AssertionError as e: self.verificationErrors.append(str(e))
            driver.back()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
