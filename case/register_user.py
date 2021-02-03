import os
import unittest

import ddt

from common import base
from common.openExcel import OpenExcel
from page.page_register import Register_page
from time import sleep
# from database import Database

excel_object = OpenExcel((os.path.dirname(__file__) + '/测试数据.xlsx'), converters=None,
                         sheet_name='用户注册数据').get_dict()


# dbb = Database("ecshop", "168168", port=3307)


@ddt.ddt
class MySecondTestCase(unittest.TestCase):
    url = r'http://localhost:8080/ecshop/user.php?act=register'

    def setUp(self):
        self.driver = base.open_browser()
        self.rg = Register_page(self.driver)
        self.rg.open_url(self.url)

    def tearDown(self):
        self.driver.quit()

    def register(self, username, email, password, confirm, tel):
        self.rg.username_input(username)
        # sleep(5)
        self.rg.email_input(email)
        # sleep(5)
        self.rg.password_input(str(password))
        # sleep(5)
        self.rg.confirm_password(str(confirm))
        # sleep(5)
        self.rg.tel_input(str(tel))
        self.rg.click_submit()

    @ddt.data(*excel_object)
    def test_register_user(self, db):
        self.register(**db)


if __name__ == '__main__':
    unittest.main()
