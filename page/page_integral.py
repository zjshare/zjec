# 导包
from time import sleep
from selenium.webdriver.common.by import By
import re
from common.database import Database

# 从base包导入Base类
from common.base import Base, open_browser_option

# 定义登录地址
integral_url = "http://localhost:8080/ecshop/user.php"

# 定义一个 积分页面类
class Integral(Base):
    # 定位元素
    text_loc=(By.CSS_SELECTOR,'[class="f_l"]')
    # 操作元素
    def get_text(self):
        text = self.find_element(self.text_loc).get_attribute('outerHTML')
        return re.findall("积分:(\d+)积分", text)
    #     print(self.find_element(self.text_loc).get_attribute('outerHTML'))
    #     return self.find_element(self.text_loc).get_attribute('outerHTML')


if __name__ == '__main__':

    driver= open_browser_option()
    driver.get(integral_url)
    sleep(2)
    lp =Integral(driver)
    a= lp.get_text()
    print(a)
    data = Database('ecshop_zj', password='root', port=3308)
    data_sql = data.read_one("select pay_points from ecs_users where user_name='a123456'")
    print( )

    # text = lp.find_element(lp.text_loc).get_attribute('outerHTML')
    # print(text)
    # print(re.findall("积分:(\d+)积分", text))
    # a=lp.get_text()
    # print(a)


