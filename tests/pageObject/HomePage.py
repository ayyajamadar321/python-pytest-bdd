from selenium.webdriver.common.by import By

from .CheckBox import CheckBox
from .DropDown import DropDown


class Homepage:
    def __init__(self, driver):
        self.driver = driver

    dropdown_ele = (By.CSS_SELECTOR, "a[href*='dropdown']")
    checkbox_ele = (By.CSS_SELECTOR, "a[href*='check']")

    def get_drodwon(self):
        self.driver.find_element(*Homepage.dropdown_ele).click()
        obj_dropdown = DropDown(self.driver)
        return obj_dropdown

    def get_checkbox(self):
        self.driver.find_element(*Homepage.checkbox_ele).click()
        obj_checkbox = CheckBox(self.driver)
        return obj_checkbox
