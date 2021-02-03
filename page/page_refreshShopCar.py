# 导包
from time import sleep
from selenium.webdriver.common.by import By
# 从base包导入Base类
from common.base import Base, open_browser_option
#定义打开地址
user_login_url = 'http://localhost:8080/ecshop/user.php'

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 定义一个 购物车页面类
class Re_shopcar(Base):
    # 定位元素
    # 立即购买按钮
    shoppingnow_loc= (By.CSS_SELECTOR,"#ECS_FORMBUY > ul > li.padd > table > tbody > tr > td.td1 > a")
    # 购物车商品数量
    goodsNums_loc = (By.CSS_SELECTOR,'td[align="right"] input[type="text"]')
    # 清空购物车按钮
    clearCar_loc = (By.CSS_SELECTOR, "#formCart > table:nth-child(2) > tbody > tr > td:nth-child(2) > input:nth-child(1)")
    # 刷新购物车按钮
    refreshCar_loc = (By.CSS_SELECTOR, '#formCart > table:nth-child(2) > tbody > tr > td:nth-child(2) > input:nth-child(2)')
    # 结算按钮
    account_loc = (By.CSS_SELECTOR, "body > div:nth-child(7) > div.flowBox > table > tbody > tr > td:nth-child(2) > a > img")
    # 操作元素
    def go_shopping(self):
        self.click_element(self.shoppingnow_loc)
    # 修改购物数量
    def reset_nums(self):
       self.input_c(self.goodsNums_loc)
    # 输入购物车数量
    def input_nums(self,num):
        self.input_element(num,self.goodsNums_loc)
    # 点击更新购物车
    def refresh_car(self):
        self.click_element(self.refreshCar_loc)
    # 获取更新后购物车数量
    def get_values(self):
        return self.find_element(self.goodsNums_loc).get_attribute('value')




if __name__ == '__main__':
    driver = open_browser_option()
    driver.get(user_login_url)
    lp=Re_shopcar(driver)
    sleep(2)
    lp.go_shopping()
    sleep(5)
    lp.reset_nums()
    lp.input_nums(6)
    lp.refresh_car()
    sleep(10)
    v = lp.get_values()
    print(v)
    lp.quit()
