from common.base import Base
from selenium.webdriver.common.by import By


class Login_page(Base):
    username_element = (By.CSS_SELECTOR, "input[name='username']")
    password_element = (By.CSS_SELECTOR, "input[name='password']")
    url = 'http://localhost:8080/ecshop/user.php'
    click_submit_element = (By.CSS_SELECTOR, "input.us_Submit")
    successful_username_element = (By.CSS_SELECTOR, "font.f4_b")
    miss_login_element = (By.CSS_SELECTOR, 'a[href="user.php"]')

    def get_url(self):
        self.open_url(self.url)

    def username(self, username):
        self.input_element(username, self.username_element)

    def password(self, password):
        self.input_element(password, self.password_element)

    def click_submit(self):
        self.click_element(self.click_submit_element)

    def get_login_username(self):
        return self.get_element_text(self.successful_username_element)

    def miss_login(self):
        return self.get_element_text(self.miss_login_element)

    def check_login(self, username, password):
        self.username(username)
        self.password(password)
        self.click_submit()
        try:
            if username == self.get_login_username():
                print('成功')
            else:
                print("失败")
        except Exception as e:
            print("失败")
        self.driver.quit()
