import os
import unittest
import ddt
from selenium.webdriver.common.by import By
from common import base
from common.openExcel import OpenExcel
from page.page_login import Login_page
from page.page_refreshShopCar import user_login_url, Re_shopcar

# 获取登录用户数据
data2 = OpenExcel(os.path.dirname(__file__) + '/测试数据.xlsx',
                  converters={'password': str},
                  sheet_name='前台用户登录数据'
                  ).get_dict()

@ddt.ddt
class RefShopCar(unittest.TestCase):
    # def setUp(self, username, password):
    #     # 加载谷歌浏览器配置项
    #     # driver = open_browser_option()
    #
    #
    #     # self.lp = Re_shopcar(driver)
    #     # sleep(5)

    # def tearDown(self):
    #     self.lp.quit()
    # #
    # def refresh(self, num):
    #     # 点击立即后买
    #     self.lp.go_shopping()
    #     # 清空购买数量
    #     self.lp.reset_nums()
    #     # 输入购买数量
    #     self.lp.input_nums(num)
    #     # 刷新购物车
    #     self.lp.refresh_car()
    #     # 获取更新后购物车数量
    #     self.lp.get_values()
    #     # 断言
    #     self.assertTrue(num == self.lp.get_values(), msg='不相等')

    @ddt.data(*data2)
    def test_login(self, db):
        self.login_data(**db)

    def login_data(self, username, password, num):
        # 打开浏览器
        driver = base.open_browser()
        # 输入网址
        driver.get(user_login_url)
        # 实例化
        lps = Login_page(driver)
        # 输入用户名
        lps.username(username)
        # 输入密码
        lps.password(password)
        # 点击登录
        lps.click_submit()
        # 点击首页
        lps.find_element((By.CSS_SELECTOR, '#mainNav > div > ul > li:nth-child(1) > a')).click()
        # 点击商品
        lps.find_element((By.CSS_SELECTOR,
                          'body > div.index-body > div > div > div:nth-child(2) > div.goods-right > div > a:nth-child(1) > div.img-box > img')).click()
       # 点击立即购买
        lps.find_element(
            (By.CSS_SELECTOR, '#ECS_FORMBUY > ul > li.padd > table > tbody > tr > td.td1 > a > img')).click()

        # 实例化对象
        lp = Re_shopcar(driver)
        # 清空购物车数量
        lp.reset_nums()
        # 输入购物车数量
        lp.input_nums(num)
        # 刷新购物车
        lp.refresh_car()
        # 获取刷新后购物车数量
        lp.get_values()
        # 断言
        self.assertTrue(num == lp.get_values(), msg='数据没有更新成功')


if __name__ == '__main__':
    unittest.main()
