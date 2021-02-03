import unittest
from common import base, openExcel
from page.page_user_goods_search import UserGoodsSearch
import ddt
import os
from common.database import Database
from page.page_login import Login_page

excel = openExcel.OpenExcel(os.path.dirname(__file__) + '/测试数据.xlsx', converters=None, sheet_name='所有商品名称').get_dict()
excel2 = openExcel.OpenExcel(os.path.dirname(__file__) + '/测试数据.xlsx', converters=None,
                             sheet_name='商品名称模糊匹配关键字').get_dict()


@ddt.ddt
class EcUserGoodsSerachCase(unittest.TestCase):
    def setUp(self):
        self.driver = base.open_browser()
        self.driver.get(base.Base(self.driver).home_link)

    def tearDown(self):
        self.driver.quit()

    def steps(self, goodsname):
        """
    用例ID: 2
    用例标题: 验证未登录用户能成功输入商品信息并成功搜索到已添加商品
    预置条件: 使用谷歌浏览器打开至首页
    操作步骤:
        1.找到右上角搜索框,输入商品名称
        2.点击搜索
    预期结果:
        1.成功搜索到已添加商品
        :param goodsname:
        :return:
        """
        ugs = UserGoodsSearch(self.driver)
        ugs.input_goods_name(goodsname)
        ugs.click_serach_button()
        text = ugs.correct_text()
        self.assertEqual(goodsname, text, msg='查找的商品信息有误!')

    @ddt.data(*excel)
    def test_user_goods_search(self, db):
        self.steps(**db)

    def test_ifnotinput_serach(self):
        """
    用例ID: 3
    用例标题:验证用户不输入搜索条件,点击搜索后显示所有商品信息
    预置条件:使用谷歌浏览器进入首页
    执行步骤:
        1.不输入搜索条件,点击搜索按钮
    预期结果:
        1.成功显示所有商品信息
        :return:
        """
        ugs = UserGoodsSearch(self.driver)
        ugs.click_serach_button()
        try:
            count1 = ugs.count_current_goods()
            ugs.next_goods_page()
            count2 = ugs.count_current_goods()
            ugs.next_goods_page()
            count3 = ugs.count_current_goods()
            ugs.next_goods_page()
            coun4 = ugs.count_current_goods()
            allgoods = count1 + count2 + count3 + coun4
        except Exception as e:
            self.assertTrue(False, msg=f'没有找到这个商品{e}')
        else:
            db = Database(database='ecshop', password='168168')
            sql = 'select count(*) from ec_goods where is_on_sale=1'
            dabase_count = db.read_one(sql)['count(*)']
            self.assertTrue(int(allgoods) == dabase_count, msg='商品没有全部显示')

    def steps2(self, goodsname):
        """
    用例ID: 4
    用例标题: 验证已登录用户能成功输入商品信息并成功搜索到已添加商品
    预置条件: 使用谷歌浏览器打开至首页
    执行步骤:
        1.点击请登录
        2.输入账号
        3.输入密码
        4.点击登录
        5.找到右上角搜索框,输入商品名称
        6.点击搜索
    预期结果:
        1.成功搜索到已添加商品
        :return:
        """
        ugs = UserGoodsSearch(self.driver)
        lg = Login_page(self.driver)
        lg.get_url()
        lg.username('admin1234')
        lg.password('123456')
        lg.click_submit()
        ugs.input_goods_name(goodsname)
        ugs.click_serach_button()
        text = ugs.correct_text()
        self.assertEqual(goodsname, text, msg='查找的商品信息有误!')

    @ddt.data(*excel)
    def test_loginok_user(self, db2):
        self.steps2(**db2)

    @ddt.data(*excel2)
    def test_oksearch_keywords(self, db3):
        self.steps3(**db3)

    def steps3(self, goodsname):
        """
    用例ID: 5
    用例标题: 验证模糊搜索商品关键字,成功获取数据库中含关键字的在售商品
    预置条件: 使用谷歌浏览器进入商城首页
    执行步骤:
        1.输入商品关键字
        2.点击搜索
    预期结果:
        成功跳转到商品信息页面,并且显示含关键字的商品信息
        :return:
        """
        ugs = UserGoodsSearch(self.driver)
        ugs.input_goods_name(goodsname)
        ugs.click_serach_button()
        text = ugs.correct_text()
        self.assertIn(goodsname, text, msg='查找的商品信息有误!')


if __name__ == '__main__':
    unittest.main()
