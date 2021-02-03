from common import base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# 后台登录页面url
url = 'http://localhost:8080/ecshop/admin/privilege.php?act=login'


class PageLogin(base.Base):
    def remove_alert(self):
        self.find_element((By.CSS_SELECTOR, 'span[onclick="btnCancel(this)"]')).click()

    def login_admin(self):
        self.remove_alert()
        self.find_element((By.CSS_SELECTOR, '#cloudLogin')).click()

    def input_username_admin(self, account='admin'):
        self.find_element((By.CSS_SELECTOR, 'input[name="username"]')).send_keys(account)

    def input_password_admin(self, password='qq1154371933'):
        self.find_element((By.CSS_SELECTOR, 'input[name="password"]')).send_keys(password)

    def click_submit(self):
        self.find_element((By.CSS_SELECTOR, '.btn-a')).click()

    # def click_manageOfgoods_add(self):


if __name__ == '__main__':
    driver = base.open_browser()
    pl = PageLogin(driver)
    driver.get(url)
    pl.login_admin()
    pl.input_username_admin()
    pl.input_password_admin()
    pl.click_submit()
    driver.switch_to.frame('menu-frame')
    pl.find_element((By.CSS_SELECTOR, 'li[data-key="01_goods_list"]')).click()  # 点击商品管理
    pl.find_element((By.CSS_SELECTOR, 'a[href="goods.php?act=add"]')).click()  # 点击添加新商品
    driver.switch_to.parent_frame()
    driver.switch_to.frame('main-frame')
    pl.find_element((By.CSS_SELECTOR, 'input[style="float:left;color:;"]')).send_keys("电动滑板鞋")  # 商品名称
    select1 = pl.find_element((By.CSS_SELECTOR, 'select[name="goods_name_style"]'))
    Select(select1).select_by_value('strong')  # 字体样式
    pl.find_element((By.CSS_SELECTOR, 'input[name="goods_sn"]')).send_keys('101')  # 商品货号
    select2 = pl.find_element((By.CSS_SELECTOR, 'select[onchange="hideCatDiv()"]'))
    Select(select2).select_by_value('18')
    # pl.find_element((By.CSS_SELECTOR, 'button[onclick="rapidCatAdd()"]')).click()  # 点击添加分类
    pl.find_element((By.CSS_SELECTOR, 'input[onclick="addOtherCat(this.parentNode)"]')).click()  # 点击扩展
    select3 = pl.find_element((By.CSS_SELECTOR, 'select[name="other_cat[]"]'))  # 定位
    Select(select3).select_by_value('19')
    select4 = pl.find_element((By.CSS_SELECTOR, 'select[onchange="hideBrandDiv()"]'))  # 定位商品品牌select标签
    Select(select4).select_by_value('15')  # 选择value=15的品牌(仓品)
    select5 = pl.find_element((By.CSS_SELECTOR, '#suppliers_id'))  # 定位选择供货商select标签
    Select(select5).select_by_value('2')  # 选择上海供货商
    pl.find_element((By.CSS_SELECTOR, 'input[onblur="priceSetted()"]')).clear()  # 清空本店售价文本
    pl.find_element((By.CSS_SELECTOR, 'input[onblur="priceSetted()"]')).send_keys('188')  # 本店售价188
    # pl.find_element((By.CSS_SELECTOR, '.rank_1')).clear()  # 清空 会员价格>注册用户
    # pl.find_element((By.CSS_SELECTOR, '.rank_1')).send_keys('888')  # 注册会员价格888
    pl.find_element((By.CSS_SELECTOR, 'input[name="volume_number[]"]')).send_keys('5')  # 优惠数量为5个
    pl.find_element((By.CSS_SELECTOR, 'input[name="volume_price[]"]')).send_keys('20')  # 当优惠梳理为5时,优惠20
    pl.find_element((By.CSS_SELECTOR, 'input[onclick="handlePromote(this.checked);"]')).click()  # 勾选促销价
    pl.find_element((By.CSS_SELECTOR, 'input[name="promote_price"]')).clear()  # 清空促销价文本
    pl.find_element((By.CSS_SELECTOR, 'input[name="promote_price"]')).send_keys('88')  # 促销价设置为88
    # 修改促销开始时间
    js = "document.getElementById('promote_start_date').value='2021-03-21'"
    driver.execute_script(js)
    # 修改促销结束时间
    js2 = "document.getElementById('promote_end_date').value='2021-04-21'"
    driver.execute_script(js2)
    #  上传商品图片
    pl.find_element((By.CSS_SELECTOR, 'input[name="goods_img"]')).send_keys(r'C:\3000soft\Red Spider\Language\logo.jpg')
    pl.find_element((By.CSS_SELECTOR, 'div.button-div>input[type="button"]')).click()  # 点击确定

