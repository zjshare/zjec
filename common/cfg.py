"""
1. 学习目标

2. 概念

3. 语法

4. 案例
"""
import configparser


def get_db_cfg():
    """
    将配置文件中的数据库连接信息读取出来
    :return: 返回读取的字典
    """
    cfg = configparser.ConfigParser()
    cfg.read("db.ini", encoding="utf8")

    data = dict(cfg.items("database"))  # 将读取的数据转化成字典

    # 修改字典
    data["port"] = int(data['port'])  # 将端口号 转化成 int
    return data


if __name__ == '__main__':
    res = get_db_cfg()
    print(res)
