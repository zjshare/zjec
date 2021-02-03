import unittest
from page.page_login import Login_page
from common import base
from common.openExcel import OpenExcel
import ddt
import os

excel_object = OpenExcel((os.path.dirname(__file__) + '/测试数据.xlsx'), {'username': str, 'password': str},
                         sheet_name='用户登录合法数据')
excel_list = excel_object.get_list()
excel_object2 = OpenExcel((os.path.dirname(__file__) + '/测试数据.xlsx'), {'username': str, 'password': str},
                          sheet_name='用户登录不合法数据')
excel_list2 = excel_object2.get_list()


@ddt.ddt
class MyFirstTestCase(unittest.TestCase):
    def setUp(self):
        driver = base.open_browser()
        self.lp = Login_page(driver)
        self.lp.get_url()

    def tearDown(self):
        self.lp.quit()

    def login_case1(self, testing_name, testing_paswd):
        self.lp.username(testing_name)
        self.lp.password(testing_paswd)
        self.lp.click_submit()
        self.assertEqual(testing_name, self.lp.get_login_username(), msg='输入的用户名和跳转后左上角显示的用户名不一致')

    def login_case2(self, testing_name, testing_paswd):
        self.lp.username(testing_name)
        self.lp.password(testing_paswd)
        self.lp.click_submit()
        self.assertTrue(testing_name != self.lp.miss_login() or testing_name != self.lp.get_login_username(),
                        msg='登录成功,输入的用户名和跳转后左上角显示的用户名一致')

    @ddt.data(*excel_list)
    def test_case1(self, db):
        self.login_case1(*db)

    @ddt.data(*excel_list2)
    def test_case2(self, db):
        self.login_case2(*db)

        """
        用例ID:
        用例标题:验证合法数据登录成功
        前置条件:
            使用谷歌浏览器打开ecshop登录页面 已有用户名:admin123 密码:123456
        用例步骤:
            1.输入用户名
            2.输入密码
            3.点击登录
        预期结果:
            登录成功,且成功跳转到左上角显示的用户名和输入的一致
        """


if __name__ == '__main__':
    unittest.main()

"""
标题:验证非法数据登录
准备:准备非法数据
登录
预期结果: 无法登录
实际结果: 成功登录
提出bug
断言结果:用例不通过
"""
