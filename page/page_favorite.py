# 导包
from time import sleep
from selenium.webdriver.common.by import By

# 从base包导入Base类
from common.base import Base, open_browser_option

# 定义登录地址
user_login_url = 'http://localhost:8080/ecshop/user.php'


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## 定义一个 购物车页面类

class Favorite(Base):
    # 定位元素
    btn_collect_loc = (By.CSS_SELECTOR, '#ECS_FORMBUY > ul > li.padd > table > tbody > tr > td.td2 > a')

    # 操作元素
    def click_collect(self):
      self.click_element(self.btn_collect_loc)



if __name__ == '__main__':
    driver = open_browser_option()
    driver.get(user_login_url)
    lp = Favorite(driver)
    # sleep(5)
    lp.click_collect()
    # lp.get_alter()
    # sleep(5)
    v=lp.get_alter()
    print(v)
    sleep(2)
    lp.quit()
