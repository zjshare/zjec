"""
对pymysql 进行二次封装,让我们操作数据库更加的方便
"""
import pymysql


class Database(object):
    def __init__(self, database: str, password: str, host: str = "127.0.0.1", user: str = "root",
                 charset: str = "utf8", port: int = 3307):
        """
        初始化数据库连接对象
        :param database: 数据库名
        :param password: 密码
        :param host: ip地址
        :param user: 用户名
        :param charset: 字符集
        :param port: 端口号
        """
        self.cnn = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            charset=charset,
            port=int(port)
        )

    def __del__(self):  # 对象被销毁的时候调用执行
        """
        销毁对象的同时关闭数据库连接
        :return:
        """
        self.cnn.close()

    def read_all(self, sql: str, args: list = None):
        """
        获取所有数据
        :param sql: sql语句
        :param args: 需要的参数
        :return: 查询的结果
        """
        # 使用连接对象创建游标对象
        with self.cnn.cursor(cursor=pymysql.cursors.DictCursor) as cursor:
            cursor.execute(sql, args)  # 执行sql语句
            data = cursor.fetchall()
        return data

    def read_one(self, sql: str, args: list = None):
        """
        获取一条数据
        :param sql: sql语句
        :param args: 需要的参数
        :return: 查询的结果
        """
        # 使用连接对象创建游标对象
        with self.cnn.cursor(cursor=pymysql.cursors.DictCursor) as cursor:
            cursor.execute(sql, args)  # 执行sql语句
            data = cursor.fetchone()
        return data

    def execute_one(self, sql: str, args: list = None):
        """
        执行一条sql语句
        :param sql:
        :param args:
        :return:
        """
        # 使用连接对象创建游标对象
        try:
            with self.cnn.cursor() as cursor:
                res = cursor.execute(sql, args)  # 返回受影响的行数
                if res != 1:
                    raise Exception("写入数据失败!")
                # 提交数据
                self.cnn.commit()
                return True
        except Exception as e:
            # 回滚
            self.cnn.rollback()
            print("错误:", e)
            return False

    def execute_many(self, sql: str, args: list):
        """
        执行多条sql语句
        :param sql:
        :param args:
        :return:
        """
        # 使用连接对象创建游标对象
        try:
            with self.cnn.cursor() as cursor:
                res = cursor.executemany(sql, args)  # 返回受影响的行数
                if res != len(args):
                    raise Exception("写入数据失败!")
                # 提交数据
                self.cnn.commit()
                return True
        except Exception as e:
            # 回滚
            self.cnn.rollback()
            print("错误:", e)
            return False

    def execute(self, sql: str, args: list = None):
        # 使用连接对象创建游标对象
        try:
            with self.cnn.cursor() as cursor:
                cursor.execute(sql, args)  # 返回受影响的行数
                self.cnn.commit()
                return True
        except Exception as e:
            # 回滚
            self.cnn.rollback()
            print("错误:", e)
            return False


if __name__ == '__main__':
    # database = Database(database="test", password="root")
    # sql = 'INSERT INTO student(stu_no,stu_name,class_id,age,money) VALUES(%s,%s,%s,%s,%s)'
    # args = [("itsrc-020", "张一", 1, 20, 250),
    #         ("itsrc-021", "张二", 1, 20, 250),
    #         ("itsrc-022", "张三", 1, 20, 250),
    #         ("itsrc-023", "张五", 1, 20, 250),
    #         ("itsrc-024", "张四", None, 20, 250)]
    # res = database.execute_many(sql, args)
    # if res:
    #     print("成功")
    # else:
    #     print("失败")

    db = Database("ecshop", "168168", port=3307)
    goods_name = "电动滑板鞋"
    # sql = "select * from ec_users where user_name = %s"
    # args = [username]
    # data = db.execute_one(sql, args)
    # print(data)
    sql = "select goods_name from ec_goods where goods_name=%s"
    args = [goods_name]
    # sqlcheck = db.read_one(sql, args)
    # print(sqlcheck)
    print(db.execute(sql,args))

