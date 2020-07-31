import time

import self as self

from .pageObject.HomePage import Homepage
from .utilities.base import BaseClass


class TestCheckbox(BaseClass):
    def test_checkbox(self):
        obj_homePage = Homepage(self.driver)
        obj_checkbox = obj_homePage.get_checkbox()
        time.sleep(3)
        ele_checkbox = obj_checkbox.get_box()
        for ele in ele_checkbox:
            if ele.text == "checkbox 2":
                ele.click()

        self.driver.get_screenshot_as_file("screen.png")

    print("Thank you for selecting check box")
