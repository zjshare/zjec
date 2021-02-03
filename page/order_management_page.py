from common.base import Base
from selenium.webdriver.common.by import By

url_login = "http://localhost:8080/ecshop/admin/privilege.php?act=login"

url = "http://localhost:8080/ecshop/admin/index.php"


class ORDERMANAGEMENT_PAGE(Base):
    btuCancel_loc = (By.CSS_SELECTOR, "span[onclick='btnCancel(this)']")
    click_EC_loc = (By.CSS_SELECTOR, "#cloudLogin")
    username_loc = (By.CSS_SELECTOR, "input[type='text'][name='username']")
    password_loc = (By.CSS_SELECTOR, "input[type='password'][name='password']")
    login_loc = (By.CSS_SELECTOR, ".btn-a")
    frame_loc = (By.CSS_SELECTOR, "#menu-frame")
    OM_loc = (By.CSS_SELECTOR, "[data-key='02_order_list']")
    OC_loc = (By.CSS_SELECTOR, "sub-menu-03_order_query")

    def butCanael(self):
        self.click_element(self.btuCancel_loc)

    def click_EC(self):
        self.click_element(self.click_EC_loc)

    def username(self, user):
        self.send_keys_element(self.username_loc, user)

    def password(self,pd):
        self.send_keys_element(self.password_loc,pd)

    def login(self):
        self.click_element(self.login_loc)

    def inframe(self):
        self.in_frame(self.frame_loc)

    def click_OM(self):
        self.click_element(self.OM_loc)

    def click_OC(self):
        self.click_element(self.OC_loc)
