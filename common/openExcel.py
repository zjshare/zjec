import pandas


class OpenExcel(object):
    def __init__(self, filepath, converters, sheet_name):
        self.excel = pandas.read_excel(
            filepath, converters=converters, sheet_name=sheet_name)

    def get_list(self):
        return self.excel.values.tolist()

    def get_dict(self):
        li = []
        for i in self.excel.index.values:
            li.append(self.excel.loc[i].to_dict())
        return li


if __name__ == '__main__':
    oe = OpenExcel('测试数据.xlsx', {"password": str, "number": str}, "用户信息")
    print(oe.get_dict())

    print(oe.get_list())
    #     oe = Excel(r'C:\Users\Administrator\Desktop\ecshop自动化\case\测试数据.xlsx', {"password": str, "number": str},
    #                sheet_name='用户登录合法数据')
    #     print(oe.get_dict())
    #     print(oe.get_list())
    data = pandas.read_excel(
        r'C:\Users\Administrator\Desktop\ecshop自动化\case\测试数据.xlsx')
    wei = data.loc[1].to_dict()
    print(str(wei["username"]))
