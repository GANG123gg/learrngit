import xlrd
import unittest
from ddt import ddt,data,unpack

def get_zong_xls(filexpath):
    list_values = []
    file = xlrd.open_workbook(filexpath)
    table = file.sheet_by_name('GroupAdminNo')
    rows = table.nrows
    for i in range(1,rows):

        list_values.append(table.row_values(i))
    return list_values
@ddt
class TestCases(unittest.TestCase):
    #@data('admin','zhiyi')#单个值，代表的一个用例
    #@data(['admin','123456'],['zhiyi','123'])

    #获取excel里面的数据,数据多少条不固定，有多少行就代表多少个用例
    datas = get_zong_xls(r'zong_login_test.xls')
    caseDatas=list(datas)

    #@data(('admin','123456'),('zhiyi','123')) #多个值
    #@data(*[('admin','123456'),('zhiyi','123')])#所有的用例元素组装成一个大列表，*解包多个用例
    #@unpack #把一个整体的值（用例）解包成具体的参数，用例需要用相对应的参数来接收
    #@file_data('./test.yaml')
    @data(*caseDatas)
    @unpack
    def test(self,head,username,password,group_name,name,phone,email,address,element,assertion,result):
        print(head,username,password,group_name,name,phone,email,address,element,assertion,result)



if __name__ == '__main__':
    unittest.main()
