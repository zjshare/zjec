# from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

# 从base包导入Base类
from common.base import Base

# 定义登录地址
# info_url = "http://localhost:8080/ecshop/user.php"
info_url = "http://localhost:8080/ecshop/user.php"


# 定义一个 个人中心页面
class Info(Base):
    # 定位元素
    username_loc = (By.NAME, "username")
    password_loc = (By.NAME, "password")
    # 登录
    submit_loc = (By.XPATH, '/html/body/div[6]/div[1]/form/table/tbody/tr[4]/td[2]/input[3]')
   #用户信息链接
    a_userinfo_loc =(By.XPATH,'/html/body/div[6]/div[1]/div/div/div/div/a[2]')
    birthdayYear_loc = (By.NAME, "birthdayYear")
    birthdayMonth_loc = (By.NAME, "birthdayMonth")
    birthdayDayr_loc = (By.NAME, "birthdayDay")
    sex1_loc = (By.XPATH, "/html/body/div[6]/div[2]/div/div/div/form[1]/table/tbody/tr[2]/td[2]/input[1]")  # 保密
    sex2_loc = (By.XPATH, "/html/body/div[6]/div[2]/div/div/div/form[1]/table/tbody/tr[2]/td[2]/input[2]")  # 男
    sex3_loc = (By.XPATH, "/html/body/div[6]/div[2]/div/div/div/form[1]/table/tbody/tr[2]/td[2]/input[3]")  # 女
    email_loc = (By.NAME, "email")
    extend_field5_loc = (By.NAME, 'extend_field5')  # 手机号
    old_password_loc = (By.NAME, 'old_password')  # 原密码
    new_password_loc = (By.NAME, 'new_password')  # 新密码
    comfirm_password_loc = (By.NAME, 'comfirm_password')  # 确认密码
    submit_info_loc=(By.XPATH,'/html/body/div[6]/div[2]/div/div/div/form[1]/table/tbody/tr[10]/td/input[2]')
    submit_pwd_loc = (By.XPATH, '/html/body/div[6]/div[2]/div/div/div/form[2]/table/tbody/tr[4]/td/input[2]')  # 密码确认按钮
    a_rest_loc =(By.XPATH,'//*[@id="ECS_MEMBERZONE"]/a[1]') # 重置页面后 请登录元素

    #
    #

    # 操作元素
    # 输入 用户名
    def input_username(self, username):
        self.send_keys_element(self.username_loc, username)

    # 输入密码
    def input_password(self, password):
        self.send_keys_element(self.password_loc, password)

    # 点击 登录按钮
    def click_submit(self):
        self.click_element(self.submit_loc)
    # 点击 用户信息链接
    def click_a_userinfo(self):
        self.click_element(self.a_userinfo_loc)

    def sel_year(self, text):
        self.select(self.birthdayYear_loc, text)

    def sel_month(self, text):
        self.select(self.birthdayMonth_loc, text)

    def sel_day(self, text):
        self.select(self.birthdayDayr_loc, text)

    # 清空输入框
    def inp_c(self, locator, timeout=10):
        self.input_c(locator, timeout)

    # 输入 email
    def input_email(self, email):
        self.send_keys_element(self.email_loc, email)

    # 输入手机号
    def input_phone(self, phone):
        self.send_keys_element(self.extend_field5_loc, phone)

    # 输入原密码
    def input_old_password(self, old_password):
        self.send_keys_element(self.old_password_loc, old_password)

    # 输入新密码
    def input_new_password(self, new_password):
        self.send_keys_element(self.new_password_loc, new_password)

    # 输入确认密码
    def input_comfirm_password(self, comfirm_password):
        self.send_keys_element(self.comfirm_password_loc, comfirm_password)

    # 点击确认按钮
    def btn_submit(self):
        self.click_element(self.submit_pwd_loc)

    # 获取请登录链接内容
    def a_rest(self):
        return self.get_element_text(self.a_rest_loc)


if __name__ == '__main__':
    # #谷歌
    # # 个人加载项地址
    user_data_dir = r"--user-data-dir=C:\Users\DELL\AppData\Local\Google\Chrome\User Data"
    # 实例化加载配置对象
    option = webdriver.ChromeOptions()

    # 给加载对象添加个人资料路径
    option.add_argument(user_data_dir)

    # 打开浏览器  使用个人加载项配置 ==> 必须要关闭所有的浏览器
    driver = webdriver.Chrome(options=option)
    driver.get(info_url)
    lp = Info(driver)
    lp.sel_year('1999')
    lp.sel_month('02')
    lp.sel_day('30')
    lp.inp_c(lp.email_loc)
    lp.input_email('1294676790@qq.com')

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#     # 创建一个浏览器对象
#     driver = open_browser()
#     #  实例化一个个人信息对象 因为继承了Base,所以要传入一个driver
#     lp= Info(driver)
#     lp.open_url(info_url)
#     sleep(10)
#     lp.quit()
