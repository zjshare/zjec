import unittest
from common.database import Database
from time import sleep
import ddt
from common.base import Base, open_browser_option
from page.page_integral import Integral,integral_url
# 实例化数据库对象
data = Database('ecshop_zj', password='root', port=3308)
# 读取数据库内容
data_sql = data.read_one("select pay_points from ecs_users where user_name='a123456'")


@ddt.ddt
class IntegralCase(unittest.TestCase):
    def setUp(self):
        driver = open_browser_option()
        driver.get(integral_url)
        self.lp = Integral(driver)
        sleep(5)

    def tearDown(self):
        self.lp.quit()


    def integra(self):
        te = self.lp.get_text()
        return te



    @ddt.data(data_sql)
    def test_case_01(self,db):
        #  integra()[0]:integra()返回来的是一个列表,
        #  db接收到的是一个字典,  str(db['pay_points'])把获取到的值转换为一个字符串
        self.assertEqual(self.integra()[0], str(db['pay_points']))


if __name__ == '__main__':
    unittest.main()
