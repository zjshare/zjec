import unittest
from page.page_admin_login_zzd import PageLogin, url
from common import base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from common.database import Database
from common.openExcel import OpenExcel
import os
import ddt
from time import sleep
import pymysql

dataE = OpenExcel(os.path.dirname(__file__) + '/测试数据.xlsx', sheet_name='添加新商品', converters=None).get_dict()

db = Database(database="ecshop", password="168168")


@ddt.ddt
class CheckAdminAddGoodsTestCase(unittest.TestCase):
    """
    用例ID : 6
    用例标题: 验证后台添加商品的通用信息栏正确性
    预置条件: 使用谷歌浏览器打开后台登录网页
    执行步骤:
        1.输入用户名
        2.输入密码
        3.点击登录
        4.点击商品管理
        5.点击添加新商品
    预期结果:
        成功登录,并正确显示添加商品的通用信息栏
    """

    @classmethod
    def setUpClass(cls):
        sql = "delete from ec_goods where goods_id>74"
        db.execute(sql)

    def stepsk(self, goods_name, goods_ID):
        driver = base.open_browser()
        pl = PageLogin(driver)
        driver.get(url)
        pl.login_admin()
        pl.input_username_admin()
        pl.input_password_admin()
        pl.click_submit()
        driver.switch_to.frame('menu-frame')
        pl.find_element((By.CSS_SELECTOR, 'li[data-key="01_goods_list"]')).click()  # 点击商品管理
        pl.find_element((By.CSS_SELECTOR, 'a[href="goods.php?act=add"]')).click()  # 点击添加新商品
        driver.switch_to.parent_frame()
        driver.switch_to.frame('main-frame')
        pl.find_element((By.CSS_SELECTOR, 'input[style="float:left;color:;"]')).send_keys(goods_name)  # 商品名称
        select1 = pl.find_element((By.CSS_SELECTOR, 'select[name="goods_name_style"]'))
        Select(select1).select_by_value('strong')  # 字体样式
        pl.find_element((By.CSS_SELECTOR, 'input[name="goods_sn"]')).send_keys(str(goods_ID))  # 商品货号
        select2 = pl.find_element((By.CSS_SELECTOR, 'select[onchange="hideCatDiv()"]'))
        Select(select2).select_by_value('18')
        # pl.find_element((By.CSS_SELECTOR, 'button[onclick="rapidCatAdd()"]')).click()  # 点击添加分类
        pl.find_element((By.CSS_SELECTOR, 'input[onclick="addOtherCat(this.parentNode)"]')).click()  # 点击扩展
        select3 = pl.find_element((By.CSS_SELECTOR, 'select[name="other_cat[]"]'))  # 定位
        Select(select3).select_by_value('19')
        select4 = pl.find_element((By.CSS_SELECTOR, 'select[onchange="hideBrandDiv()"]'))  # 定位商品品牌select标签
        Select(select4).select_by_value('15')  # 选择value=15的品牌(仓品)
        select5 = pl.find_element((By.CSS_SELECTOR, '#suppliers_id'))  # 定位选择供货商select标签
        Select(select5).select_by_value('2')  # 选择上海供货商
        pl.find_element((By.CSS_SELECTOR, 'input[onblur="priceSetted()"]')).clear()  # 清空本店售价文本
        pl.find_element((By.CSS_SELECTOR, 'input[onblur="priceSetted()"]')).send_keys('188')  # 本店售价188
        # pl.find_element((By.CSS_SELECTOR, '.rank_1')).clear()  # 清空 会员价格>注册用户
        # pl.find_element((By.CSS_SELECTOR, '.rank_1')).send_keys('888')  # 注册会员价格888
        pl.find_element((By.CSS_SELECTOR, 'input[name="volume_number[]"]')).send_keys('5')  # 优惠数量为5个
        pl.find_element((By.CSS_SELECTOR, 'input[name="volume_price[]"]')).send_keys('20')  # 当优惠梳理为5时,优惠20
        pl.find_element((By.CSS_SELECTOR, 'input[onclick="handlePromote(this.checked);"]')).click()  # 勾选促销价
        pl.find_element((By.CSS_SELECTOR, 'input[name="promote_price"]')).clear()  # 清空促销价文本
        pl.find_element((By.CSS_SELECTOR, 'input[name="promote_price"]')).send_keys('88')  # 促销价设置为88
        # 修改促销开始时间
        js = "document.getElementById('promote_start_date').value='2021-03-21'"
        driver.execute_script(js)
        # 修改促销结束时间
        js2 = "document.getElementById('promote_end_date').value='2021-04-21'"
        driver.execute_script(js2)
        #  上传商品图片
        pl.find_element((By.CSS_SELECTOR, 'input[name="goods_img"]')).send_keys(
            r'C:\3000soft\Red Spider\Language\logo.jpg')
        pl.find_element((By.CSS_SELECTOR, 'div.button-div>input[type="button"]')).click()  # 点击确定
        sleep(3)
        # with pymysql.connect(database='ecshop', port=3307, user='root', password='168168', charset='utf8',
        #                      host='127.0.0.1') as cnn:
        #     with cnn.cursor(cursor=pymysql.cursors.DictCursor) as cur:
        #         sql = "select goods_name from ec_goods where goods_name=%s"
        #         args = ["苹果"]
        #         tiao = cur.execute(sql, args)
        #         print(tiao)
        #         koko = cur.fetchall()
        #         print(koko)
        sql = "select goods_name from ec_goods where goods_name=%s"
        args = [goods_name]
        sqlcheck = db.read_one(sql, args)
        jkjk = sqlcheck['goods_name']
        sleep(5)
        self.assertTrue(goods_name == jkjk, msg='没有添加成功')
        driver.quit()

    @ddt.data(*dataE)
    def test_add_goods_new(self, dbk):
        self.stepsk(**dbk)


if __name__ == '__main__':
    unittest.main()
