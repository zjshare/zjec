from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


def open_browser(name: str = "chrome"):
    if name == "chrome":
        driver = webdriver.Chrome()
    elif name == "ie":
        driver = webdriver.Ie()
    elif name == "firfox":
        driver = webdriver.Firefox()
    else:
        raise Exception("错误!")
    driver.maximize_window()
    return driver


def open_browser_option():
    """
    谷歌浏览器配置项
    :return:
    """
    user_data_dir = r"--user-data-dir=C:\Users\DELL\AppData\Local\Google\Chrome\User Data"
    # 实例化加载配置对象
    option = webdriver.ChromeOptions()
    # 给加载对象添加个人资料路径
    option.add_argument(user_data_dir)
    # 打开浏览器  使用个人加载项配置 ==> 必须要关闭所有的浏览器
    driver = webdriver.Chrome(options=option)
    driver.maximize_window()
    return driver


#   封装一个类 操作页面
class Base(object):
    home_link = "http://localhost:8080/ecshop/"

    def __init__(self, driver):
        self.driver = driver

    # 获取网址
    def open_url(self, url):
        self.driver.get(url)

    # 定位元素
    def find_element(self, locator, timeout=8):
        self.element = WebDriverWait(self.driver, timeout).until(
            ec.presence_of_element_located(locator))
        return self.element

    # 输入值
    def input_element(self, content: str, locator, timeout=8):
        self.find_element(locator, timeout).send_keys(content)

    # 点击
    def click_element(self, locator, timeout=8):
        self.find_element(locator, timeout).click()

    # 获取元素的文本
    def get_element_text(self, locator, timeout=8):
        return self.find_element(locator, timeout).text

    # 退出当前窗口
    def back_current_window(self):
        self.driver.close()

    # 退出所有关联窗口 并且关闭浏览器驱动
    def quit(self):
        self.driver.quit()

    # 定义一个下拉框方法
    def select(self, locator, text, timeout=10):
        select = self.find_element(locator, timeout)
        s = Select(select)
        s.select_by_visible_text(text)

    # 清空输入框
    def input_c(self, locator, timeout=10):
        self.find_element(locator, timeout).clear()

    # 获取弹窗
    def get_alter(self):
        # 获取弹窗
        alt = WebDriverWait(self.driver, 5).until(ec.alert_is_present())
        # 获取弹窗文本
        return alt.text

    # 统计标签个数,返回一个列表
    def count_element(self, locator, timeout=8):
        return WebDriverWait(self.driver, timeout).until(ec.presence_of_all_elements_located(locator))


if __name__ == '__main__':
    driver = open_browser("chrome")
    Base(driver).count_element((By.CSS_SELECTOR, ''))
    print(__file__)
