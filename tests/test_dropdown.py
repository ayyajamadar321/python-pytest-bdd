
import time

from tests.pageObject.HomePage import Homepage
from tests.utilities.base import BaseClass


class TestDrop(BaseClass):
    def test_drodwon(self):
        obj_homePage = Homepage(self.driver)
        obj_dropdown = obj_homePage.get_drodwon()
        time.sleep(3)
        sele_dropdown = obj_dropdown.get_drop()
        self.selectOptipn(obj_dropdown.get_drop(), "Option 2")
        assert "Option 2" in sele_dropdown.text

    print("Thank you for selecting Option 2")







# select = Select(sele_dropdown)
# select.select_by_visible_text("Option 2")
# assert "Option 2" in sele_dropdown.text