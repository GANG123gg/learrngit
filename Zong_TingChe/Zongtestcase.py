import unittest
from HTMLTestRunner import HTMLTestRunner

import xlrd
from ddt import ddt,data,unpack
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from Zong_TingChe.UserAdmin.zong_Groupadmin import GroupAdmin_zong
from Zong_TingChe.UserAdmin.zong_OwnerAdmin import OwnerAdmin_zong
from Zong_TingChe.UserAdmin.zong_ShopAdmin import ShopAdmin_Zong
from Zong_TingChe.UserAdmin.zong_PlatformAdmin import Platform_Admin_Zong
from Zong_TingChe.UserAdmin.zong_ServiceAdmin import ServiceAdmin_Zong
from Zong_TingChe.UserAdmin.zong_PatrolAdmin import PatrolAdmin_Zong
from Zong_TingChe.ZongBrowser import ZongBrowser
from Zong_TingChe.Zongoperationpage import OperaPage_Login
from time import sleep
from Zong_TingChe.ParkAdmin.zong_ParkList import ParkList_Zong
from Zong_TingChe.ParkAdmin.zong_DeviceAdmin_terminal import Terminal_Zong
from Zong_TingChe.ParkAdmin.zong_DeviceAdmin_camera import Camera_Zong
from Zong_TingChe.ParkAdmin.zong_DeviceAdmin_display import Display_Zong
from Zong_TingChe.ParkAdmin.zong_Charge_Temporary import Charge_Temporary_Zong
from Zong_TingChe.ParkAdmin.zong_Charge_VIP import Charge_VIP_Zong
from Zong_TingChe.ParkAdmin.zong_Service_Member import Service_Member_Zong
from Zong_TingChe.ParkAdmin.zong_Service_VIP import Service_VIP_Zong
from Zong_TingChe.ParkAdmin.zong_Discount_List import Discounts_List_Zong
from Zong_TingChe.ParkAdmin.zong_BlackList import BlackList
from Zong_TingChe.SystemAdmin.system_set import Set_Tag


def get_zong_xls(filexpath,sheet):
        '''
        封装批量读取Excel数据
        :param filexpath:
        :return:
        '''
        list_values = []
        file = xlrd.open_workbook(filexpath)
        table = file.sheet_by_name(sheet)
        rows = table.nrows
        for i in range(1,rows):
            list_values.append(table.row_values(i))
        return list_values
login_list_values = (r'zong_login_test.xls')
login_list = 'Login'
group_list_add = 'GroupAdmin'
group_list_update_one = 'GroupRedactOne'
group_list_update_two = 'GroupRedactTwo'
group_list_find = 'GroupFind'

#业主管理
owner_list_values = (r'zong_owner_test.xls')
owner_list_add_one = 'OwnerAddOne'
owner_list_update_one = 'OwnerUpateOne'
owner_list_update_three = 'OwnerUpateThree'
owner_list_find_one = 'OwnerFindOne'
owner_list_del = 'OwnerDelOne'

#商家管理
shop_list_values = (r'zong_shop_test.xls')
shop_list_add = 'ShopAddOne'
shop_list_update = 'ShopUpdateOne'
shop_list_find = 'ShopFindOne'
shop_list_del = 'ShopDelOne'

#平台管理
platform_list_values = (r'zong_platform.xls')
platform_list_add = 'platformAdd'
platform_list_up = 'platformUp'
platform_list_find = 'platformFind'
platform_list_del = 'plaformDel'

#客服管理
service_list_values = (r'zong_service_test.xls')
service_list_add_one = 'ServiceAddOne'
service_list_update_one = 'ServiceUpdateOne'
service_list_find = 'ServiceFind'
service_list_del = 'ServiceDel'

#巡逻岗管理
patrol_list_values = (r'zong_patrol_test.xls')
patrol_list_add_one = 'PatrolAddOne'
patrol_list_update_one = 'PatrolUpdateOne'
patrol_list_find = 'PatrolFind'
patrol_list_del = 'PatrolDel'

#车场列表
park_list_values = (r'zong_park_test.xls')
park_list_add_one = 'ParkAdd'
park_list_update_one = 'ParkUpdate'
park_list_find = 'ParkFind'

#纵停终端
terminal_list_values = (r'zong_terminal_test.xls')
terminal_list_add = 'TerminalAdd'
terminal_list_update = 'TerminlaUpdate'
terminal_list_find = 'TerminalFind'
terminal_list_del = 'TerminalDel'

#相机
camera_list_values = (r'zong_camera_test.xls')
camera_list_add = 'CameraAdd'
camera_list_update = 'CameraUpdate'
camera_list_find = 'CameraFind'
camera_list_del = 'CameraDel'

#显示屏
display_list_values = (r'zong_display_test.xls')
display_list_add = 'DisplayAdd'
display_list_update = 'DisplayUpdate'
display_list_find = 'DisplayFind'
display_list_del = 'DisplayDel'

#临时计费规则
charge_temporary_list_values = (r'')
charge_temporary_list_add = ''
charge_temporary_list_update = ''
charge_temporary_list_find = ''
charge_temporary_list_del = ''

#VIP套餐
charge_vip_list_values = (r'zong_charge_vip_text.xls')
charge_vip_list_add = 'ChargeVIPAdd'
charge_vip_list_update = 'ChargeVIPUpdate'
charge_vip_list_find = 'ChargeVIPFind'
charge_vip_list_del = 'ChargeVIPDel'

#会员车服务
service_member_list_values = (r'zong_service_member_test.xls')
service_member_list_add = 'ServiceMemberAdd'
service_member_list_update = 'ServiceMemberUpdate'
service_member_list_find = 'ServiceMemberFind'
service_member_list_import = 'ServiceMemberImport'
service_member_list_del = 'ServiceMemberDel'

#贵宾车服务
service_vip_list_values = (r'zong_service_vip_test.xls')
service_vip_list_add = 'ServiceAdd'
service_vip_list_update = 'ServiceUpdate'
service_vip_list_find = 'ServiceFind'
service_vip_list_import = 'ServiceImport'
service_vip_list_del ='ServiceDel'

#优惠券列表
discount_list_list_values = (r'zong_discount_list_test.xls')
discount_list_list_add = 'ListAdd'
discount_list_list_recharge = 'ListRecharge'
discount_list_list_find = 'ListFind'
discount_list_list_del = 'ListDel'

#黑名单
blacklist_values = (r'zong_blacklist_test.xls')
blacklist_add = 'BlackAdd'
blacklist_import = 'BlackImport'
blacklist_find = 'BlackFind'
blacklist_del = 'BlackDel'

#标识配置
tag_list_values = (r'zong_system_tag.xls')
tag_list_update = 'TagUpdate'


@ddt#集团管理
class TestCase_Login_groupTest(unittest.TestCase,GroupAdmin_zong):
    def setUp(self):
        self.opts = webdriver.ChromeOptions()
        self.opts.add_argument('--headless')
        self.opts.add_argument('--window-size=1440,900')
        self.driver = webdriver.Chrome(chrome_options=self.opts)
        # self.driver = webdriver.Chrome()
        # self.driver.maximize_window()
        self.driver.get('https://test.ghparking.com/')
        self.driver.implicitly_wait(10)
        self.browser = ZongBrowser(self.driver)

    datas = get_zong_xls(login_list_values,login_list)
    casedatas = list(datas)
    @data(*casedatas)
    @unpack
    def test_1login01(self,head,username,password,result,element,assertion):
        '''
        "head"
        :return:
        '''
        self.log_zong(head)
        self.login_zonglogin(username,password)
        # ele = self.driver.find_elements_by_xpath('//*[@id="app"]/div/div[1]/div[1]/a/h1')
        # self.assertEqual(len(ele),1)
        self.assertEqual(self.assert_text_zong(OperaPage_Login.login_assert,element),assertion)
        self.log_zong(result)

    group_datas = get_zong_xls(login_list_values,group_list_add)
    group_casedatas = list(group_datas)
    @data(*group_casedatas)
    @unpack
    def test_2group01(self,head,username,password,choose,group_name,name,phone,email,address,
                    account,select_date_one,select_date_two,select_time_two,element,assertion,result):
        '''
        新增集团账号
        :param head: 标题
        :param username: 账号
        :param password: 密码
        :param group_name: 集团名称
        :param name: 负责人姓名
        :param phone: 联系方式
        :param email: 邮箱
        :param address: 详细地址
        :param select_date_one: 生效时间
        :param select_date_two: 截止时间
        :param element: 定位元素路径
        :param assertion: 断言
        :param result: 测试结果
        :return:
        '''

        self.group_adduser(head,username,password,choose,group_name,name,phone,email,address,
                           account,select_date_one,select_date_two,select_time_two)
        self.assertEqual(self.assert_text_zong(OperaPage_Login.login_assert,element),assertion)
        self.log_zong(result)

    group_update_one_datas = get_zong_xls(login_list_values,group_list_update_one)
    group_update_one_casedatas = list(group_update_one_datas)
    @data(*group_update_one_casedatas)
    @unpack
    def test_3groupupdate01(self,head,username,password,choose,ele,element,assertion,result):
        self.group_update(head,username,password,choose,ele)
        self.assertEqual(self.assert_text_zong(OperaPage_Login.login_assert,element),assertion)
        self.log_zong(result)

    group_update_two_datas = get_zong_xls(login_list_values,group_list_update_two)
    group_update_two_casedatas = list(group_update_two_datas)
    @data(*group_update_two_casedatas)
    @unpack
    def test_4groupupdate02(self,head,username,password,expiration_date,
                          expiration_time,effective_date,effective_time,element,assertion,result):
        self.group_update_one(head,username,password,expiration_date,expiration_time,effective_date,effective_time)
        self.assertEqual(self.assert_text_zong(OperaPage_Login.login_assert,element),assertion)
        self.log_zong(result)

    group_find_datas = get_zong_xls(login_list_values,group_list_find)
    group_find_casedatas = list(group_find_datas)
    @data(*group_find_casedatas)
    @unpack
    def test_5groupfind01(self,head,username,password,element_search,values,element,
                          assertion,result,element_reset,assertion_reset,result_reset):
        self.group_checkuser_search(head,username,password,OperaPage_Login.login_assert,element_search,values)
        self.assertEqual(self.assert_text_zong(OperaPage_Login.login_assert,element),assertion)
        self.log_zong(result)
        self.group_checkuser_reset()
        self.assertEqual(self.assert_text_zong(OperaPage_Login.login_assert,element_reset),assertion_reset)
        self.log_zong(result_reset)


    def tearDown(self):
        self.driver.quit()

@ddt#业主管理
class TestCase_OwnerTest(unittest.TestCase,OwnerAdmin_zong):

    def setUp(self):
        self.opts = webdriver.ChromeOptions()
        self.opts.add_argument('--headless')
        self.opts.add_argument('--window-size=1440,900')
        self.driver = webdriver.Chrome(chrome_options=self.opts)
        # self.driver = webdriver.Chrome()
        # self.driver.maximize_window()
        self.driver.get('https://test.ghparking.com/')
        self.driver.implicitly_wait(10)
        self.browser = ZongBrowser(self.driver)

    owner_add_one_datas = get_zong_xls(owner_list_values,owner_list_add_one)
    owner_add_one_casedatas = list(owner_add_one_datas)
    @data(*owner_add_one_casedatas)
    @unpack
    def test_1owneradd01(self,head,username,password,choose,company_name,ownername,phone,card,address,effective_date,effective_time,
                  expiration_date,expiration_time,element,assertion,result):
        self.owner_add_one(head,username,password,choose,company_name,ownername,phone,card,address,effective_date,effective_time,
                  expiration_date,expiration_time)
        self.assertEqual(self.assert_text_zong(OperaPage_Login.login_assert,element),assertion)
        self.log_zong(result)

    owner_update_one_datas = get_zong_xls(owner_list_values,owner_list_update_one)
    owner_update_one_casedatas = list(owner_update_one_datas)
    @data(*owner_update_one_casedatas)
    @unpack
    def tset_2ownerupdate01(self,head,username,password,choose,ele,element,assertion,result):
        self.owner_update_one(head,username,password,choose,ele)
        self.assertEqual(self.assert_text_zong(OperaPage_Login.login_assert,element),assertion)
        self.log_zong(result)

    owner_update_three_datas = get_zong_xls(owner_list_values,owner_list_update_three)
    owner_update_three_casedatas = list(owner_update_three_datas)
    @data(*owner_update_three_casedatas)
    @unpack
    def test_3ownerupdate03(self,head,username,password,expiration_date,expiration_time,
                          effective_date,effective_time,element,assertion,result):
        self.owner_update_three(head,username,password,expiration_date,expiration_time,effective_date,effective_time)
        self.assertEqual(self.assert_text_zong(OperaPage_Login.login_assert,element),assertion)
        self.log_zong(result)

    owner_find_one_datas = get_zong_xls(owner_list_values,owner_list_find_one)
    owner_find_one_casedatas = list(owner_find_one_datas)
    @data(*owner_find_one_casedatas)
    @unpack
    def test_4ownercheck01(self,head,username,password,ele,value,element,assertion,result,
                           element_reset,assertion_reset,result_reset):
        self.owner_check_search(head,username,password,ele,value)
        self.assertEqual(self.assert_text_zong(OperaPage_Login.login_assert,element),assertion)
        self.log_zong(result)
        self.owner_check_reset()
        self.assertEqual(self.assert_text_zong(OperaPage_Login.login_assert,element_reset),assertion_reset)
        self.log_zong(result_reset)

    owner_del_datas = get_zong_xls(owner_list_values,owner_list_del)
    owner_del_casedatas = list(owner_del_datas)
    @data(*owner_del_casedatas)
    @unpack
    def test_5ownerdel01(self,head,username,password,element,assertion,result):
        self.owner_del(head,username,password)
        self.assertEqual(self.assert_text_zong(OperaPage_Login.login_assert,element),assertion)
        self.log_zong(result)


    def tearDown(self):
        self.driver.quit()

@ddt#商家管理
class TestCase_ShopTest(unittest.TestCase,ShopAdmin_Zong):

    def setUp(self):
        # self.opts = webdriver.ChromeOptions()
        # self.opts.add_argument('--headless')
        # self.opts.add_argument('--window-size=1440,900')
        # self.driver = webdriver.Chrome(chrome_options=self.opts)#无头模式
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://test.ghparking.com/')
        self.driver.implicitly_wait(10)
        self.browser = ZongBrowser(self.driver)

    shop_add_one_datas = get_zong_xls(shop_list_values,shop_list_add)
    shop_add_one_casedatas = list(shop_add_one_datas)
    @data(*shop_add_one_casedatas)
    @unpack
    def test_1shopadd(self,head,username,password,choose,shopname,personname,phone,discount,account,
                      element,assertion,result):
        self.shop_add_one(head,username,password,choose,shopname,personname,phone,discount,account)
        self.assertEqual(self.assert_text_zong(OperaPage_Login.login_assert,element),assertion)
        self.log_zong(result)

    shop_update_one_datas = get_zong_xls(shop_list_values,shop_list_update)
    shop_update_one_casedatas = list(shop_update_one_datas)
    @data(*shop_update_one_casedatas)
    @unpack
    def test_2shopupdate(self,head,username,password,choose,ele,values,element,assertion,result):
        self.shop_update_one(head,username,password,choose,ele,values)
        self.assertEqual(self.assert_text_zong(OperaPage_Login.login_assert,element),assertion)
        self.log_zong(result)

    shop_find_datas = get_zong_xls(shop_list_values,shop_list_find)
    shop_find_casedatas = list(shop_find_datas)
    @data(*shop_find_casedatas)
    @unpack
    def test_3shopcheck(self,head,username,password,ele,values,element,assertion,result,
                        reset_element,reset_assertion,reset_result):
        self.shop_check_search(head,username,password,OperaPage_Login.login_assert,ele,values)
        self.assertEqual(self.assert_text_zong(OperaPage_Login.login_assert,element),assertion)
        self.log_zong(result)
        self.shop_check_reset()
        self.assertEqual(self.assert_text_zong(OperaPage_Login.login_assert,reset_element),reset_assertion)
        self.log_zong(reset_result)

    shop_del_datas = get_zong_xls(shop_list_values,shop_list_del)
    shop_del_casedatas = list(shop_del_datas)
    @data(*shop_del_casedatas)
    @unpack
    def test_4shopdel(self,head,username,password,element,assertion,result):
        self.shop_del_one(head,username,password)
        self.assertEqual(self.assert_text_zong(OperaPage_Login.login_assert,element),assertion)
        self.log_zong(result)

    def tearDown(self):
        self.driver.quit()

@ddt#客服管理
class TestCase_ServiceTest(unittest.TestCase,ServiceAdmin_Zong):

    def setUp(self):
        self.opts = webdriver.ChromeOptions()
        self.opts.add_argument('--headless')
        self.opts.add_argument('--window-size=1440,900')
        self.driver = webdriver.Chrome(chrome_options=self.opts)#无头模式
        # self.driver = webdriver.Chrome()
        # self.driver.maximize_window()
        self.driver.get('https://test.ghparking.com/')
        self.driver.implicitly_wait(10)
        self.browser = ZongBrowser(self.driver)

    service_add_one_datas = get_zong_xls(service_list_values,service_list_add_one)
    service_add_one_casedatas = list(service_add_one_datas)
    @data(*service_add_one_casedatas)
    @unpack
    def test_1service_add01(self,head,username,password,choose,name,phone,account,element,assertion,result):
        self.service_add_one(head,username,password,choose,name,phone,account)
        self.assertEqual(self.assert_text_zong(OperaPage_Login.login_assert,element),assertion)
        self.log_zong(result)

    service_update_one_datas = get_zong_xls(service_list_values,service_list_update_one)
    service_update_one_casedatas = list(service_update_one_datas)
    @data(*service_update_one_casedatas)
    @unpack
    def test_2service_update01(self,head,username,password,choose,ele,values,element,assertion,result):
        self.service_update_one(head,username,password,choose,ele,values)
        self.assertEqual(self.assert_text_zong(OperaPage_Login.login_assert,element),assertion)
        self.log_zong(result)

    service_find_datas = get_zong_xls(service_list_values,service_list_find)
    service_find_casedatas = list(service_find_datas)
    @data(*service_find_casedatas)
    @unpack
    def test_3service_find(self,head,username,password,ele,values,element,assertion,result,
                         reset_element,reset_assertion,reset_result):
        self.service_check_search(head,username,password,ele,values)
        self.assertEqual(self.assert_text_zong(OperaPage_Login.login_assert,element),assertion)
        self.log_zong(result)
        self.service_check_reset()
        self.assertEqual(self.assert_text_zong(OperaPage_Login.login_assert,reset_element),reset_assertion)
        self.log_zong(reset_result)

    service_del_datas = get_zong_xls(service_list_values,service_list_del)
    service_del_casedatas = list(service_del_datas)
    @data(*service_del_casedatas)
    @unpack
    def test_4service_del(self,head,username,password,element,assertion,result):
        self.service_del(head,username,password)
        self.assertEqual(self.assert_text_zong(OperaPage_Login.login_assert,element),assertion)
        self.log_zong(result)

    def tearDown(self):
        pass
        #self.driver.quit()

@ddt#平台管理
class TestCase_PlatformTest(unittest.TestCase,Platform_Admin_Zong):
    def setUp(self):
        self.opts = webdriver.ChromeOptions()
        self.opts.add_argument('--headless')
        self.opts.add_argument('--window-size=1440,900')
        self.driver = webdriver.Chrome(chrome_options=self.opts)#无头模式
        # self.driver = webdriver.Chrome()
        # self.driver.maximize_window()
        self.driver.get('https://test.ghparking.com/')
        self.driver.implicitly_wait(10)
        self.browser = ZongBrowser(self.driver)

    platform_add_datas = get_zong_xls(platform_list_values,platform_list_add)
    platform_add_casedatas = list(platform_add_datas)
    @data(*platform_add_casedatas)
    @unpack
    def test_1platform_add(self,head,username,password,choose,name,phone,account,remark,
                           element,assertion,result):
        self.platform_admin_add(head,username,password,choose,name,phone,account,remark)
        self.assertEqual(self.assert_text_zong(OperaPage_Login.login_assert,element),assertion)
        self.log_zong(result)

    platform_up_datas = get_zong_xls(platform_list_values,platform_list_up)
    platform_up_casedatas = list(platform_up_datas)
    @data(*platform_up_casedatas)
    @unpack
    def test_2platform_up(self,head,username,password,choose,ele,values,element,assertion,result):
        self.platform_admin_update(head,username,password,choose,ele,values)
        self.assertEqual(self.assert_text_zong(OperaPage_Login.login_assert,element),assertion)
        self.log_zong(result)

    platform_find_datas = get_zong_xls(platform_list_values,platform_list_find)
    platform_find_casedatas = list(platform_find_datas)
    @data(*platform_find_casedatas)
    @unpack
    def test_3platform_find(self,head,username,password,ele,value,
                            element,assertion,result,reset_element,reset_assertion,reset_result):
        self.platform_check_search(head,username,password,ele,value)
        self.assertEqual(self.assert_text_zong(OperaPage_Login.login_assert,element),assertion)
        self.log_zong(result)
        self.platform_check_reset()
        self.assertGreater(len(self.assert_amoun_zong(OperaPage_Login.login_assert,reset_element)),reset_assertion)
        self.log_zong(reset_result)

    platform_del_datas = get_zong_xls(platform_list_values,platform_list_del)
    platform_del_casedatas = list(platform_del_datas)
    @data(*platform_del_casedatas)
    @unpack
    def test_4platform_del(self,head,username,password,element,assertion,result):
        self.platform_del(head,username,password)
        self.assertEqual(self.assert_text_zong(OperaPage_Login.login_assert,element),assertion)
        self.log_zong(result)

    def tearDown(self):
        self.driver.quit()

@ddt#巡逻岗管理
class TestCase_PatrolTest(unittest.TestCase,PatrolAdmin_Zong):

    def setUp(self):
        # self.opts = webdriver.ChromeOptions()
        # self.opts.add_argument('--headless')
        # self.opts.add_argument('--window-size=1440,900')
        # self.driver = webdriver.Chrome(chrome_options=self.opts)#无头模式
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://test.ghparking.com/')
        self.driver.implicitly_wait(10)
        self.browser = ZongBrowser(self.driver)

    pataol_add_one_datas = get_zong_xls(patrol_list_values,patrol_list_add_one)
    patrol_add_one_casedatas = list(pataol_add_one_datas)
    @data(*patrol_add_one_casedatas)
    @unpack
    def test_1patrol_add01(self,head,username,password,choose,name,phone,account,element,assertion,result):
        self.patrol_add_one(head,username,password,choose,name,phone,account)
        self.assertEqual(self.assert_text_zong(OperaPage_Login.login_assert,element),assertion)
        self.log_zong(result)

    pataol_update_one_datas = get_zong_xls(patrol_list_values,patrol_list_update_one)
    patrol_update_one_casedatas = list(pataol_update_one_datas)
    @data(*patrol_update_one_casedatas)
    @unpack
    def test_2patrol_update01(self,head,username,password,choose,ele,values,element,assertion,result):
        self.patrol_update_one(head,username,password,choose,ele,values)
        self.assertEqual(self.assert_text_zong(OperaPage_Login.login_assert,element),assertion)
        self.log_zong(result)

    pataol_find_datas = get_zong_xls(patrol_list_values,patrol_list_find)
    patrol_find_casedatas = list(pataol_find_datas)
    @data(*patrol_find_casedatas)
    @unpack
    def test_3patrol_find(self,head,username,password,ele,values,element,assertion,result,
                        reset_element,reset_assertion,reset_result):
        self.patrol_find_search(head,username,password,ele,values)
        self.assertEqual(self.assert_text_zong(OperaPage_Login.login_assert,element),assertion)
        self.log_zong(result)
        self.patrol_find_reset()
        self.assertEqual(self.assert_text_zong(OperaPage_Login.login_assert,reset_element),reset_assertion)
        self.log_zong(reset_result)

    pataol_del_datas = get_zong_xls(patrol_list_values,patrol_list_del)
    patrol_del_casedatas = list(pataol_del_datas)
    @data(*patrol_del_casedatas)
    @unpack
    def test_4patrol_del(self,head,username,password,element,assertion,result):
        self.patrol_del(head,username,password)
        self.assertEqual(self.assert_text_zong(OperaPage_Login.login_assert,element),assertion)
        self.log_zong(result)

    def tearDown(self):
        self.driver.quit()

@ddt#车场列表
class TestCase_ParkTest(unittest.TestCase,ParkList_Zong):

    def setUp(self):
        self.opts = webdriver.ChromeOptions()
        self.opts.add_argument('--headless')
        self.opts.add_argument('--window-size=1440,900')
        self.driver = webdriver.Chrome(chrome_options=self.opts)#无头模式
        # self.driver = webdriver.Chrome()
        # self.driver.maximize_window()
        self.driver.get('https://test.ghparking.com/')
        self.driver.implicitly_wait(10)
        self.browser = ZongBrowser(self.driver)

    park_add_one_datas = get_zong_xls(park_list_values,park_list_add_one)
    park_add_one_casedatas = list(park_add_one_datas)
    @data(*park_add_one_casedatas)
    @unpack
    def test_1park_add01(self,head,username,password,choose,name,temporary_amount,temporary_surplus,
                       member_amount,member_surplus,element,assertion,result):
        self.park_add_one(head,username,password,choose,name,temporary_amount,temporary_surplus,
                          member_amount,member_surplus)
        self.assertEqual(self.assert_text_zong(OperaPage_Login.login_assert,element),assertion)
        self.log_zong(result)

    park_update_one_datas = get_zong_xls(park_list_values,park_list_update_one)
    park_update_one_casedatas = list(park_update_one_datas)
    @data(*park_update_one_casedatas)
    @unpack
    def test_2park_update01(self,head,username,password,ele,choose,values,element,assertion,result):
        self.park_update_one(head,username,password,ele,choose,values)
        self.assertEqual(self.assert_text_zong(OperaPage_Login.login_assert,element),assertion)
        self.log_zong(result)

    park_find_datas = get_zong_xls(park_list_values,park_list_find)
    park_find_casedatas = list(park_find_datas)
    @data(*park_find_casedatas)
    @unpack
    def test_3park_find01(self,head,username,password,ele,values,element,assertion,result,
                        reset_element,reset_assertion,reset_result):
        self.park_find_search(head,username,password,ele,values)
        self.assertEqual(self.assert_text_zong(OperaPage_Login.login_assert,element),assertion)
        self.log_zong(result)
        self.park_find_reset()
        self.assertEqual(self.assert_text_zong(OperaPage_Login.login_assert,reset_element),reset_assertion)
        self.log_zong(reset_result)


    def tearDown(self):
        self.driver.quit()

@ddt#终端
class TestCase_TerminalTest(unittest.TestCase,Terminal_Zong):

    def setUp(self):
        self.opts = webdriver.ChromeOptions()
        self.opts.add_argument('--headless')
        self.opts.add_argument('--window-size=1440,900')
        self.driver = webdriver.Chrome(chrome_options=self.opts)#无头模式
        # self.driver = webdriver.Chrome()
        # self.driver.maximize_window()
        self.driver.get('https://test.ghparking.com/')
        self.driver.implicitly_wait(10)
        self.browser = ZongBrowser(self.driver)

    terminal_add_datas = get_zong_xls(terminal_list_values,terminal_list_add)
    terminal_add_casedatas = list(terminal_add_datas)
    @data(*terminal_add_casedatas)
    @unpack
    def test_1terminal_add01(self,head,username,password,sequence,choose,element,assertion,result):
        self.terminal_add(head,username,password,sequence,choose)
        self.assertEqual(self.assert_text_zong(OperaPage_Login.login_assert,element),assertion)
        self.log_zong(result)

    terminal_update_datas = get_zong_xls(terminal_list_values,terminal_list_update)
    terminal_update_casedatas = list(terminal_update_datas)
    @data(*terminal_update_casedatas)
    @unpack
    def test_2terminal_update01(self,head,username,password,sequence,choose,element,assertion,result):
        self.terminal_update(head,username,password,sequence,choose)
        self.assertEqual(self.assert_text_zong( OperaPage_Login.login_assert,element),assertion)
        self.log_zong(result)

    terminal_find_datas = get_zong_xls(terminal_list_values,terminal_list_find)
    terminal_find_casedatas = list(terminal_find_datas)
    @data(*terminal_find_casedatas)
    @unpack
    def test_3terminal_find(self,head,username,password,ele,values,element,assertion,result,
                          reset_element,reset_assertion,reset_result):
        self.terminal_find_search(head,username,password,ele,values)
        self.assertEqual(self.assert_text_zong(OperaPage_Login.login_assert,element),assertion)
        self.log_zong(result)
        self.terminal_find_reset()
        self.assertEqual(self.assert_text_zong(OperaPage_Login.login_assert,reset_element),reset_assertion)
        self.log_zong(reset_result)

    terminal_del_datas = get_zong_xls(terminal_list_values,terminal_list_del)
    terminal_del_casedatas = list(terminal_del_datas)
    @data(*terminal_del_casedatas)
    @unpack
    def test_4terminal_del(self,head,username,password,element,assertion,result):
        self.terminal_del(head,username,password)
        self.assertEqual(self.assert_text_zong(OperaPage_Login.login_assert,element),assertion)
        self.log_zong(result)

    def tearDown(self):
        self.driver.quit()

@ddt#相机
class TestCase_CameraTest(unittest.TestCase,Camera_Zong):

    def setUp(self):
        self.opts = webdriver.ChromeOptions()
        self.opts.add_argument('--headless')
        self.opts.add_argument('--window-size=1440,900')
        self.driver = webdriver.Chrome(chrome_options=self.opts)#无头模式
        # self.driver = webdriver.Chrome()
        # self.driver.maximize_window()
        self.driver.get('https://test.ghparking.com/')
        self.driver.implicitly_wait(10)
        self.browser = ZongBrowser(self.driver)

    camera_add_datas = get_zong_xls(camera_list_values,camera_list_add)
    camera_add_casedatas = list(camera_add_datas)
    @data(*camera_add_casedatas)
    @unpack
    def test_1camera_add(self,head,username,password,choose,delete,sequence,ip,genre,
                       element,assertion,result):
        self.camera_add(head,username,password,choose,delete,sequence,ip,genre)
        self.assertEqual(self.assert_text_zong(OperaPage_Login.login_assert,element),assertion)
        self.log_zong(result)

    camera_update_datas = get_zong_xls(camera_list_values,camera_list_update)
    camera_update_casedatas = list(camera_update_datas)
    @data(*camera_update_casedatas)
    @unpack
    def test_2camera_update(self,head,username,password,choose,ele,values,
                          element,assertion,result):
        self.camera_update(head,username,password,choose,ele,values)
        self.assertEqual(self.assert_text_zong(OperaPage_Login.login_assert,element),assertion)
        self.log_zong(result)

    camera_find_datas = get_zong_xls(camera_list_values,camera_list_find)
    camera_find_casedatas = list(camera_find_datas)
    @data(*camera_find_casedatas)
    @unpack
    def test_3camera_find(self,head,username,password,ele,values,element,assertion,result,
                        reset_enement,reset_assertion,reset_result):
        self.camera_find_search(head,username,password,ele,values)
        self.assertEqual(self.assert_text_zong(OperaPage_Login.login_assert,element),assertion)
        self.log_zong(result)
        self.camera_find_reset()
        self.assertEqual(self.assert_text_zong(OperaPage_Login.login_assert,reset_enement),reset_assertion)
        self.log_zong(reset_result)

    camera_del_datas = get_zong_xls(camera_list_values,camera_list_del)
    camera_del_casedatas = list(camera_del_datas)
    @data(*camera_del_casedatas)
    @unpack
    def test_4camera_del(self,head,username,password,element,assertion,result):
        self.camera_delete(head,username,password)
        self.assertEqual(self.assert_text_zong(OperaPage_Login.login_assert,element),assertion)
        self.log_zong(result)

    def tearDown(self):
        self.driver.quit()

@ddt#显示屏
class TestCase_DisplayTest(unittest.TestCase,Display_Zong,):

    def setUp(self):
        self.opts = webdriver.ChromeOptions()
        self.opts.add_argument('--headless')
        self.opts.add_argument('--window-size=1440,900')
        self.driver = webdriver.Chrome(chrome_options=self.opts)#无头模式
        # self.driver = webdriver.Chrome()
        # self.driver.maximize_window()
        self.driver.get('https://test.ghparking.com/')
        self.driver.implicitly_wait(10)
        self.browser = ZongBrowser(self.driver)

    display_add_datas = get_zong_xls(display_list_values,display_list_add)
    display_add_casedatas = list(display_add_datas)
    @data(*display_add_casedatas)
    @unpack
    def test_1display_add(self,head,username,password,choose,delete,element,assertion,result):
        self.display_add(head,username,password,choose,delete)
        self.assertEqual(self.assert_text_zong(OperaPage_Login.login_assert,element),assertion)
        self.log_zong(result)

    display_update_datas = get_zong_xls(display_list_values,display_list_update)
    display_update_casedatas = list(display_update_datas)
    @data(*display_update_casedatas)
    @unpack
    def test_2display_update(self,head,username,password,element,assertion,result):
        self.display_update(head,username,password)
        self.assertEqual(self.assert_text_zong(OperaPage_Login.login_assert,element),assertion)
        self.log_zong(result)


    display_find_datas = get_zong_xls(display_list_values,display_list_find)
    display_find_casedatas = list(display_find_datas)
    @data(*display_find_casedatas)
    @unpack
    def test_3display_find(self,head,username,password,values,element,assertion,result,
                         reset_element,reset_assertion,reset_result):
        self.display_find_search(head,username,password,values)
        self.assertEqual(self.assert_text_zong(OperaPage_Login.login_assert,element),assertion)
        self.log_zong(result)
        self.display_find_reset()
        self.assertEqual(self.assert_text_zong(OperaPage_Login.login_assert,reset_element),reset_assertion)
        self.log_zong(reset_result)

    display_del_datas = get_zong_xls(display_list_values,display_list_del)
    display_del_casedatas = list(display_del_datas)
    @data(*display_del_casedatas)
    @unpack
    def test_4display_del(self,head,username,password,element,assertion,result):
        self.display_delete(head,username,password)
        self.assertEqual(self.assert_text_zong(OperaPage_Login.login_assert,element),assertion)
        self.log_zong(result)

    def tearDown(self):
        self.driver.quit()
'''
@ddt
class TestCase_Charge_TemporaryTest(unittest.TestCase,Charge_Temporary_Zong):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://test.ghparking.com/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        self.browser = ZongBrowser(self.driver)

    def testcharge_temporary_add(self):
        pass

    def testcharge_temporary_update(self):
        pass

    def testcharge_temporary_find(self):
        pass

    def testcharge_temporary_del(self):
        pass

    def tearDown(self):
        self.driver.quit()
'''
@ddt#vip套餐
class TestCase_Charge_VIPTest(unittest.TestCase,Charge_VIP_Zong):

    def setUp(self):
        self.opts = webdriver.ChromeOptions()
        self.opts.add_argument('--headless')
        self.opts.add_argument('--window-size=1440,900')
        self.driver = webdriver.Chrome(chrome_options=self.opts)#无头模式
        # self.driver = webdriver.Chrome()
        # self.driver.maximize_window()
        self.driver.get('https://test.ghparking.com/')
        self.driver.implicitly_wait(10)
        self.browser = ZongBrowser(self.driver)

    charge_vip_add_datas = get_zong_xls(charge_vip_list_values,charge_vip_list_add)
    charge_vip_add_casedatas = list(charge_vip_add_datas)
    @data(*charge_vip_add_casedatas)
    @unpack
    def test_1charge_vip_add(self,head,username,password,choose,car_type,vip_name,charge_money,
                           explain,element,assertion,result):
        self.charge_vip_add(head,username,password,choose,car_type,vip_name,charge_money,explain)
        self.assertEqual(self.assert_text_zong(OperaPage_Login.login_assert,element),assertion)
        self.log_zong(result)

    charge_vip_update_datas = get_zong_xls(charge_vip_list_values,charge_vip_list_update)
    charge_vip_update_casedatas = list(charge_vip_update_datas)
    @data(*charge_vip_update_casedatas)
    @unpack
    def test_2charge_vip_update(self,head,username,password,delete,ele,values,element,assertion,result):
        self.charge_vip_update(head,username,password,delete,ele,values)
        self.assertEqual(self.assert_text_zong(OperaPage_Login.login_assert,element),assertion)
        self.log_zong(result)

    charge_vip_find_datas = get_zong_xls(charge_vip_list_values,charge_vip_list_find)
    charge_vip_find_casedatas = list(charge_vip_find_datas)
    @data(*charge_vip_find_casedatas)
    @unpack
    def test_3charge_vip_find(self,head,username,password,values,element,assertion,result,
                            reset_element,reset_assertion,reset_result):
        self.charge_vip_find_search(head,username,password,values)
        self.assertEqual(self.assert_text_zong(OperaPage_Login.login_assert,element),assertion)
        self.log_zong(result)
        self.charge_vip_find_reset()
        self.assertEqual(self.assert_text_zong(OperaPage_Login.login_assert,reset_element),reset_assertion)
        self.log_zong(reset_result)

    charge_vip_del_datas = get_zong_xls(charge_vip_list_values,charge_vip_list_del)
    charge_vip_del_casedatas = list(charge_vip_del_datas)
    @data(*charge_vip_del_casedatas)
    @unpack
    def test_4charge_vip_del(self,head,username,password,values,element,assertion,result):
        self.charge_vip_del(head,username,password,values)
        self.assertEqual(self.assert_text_zong(OperaPage_Login.login_assert,element),assertion)
        self.log_zong(result)

    def tearDown(self):
        self.driver.quit()

@ddt#会员车服务
class TestCase_Service_Member(unittest.TestCase,Service_Member_Zong):

    def setUp(self):
        self.opts = webdriver.ChromeOptions()
        self.opts.add_argument('--headless')
        self.opts.add_argument('--window-size=1440,900')
        self.driver = webdriver.Chrome(chrome_options=self.opts)#无头模式
        # self.driver = webdriver.Chrome()
        # self.driver.maximize_window()
        self.driver.get('https://test.ghparking.com/')
        self.driver.implicitly_wait(10)
        self.browser = ZongBrowser(self.driver)

    service_member_add_datas = get_zong_xls(service_member_list_values,service_member_list_add)
    service_member_add_casedatas = list(service_member_add_datas)
    @data(*service_member_add_casedatas)
    @unpack
    def test_1service_member_add(self,head,username,password,choose,car_owner_name,phone,plate,
                                 effective_data_value,effective_time_value,cut_data_value,cut_time_value,
                                 reality_money,explain,element,assertion,result):
        self.service_member_add(head,username,password,choose,car_owner_name,phone,plate,
                                effective_data_value,effective_time_value,cut_data_value,
                                cut_time_value,reality_money,explain)
        self.assertEqual(self.assert_text_zong(OperaPage_Login.login_assert,element),assertion)
        self.log_zong(result)

    service_member_update_datas = get_zong_xls(service_member_list_values,service_member_list_update)
    service_member_update_casedatas = list(service_member_update_datas)
    @data(*service_member_update_casedatas)
    @unpack
    def test_2service_member_update(self,head,username,password,plate,phone,element,assertion,result):
        self.service_member_update(head,username,password,plate,phone)
        self.assertEqual(self.assert_text_zong(OperaPage_Login.login_assert,element),assertion)
        self.log_zong(result)

    service_member_find_datas = get_zong_xls(service_member_list_values,service_member_list_find)
    service_member_find_casedatas = list(service_member_find_datas)
    @data(*service_member_find_casedatas)
    @unpack
    def test_3service_member_find(self,head,username,password,ele,values,element,assertion,result,
                                  reset_element,reset_result):
        self.service_member_find_search(head,username,password,ele,values)
        self.assertEqual(self.assert_text_zong(OperaPage_Login.login_assert,element),assertion)
        self.log_zong(result)
        self.service_member_find_reset()
        self.assertEqual(len(self.assert_amoun_zong(OperaPage_Login.login_assert,reset_element)),10)
        self.log_zong(reset_result)

    service_member_import_datas = get_zong_xls(service_member_list_values,service_member_list_import)
    service_member_import_casedatas = list(service_member_import_datas)
    @data(*service_member_import_casedatas)
    @unpack
    def test_4service_member_import(self,head,username,password,element,assertion,result):
        self.service_member_import(head,username,password)
        self.assertEqual(self.assert_text_zong(OperaPage_Login.login_assert,element),assertion)
        self.log_zong(result)

    service_member_del_datas = get_zong_xls(service_member_list_values,service_member_list_del)
    service_member_del_casedatas = list(service_member_del_datas)
    @data(*service_member_del_casedatas)
    @unpack
    def test_5service_member_del(self,head,username,password,element,assertion,result):
        self.service_member_del(head,username,password)
        self.assertEqual(self.assert_text_zong(OperaPage_Login.login_assert,element),assertion)
        self.log_zong(result)

    def tearDown(self):
            self.driver.quit()

@ddt#贵宾车
class TestCase_Service_VIP(unittest.TestCase,Service_VIP_Zong):

    def setUp(self):
        self.opts = webdriver.ChromeOptions()
        self.opts.add_argument('--headless')
        self.opts.add_argument('--window-size=1440,900')
        self.driver = webdriver.Chrome(chrome_options=self.opts)#无头模式
        # self.driver = webdriver.Chrome()
        # self.driver.maximize_window()
        self.driver.get('https://test.ghparking.com/')
        self.driver.implicitly_wait(10)
        self.browser = ZongBrowser(self.driver)

    service_vip_add_datas = get_zong_xls(service_vip_list_values,service_vip_list_add)
    service_vip_add_casedatas = list(service_vip_add_datas)
    @data(*service_vip_add_casedatas)
    @unpack
    def test_1service_vip_add(self,head,username,password,choose,plate,name,phone,date,time,explain,
                              element,assertion,result):
        self.service_vip_add(head,username,password,choose,plate,name,phone,date,time,explain)
        self.assertEqual(self.assert_text_zong(OperaPage_Login.login_assert,element),assertion)
        self.log_zong(result)

    service_vip_update_datas = get_zong_xls(service_vip_list_values,service_vip_list_update)
    service_vip_update_casedatas = list(service_vip_update_datas)
    @data(*service_vip_update_casedatas)
    @unpack
    def test_2service_vip_update(self,head,username,password,phone,element,assertion,result):
        self.service_vip_update(head,username,password,phone)
        self.assertEqual(self.assert_text_zong(OperaPage_Login.login_assert,element),assertion)
        self.log_zong(result)

    service_vip_find_datas = get_zong_xls(service_vip_list_values,service_vip_list_find)
    service_vip_find_casedatas = list(service_vip_find_datas)
    @data(*service_vip_find_casedatas)
    @unpack
    def test_3service_vip_find(self,head,username,password,value,element,assertion,result,
                               reset_element,reset_result):
        self.service_vip_find_search(head,username,password,value)
        self.assertEqual(self.assert_text_zong(OperaPage_Login.login_assert,element),assertion)
        self.log_zong(result)
        self.service_vip_find_reset()
        self.assertGreater(len(self.assert_amoun_zong(OperaPage_Login.login_assert,reset_element)),2)
        self.log_zong(reset_result)

    service_vip_import_datas = get_zong_xls(service_vip_list_values,service_vip_list_import)
    service_vip_import_casedatas = list(service_vip_import_datas)
    @data(*service_vip_import_casedatas)
    @unpack
    def test_4service_vip_import(self,head,username,password,element,assertion,result):
        self.service_vip_import(head,username,password)
        self.assertEqual(self.assert_text_zong(OperaPage_Login.login_assert,element),assertion)
        self.log_zong(result)

    service_vip_del_datas = get_zong_xls(service_vip_list_values,service_vip_list_del)
    service_vip_del_casedatas = list(service_vip_del_datas)
    @data(*service_vip_del_casedatas)
    @unpack
    def test_5service_vip_del(self,head,username,password,element,assertion,result):
        self.service_vip_del(head,username,password)
        self.assertEqual(self.assert_text_zong(OperaPage_Login.login_assert,element),assertion)
        self.log_zong(result)

    def tearDown(self):
            self.driver.quit()

@ddt#优惠券充值
class TestCase_Discounts_List(unittest.TestCase,Discounts_List_Zong):

    def setUp(self):
        self.opts = webdriver.ChromeOptions()
        self.opts.add_argument('--headless')
        self.opts.add_argument('--window-size=1440,900')
        self.driver = webdriver.Chrome(chrome_options=self.opts)#无头模式
        # self.driver = webdriver.Chrome()
        # self.driver.maximize_window()
        self.driver.get('https://test.ghparking.com/')
        self.driver.implicitly_wait(10)
        self.browser = ZongBrowser(self.driver)

    discount_list_add_datas = get_zong_xls(discount_list_list_values,discount_list_list_add)
    discount_list_add_casedatas = list(discount_list_add_datas)
    @data(*discount_list_add_casedatas)
    @unpack
    def test_1discount_list_add(self,head,username,password,name,choose,park_choose,type_choose,type_value,money,
                                unit,distribute_unit_choose,distribute_value,ues_unit_choose,use_value,
                                element,assertion,result):
        self.discount_list_add(head,username,password,name,choose,park_choose,type_choose,type_value,money,
                               unit,distribute_unit_choose,distribute_value,ues_unit_choose,use_value)
        self.assertEqual(self.assert_text_zong(OperaPage_Login.login_assert,element),assertion)
        self.log_zong(result)

    discount_list_recharge_datas = get_zong_xls(discount_list_list_values,discount_list_list_recharge)
    discount_list_recharge_casedatas = list(discount_list_recharge_datas)
    @data(*discount_list_recharge_casedatas)
    @unpack
    def test_2discount_list_recharge(self,head,username,password,choose,amount,money,
                                     element,assertion,result):
            self.discount_list_recharge(head,username,password,choose,amount,money)
            self.assertEqual(self.assert_text_zong(OperaPage_Login.login_assert,element),assertion)
            self.log_zong(result)

    discount_list_find_datas = get_zong_xls(discount_list_list_values,discount_list_list_find)
    discount_list_find_casedatas = list(discount_list_find_datas)
    @data(*discount_list_find_casedatas)
    @unpack
    def test_3discount_list_find(self,head,username,password,ele,value,element,assertion,result,
                                 reset_element,reset_result):
        self.discount_list_find_search(head,username,password,ele,value)
        self.assertEqual(self.assert_text_zong(OperaPage_Login.login_assert,element),assertion)
        self.log_zong(result)
        self.discount_list_find_reset()
        self.assertGreater(len(self.assert_amoun_zong(OperaPage_Login.login_assert,reset_element)),4)
        self.log_zong(reset_result)

    discount_list_del_datas = get_zong_xls(discount_list_list_values,discount_list_list_del)
    discount_list_del_casedatas = list(discount_list_del_datas)
    @data(*discount_list_del_casedatas)
    @unpack
    def test_4discount_list_del(self,head,username,password,element,assertion,result):
        self.discount_list_del(head,username,password)
        self.assertEqual(self.assert_text_zong(OperaPage_Login.login_assert,element),assertion)
        self.log_zong(result)


    def tearDown(self):
        self.driver.quit()

@ddt#黑名单
class TestCase_blacklist(unittest.TestCase,BlackList):

    def setUp(self):
         # self.opts = webdriver.ChromeOptions()
        # self.opts.add_argument('--headless')
        # self.opts.add_argument('--window-size=1440,900')
        # self.driver = webdriver.Chrome(chrome_options=self.opts)
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://test.ghparking.com/')
        self.driver.implicitly_wait(10)
        self.browser = ZongBrowser(self.driver)

    blacklist_add_datas = get_zong_xls(blacklist_values,blacklist_add)
    blacklist_add_casedatas = list(blacklist_add_datas)
    @data(*blacklist_add_casedatas)
    @unpack
    def test_01add(self,head,username,password,choose,path,plate,remarks,element,assertion,result):
        self.login_blacklisr(head,username,password)
        self.blacklist_add(choose,path,plate,remarks)
        self.assertEqual(self.assert_text_zong(OperaPage_Login.login_assert,element),assertion)
        self.log_zong(result)

    blacklist_import_datas = get_zong_xls(blacklist_values,blacklist_import)
    blacklist_import_casedatas = list(blacklist_import_datas)
    @data(*blacklist_import_casedatas)
    @unpack
    def test_02import(self,head,username,password,choose,path,element,assertion,result):
        self.login_blacklisr(head,username,password)
        self.blacklist_import(choose,path)
        self.assertEqual(self.assert_text_zong(OperaPage_Login.login_assert,element),assertion)
        self.log_zong(result)

    blacklist_find_datas = get_zong_xls(blacklist_values,blacklist_find)
    blacklist_find_casedatas = list(blacklist_find_datas)
    @data(*blacklist_find_casedatas)
    @unpack
    def test_03find(self,head,username,password,choose,path,plate,element,assertion,result,reset_element,
                    reset_assertion,reset_result):
        self.login_blacklisr(head,username,password)
        self.blacklist_find_search(choose,path,plate)
        self.assertIn(assertion,self.assert_text_zong(OperaPage_Login.login_assert,element))
        self.log_zong(result)
        self.blacklist_find_reset()
        self.assertGreater(len(self.assert_amoun_zong(OperaPage_Login.login_assert,reset_element)),reset_assertion)
        self.log_zong(reset_result)

    blacklist_del_datas = get_zong_xls(blacklist_values,blacklist_del)
    blacklist_del_casedatas = list(blacklist_del_datas)
    @data(*blacklist_del_casedatas)
    @unpack
    def test_04del(self,head,username,password,ele,element,assertion,result):
        self.login_blacklisr(head,username,password)
        self.blacklist_del(ele)
        self.assertEqual(self.assert_text_zong(OperaPage_Login.login_assert,element),assertion)
        self.log_zong(result)

    def tearDown(self):
        self.driver.quit()

@ddt#标识配置
class TestCase_system_tag(unittest.TestCase,Set_Tag):

    def setUp(self):
        # self.opts = webdriver.ChromeOptions()
        # self.opts.add_argument('--headless')
        # self.opts.add_argument('--window-size=1440,900')
        # self.driver = webdriver.Chrome(chrome_options=self.opts)
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://test.ghparking.com/')
        self.driver.implicitly_wait(10)
        self.browser = ZongBrowser(self.driver)

    tag_update_datas = get_zong_xls(tag_list_values,tag_list_update)
    tag_update_casedatas = list(tag_update_datas)
    @data(*tag_update_casedatas)
    @unpack
    def test_01tag(self,head,username,password,platefrom_name,data_name,
                      platefrom_element,platefrom_assertion,data_element,
                      data_assertion,result):
        self.login_tag(head,username,password)
        self.tag_update(platefrom_name,data_name)
        self.assertTrue(self.wait_until_title(platefrom_name),platefrom_assertion)
        self.assertEqual(self.assert_text_zong(OperaPage_Login.login_assert,platefrom_element),platefrom_assertion)
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://test.ghparking.com/bigdata/#/')
        self.dade_login_zonglogin(username,password)
        self.assertTrue(self.wait_until_title(data_name),data_assertion)
        self.assertEqual(self.assert_text_zong(OperaPage_Login.login_assert,data_element),data_assertion)
        self.log_zong(result)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    zong_list = [TestCase_blacklist]
    # zong_list = [TestCase_Login_groupTest,TestCase_OwnerTest,TestCase_ShopTest,TestCase_PlatformTest,
    #              TestCase_PatrolTest]

    for i in zong_list:
        cases = loader.loadTestsFromTestCase(i)
        suite.addTest(cases)
    runner = HTMLTestRunner(stream=open('login_report.html','wb'),
                   verbosity=2,
                   title='纵停车自动化测试报告',
                   description='纵停车基础功能测试',
                   tester='谢港')
    runner.run(suite)