import os
import unittest
from time import sleep

import ddt
from selenium import webdriver

from common.database import Database
from common.openExcel import OpenExcel
from page.info_page import Info, info_url

# 1.实例化一个Database的对象
db = Database('ecshop_zj', password='root', port=3308)
# 2,准备执行的SQL语句
sql = 'select user_name from ecs_users'
# 3.执行SQL语句
print(db.read_one(sql))

data = OpenExcel(os.path.dirname(__file__) + "/测试数据.xlsx",
                 {'username': str,
                  'password': str,
                  'birthdayYear': str,
                  'birthdayMonth': str,
                  'birthdayDay': str,
                  'phone': str,
                  'old_password': str,
                  'new_password': str,
                  'comfirm_password': str,
                  },
                 "用户信息").get_dict()_dict()


@ddt.ddt
class InfoCase(unittest.TestCase):
    def setUp(self):
        # # #谷歌
        # # # 个人加载项地址
        user_data_dir = r"--user-data-dir=C:\Users\DELL\AppData\Local\Google\Chrome\User Data"
        # 实例化加载配置对象
        option = webdriver.ChromeOptions()

        # 给加载对象添加个人资料路径
        option.add_argument(user_data_dir)

        # 打开浏览器  使用个人加载项配置 ==> 必须要关闭所有的浏览器
        driver = webdriver.Chrome(options=option)
        driver.get(info_url)
        # 实例化一个page页面对象 (因为继承了base,所以要传driver)
        self.lp = Info(driver)
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # 打开谷歌浏览器
        # driver = open_browser()
        self.lp = Info(driver)
        # 调用get_url方法,传入login_url(在page页面保存)
        self.lp.open_url("http://localhost:8080/ecshop/")

        sleep(20)

    def teardown(self):
        self.lp.quit()

    def info(self,
             username,
             password,
             birthdayYear,
             birthdayMonth,
             birthdayDay,
             email,
             phone,
             old_password,
             new_password,
             comfirm_password):
        # 输入用户名 : junfu
        self.lp.input_username(username)
        # 输入密码 : 123456
        self.lp.input_password(password)
        # 点击登录
        self.lp.click_submit()
        sleep(5)
        # 点击 用户信息链接
        self.lp.click_a_userinfo()
        sleep(2)
        self.lp.sel_year(birthdayYear)
        self.lp.sel_month(birthdayMonth)
        self.lp.sel_day(birthdayDay)
        # sleep(1)
        # 清空email输入框
        self.lp.inp_c(self.lp.email_loc)
        self.lp.input_email(email)
        # sleep(1)
        # 清空phone输入框
        self.lp.inp_c(self.lp.extend_field5_loc)
        self.lp.input_phone(phone)
        # sleep(1)
        # 清空old_password输入框
        self.lp.inp_c(self.lp.old_password_loc)
        self.lp.input_old_password(old_password)
        # sleep(1)
        # 清空new_password输入框
        self.lp.inp_c(self.lp.new_password_loc)
        self.lp.input_new_password(new_password)
        # sleep(1)
        # 清空comfirm_password输入框
        self.lp.inp_c(self.lp.comfirm_password_loc)
        self.lp.input_comfirm_password(comfirm_password)
        # sleep(1)
        # 点击确认
        self.lp.btn_submit()
        sleep(5)
        # 获取跳转页面后
        self.lp.a_rest()

    @ddt.data(*data)
    def test_case_1(self, db):
        # pass
        self.info(**db)
        print(self.lp.a_rest())
        # 断言
        self.assertIn("请登录", self.lp.a_rest(), '修改失败')


if __name__ == '__main__':
    print(data)

    unittest.main()
