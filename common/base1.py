from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


def open_browser(browser_type: str = "谷歌"):
    if browser_type == "谷歌":
        driver = webdriver.Chrome()
    elif browser_type == "火狐":
        driver = webdriver.Firefox()
    elif browser_type == "Ie":
        driver = webdriver.Ie()
    else:
        raise TypeError("输入浏览器错误")
    driver.maximize_window()
    return driver


class Base(object):
    def __init__(self, driver):
        self.driver = driver

    def get_url(self, url):
        self.driver.get(url)

    def find_element(self, locator: tuple, timeout: int = 5):
        return WebDriverWait(self.driver, timeout).until(ec.presence_of_element_located(locator))

    def find_select(self, locator, timeout=5):
        return self.find_element(locator, timeout)

    def select_by_index(self, locator, index):
        Select(self.find_element(locator)).select_by_index(index)

    def select_by_visible_text(self, locator, visible_text):
        Select(self.find_element(locator)).select_by_visible_text(visible_text)

    def input_text(self, locator, text):
        self.find_element(locator).send_keys(text)

    def click_element(self, locator):
        self.find_element(locator).click()

    def find_alert(self, timeout: int = 5):
        return WebDriverWait(self.driver, timeout).until(ec.alert_is_present())

    def get_alert_text(self):
        return self.find_alert().text

    def clear_input_element(self,locaton):
        self.find_element(locaton).clear()
