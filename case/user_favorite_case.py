import os
import unittest
from time import sleep

import ddt
from selenium.webdriver.common.by import By

from common import base
from common.openExcel import OpenExcel
from page.page_favorite import user_login_url
from page.page_login import Login_page

# 获取登录用户数据
data2 = OpenExcel(os.path.dirname(__file__) + '/测试数据.xlsx', converters={'password': str}, sheet_name='收藏夹').get_dict()
print(data2)


#
@ddt.ddt
class FavoriteCase(unittest.TestCase):
    # def tearDown(self):
    #     self.lp.quit()

    def favorite(self, username, password):
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
        # 点击收藏
        lps.find_element((By.CSS_SELECTOR,
                          '#ECS_FORMBUY > ul > li.padd > table > tbody > tr > td.td2 > a')).click()
        # # 断言
        self.assertIn('收藏夹', base.Base(driver).get_alter())


    @ddt.data(*data2)
    def test_case_01(self, db):
        self.favorite(**db)


if __name__ == '__main__':
    unittest.main()
