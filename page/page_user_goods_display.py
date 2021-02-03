from common import base
from selenium.webdriver.common.by import By
import re

url = 'http://localhost:8080/ecshop/index.php'


class PageUserGoodsDisplay(base.Base):
    # 智能相机
    img1 = (By.CSS_SELECTOR, 'img[src="images/201605/thumb_img/72_thumb_G_1462956048008.jpg"]')
    # 平衡车
    img2 = (By.CSS_SELECTOR, 'img[src="images/201605/thumb_img/69_thumb_G_1462955300971.jpg"]')
    # 炫彩翻页保护套
    img3 = (By.CSS_SELECTOR, 'img[src="images/201605/thumb_img/70_thumb_G_1462955414561.jpg"]')
    # 透明超薄软胶保护套
    img4 = (By.CSS_SELECTOR, 'img[src="images/201605/thumb_img/68_thumb_G_1462955204381.jpg"]')
    # 运动相机
    img5 = (By.CSS_SELECTOR, 'img[src="images/201605/thumb_img/64_thumb_G_1462952811633.jpg"]')
    # 自拍杆
    img6 = (By.CSS_SELECTOR, 'img[src="images/201605/thumb_img/63_thumb_G_1462953395609.jpg"]')
    # 随时风扇
    img7 = (By.CSS_SELECTOR, 'img[src="images/201605/thumb_img/62_thumb_G_1462952557730.jpg"]')
    # 视频
    img8 = (By.CSS_SELECTOR, 'img[src="images/201605/thumb_img/61_thumb_G_1462952376889.jpg"]')

    def click_camera(self):
        self.find_element(self.img1).click()

    def click_car(self):
        self.find_element(self.img2).click()

    def click_phone_protecter1(self):
        self.find_element(self.img3).click()

    def click_phone_protecter2(self):
        self.find_element(self.img4).click()

    def click_sports_camera(self):
        self.find_element(self.img5).click()

    def click_photo_self(self):
        self.find_element(self.img6).click()

    def click_fans(self):
        self.find_element(self.img7).click()

    def click_video(self):
        self.find_element(self.img8).click()

    def get_okgoods_text(self):
        return self.find_element((By.CSS_SELECTOR, '.goods_style_name')).text


if __name__ == '__main__':
    driver = base.open_browser()
    # driver.get(url)
    pugd = PageUserGoodsDisplay(driver)
    # pugd.click_car()
    # print(pugd.get_okgoods_text())
    list2 = pugd.__dir__()
    for i in list2:
        if 'img' in i:
            print(i)
