import unittest
from common import base
from page.page_user_goods_display import PageUserGoodsDisplay, url

"""
用例ID: 1
用例标题: 验证点击商品名称,页面跳转成功且显示正确
预置条件: 使用谷歌浏览器进入商品首页
操作步骤:
    1.随机点击商品图片
预期结果:
    1.成功跳转到点击商品的信息页面,并且成功正确显示点击商品的信息
"""


class EcUserGoodsDisPlayTestCase(unittest.TestCase):
    def setUp(self):
        driver = base.open_browser()
        self.pugd = PageUserGoodsDisplay(driver)
        driver.get(url)

    def tearDown(self):
        self.pugd.quit()

    def test_display_check1(self):
        self.pugd.click_camera()
        text = self.pugd.get_okgoods_text()
        self.assertEqual("智能相机", text, msg='点击的商品和跳转后的商品信息不同')

    def test_display_check2(self):
        self.pugd.click_car()
        text = self.pugd.get_okgoods_text()
        self.assertEqual("平衡车", text, msg='点击的商品和跳转后的商品信息不同')

    def test_display_check3(self):
        self.pugd.click_fans()
        text = self.pugd.get_okgoods_text()
        self.assertEqual("随身风扇", text, msg='点击的商品和跳转后的商品信息不同')

    def test_display_check4(self):
        self.pugd.click_phone_protecter1()
        text = self.pugd.get_okgoods_text()
        self.assertEqual("炫彩翻页保护套", text, msg='点击的商品和跳转后的商品信息不同')

    def test_display_check5(self):
        self.pugd.click_phone_protecter2()
        text = self.pugd.get_okgoods_text()
        self.assertEqual("透明超薄软胶保护套", text, msg='点击的商品和跳转后的商品信息不同')

    def test_display_check6(self):
        self.pugd.click_sports_camera()
        text = self.pugd.get_okgoods_text()
        self.assertEqual("运动相机", text, msg='点击的商品和跳转后的商品信息不同')

    def test_display_check7(self):
        self.pugd.click_video()
        text = self.pugd.get_okgoods_text()
        self.assertEqual("视频", text, msg='点击的商品和跳转后的商品信息不同')

    def test_display_check8(self):
        self.pugd.click_photo_self()
        text = self.pugd.get_okgoods_text()
        self.assertEqual("自拍杆", text, msg='点击的商品和跳转后的商品信息不同')


if __name__ == '__main__':
    unittest.main()
