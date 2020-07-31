from selenium.webdriver.common.by import By


class DropDown:
    def __init__(self, driver):
        self.driver = driver

    selectdrop_ele = (By.ID, "dropdown")

    def get_drop(self):
        return self.driver.find_element(*DropDown.selectdrop_ele)
