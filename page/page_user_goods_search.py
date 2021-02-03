from common import base
from selenium.webdriver.common.by import By


# 用户搜索商品的类
class UserGoodsSearch(base.Base):
    def input_goods_name(self, goods_name):
        self.find_element((By.CSS_SELECTOR, 'input#keyword')).send_keys(goods_name)

    def click_serach_button(self):
        self.find_element((By.CSS_SELECTOR, 'input[name="imageField"]')).click()

    def correct_text(self):
        return self.find_element((By.CSS_SELECTOR, '.goodsItem>p>a')).text

    def count_current_goods(self):
        return len(self.count_element((By.CSS_SELECTOR, 'div[style="border:none;"]>div')))

    def next_goods_page(self):
        self.find_element((By.CSS_SELECTOR, 'a.next')).click()


if __name__ == '__main__':
    driver = base.open_browser()
    driver.get(base.Base(driver).home_link)
    ugs = UserGoodsSearch(driver)
    # ugs.input_goods_name("平衡车")
    ugs.click_serach_button()
    # text = ugs.correct_text()
    # print(text)
    print(ugs.count_current_goods())
