from common.base import Base
from selenium.webdriver.common.by import By
from common.base import open_browser


class Register_page(Base):
    url = r'http://localhost:8080/ecshop/user.php?act=register'

    def open_url_register(self):
        self.driver.get(self.url)

    def username_input(self, username_data):
        self.find_element((By.CSS_SELECTOR, '#username')).send_keys(username_data)

    def email_input(self, email_data):
        self.find_element((By.CSS_SELECTOR, '#email')).send_keys(email_data)

    def password_input(self, password_data):
        self.find_element((By.CSS_SELECTOR, '#password1')).send_keys(password_data)

    def confirm_password(self, password_data):
        self.find_element((By.CSS_SELECTOR, '#conform_password')).send_keys(password_data)

    def tel_input(self, tel):
        self.find_element((By.CSS_SELECTOR, 'input[name="extend_field5"]')).send_keys(tel)

    def click_submit(self):
        self.find_element((By.CSS_SELECTOR, 'input.us_Submit_reg')).click()

    def qq_input(self, qq):
        self.find_element((By.CSS_SELECTOR, 'input[name="extend_field2"]')).send_keys(qq)

    def worktel_input(self, worktel):
        self.find_element((By.CSS_SELECTOR, 'input[name="extend_field3"]')).send_keys(worktel)

    def hometel_input(self, hometel):
        self.find_element((By.CSS_SELECTOR, 'input[name="extend_field4"]')).send_keys(hometel)

    def tips_input(self):
        pass

    def answer_input(self, answer):
        self.find_element((By.CSS_SELECTOR, 'input[name=""passwd_answer""]')).send_keys(answer)

    def havetocilck(self):
        self.find_element((By.CSS_SELECTOR, 'input[name="agreement"]')).click()

    def get_happyname_text(self):
        return self.find_element((By.CSS_SELECTOR, '.f4_b')).text


if __name__ == '__main__':
    driver = open_browser("chrome")
    rp = Register_page(driver)
    rp.open_url_register()
    rp.username_input("admin1234")
    rp.email_input("1234567@qq.com")
    rp.password_input('123456')
    rp.confirm_password('123456')
    rp.tel_input('123')
    rp.click_submit()
