from selenium.webdriver.common.by import By


class CheckBox:
    def __init__(self, driver):
        self.driver = driver

    clickcheck_ele = (By.ID, "checkboxes")

    def get_box(self):
        return self.driver.find_elements(*CheckBox.clickcheck_ele)