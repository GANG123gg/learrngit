import pymysql
import xlrd


class mysql_connect_zong():

    def mysql_zong(self,grammar):
        conn = pymysql.connect(host='47.115.58.191',port=3306,user='root',password='ght2020',
                               database='park-basic',charset='utf8')
        cur = conn.cursor()
        sql = grammar
        cur.execute(sql)
        date = cur.fetchall()
        print(date)
        cur.close()
        return date



# conn = pymysql.connect(host='47.115.58.191',port=3306,user='root',password='ght2020',
#                                database='park-basic',charset='utf8')
# cur = conn.cursor()
# sql = "select d.rule_interval_id from rule_day_parting p JOIN rule_duration d on p.id = d.day_parting_id where p.create_by = 'wzct' and p.del_state = 0 and p.service_type_code = -1 "
# cur.execute(sql)
# date = cur.fetchall()
# # url = '/park/base/vehicleMeal/delVehicleMeal/'
# # for i in date:
# #     url_path =url+str(i[0])
# #     print(url_path)
# print(date)
# print(date[0][0])
# cur.close()


# list_values = []
# file = xlrd.open_workbook(r'F:\2020\untitled\Zong_TingChe\port\zong_dura_charge_test.xls')
# table = file.sheet_by_name('DurationCharge')
# # rows = table.nrows
# for i in range(1,2):
#     list_values.append(table.row_values(i))
# print(int(list_values[0][1]))
