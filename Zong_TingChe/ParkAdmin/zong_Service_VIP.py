from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Zong_TingChe.Zongoperationpage import OperaPage_Login
from time import sleep
from pywinauto import Desktop
from pywinauto.keyboard import send_keys
import random


class Service_VIP_Zong(OperaPage_Login):

    parkadmin = (By.XPATH,'//div/ul/div[4]/li/div/span')
    servicecar = (By.XPATH,'//div/ul/div[4]/li/ul/div[5]/a/li/span')
    vipcar = (By.XPATH,'//section/div/div[1]/ul/li[3]/span')
    #新增贵宾车
    vipadd = (By.XPATH,'//div/div[2]/div[2]/div[1]/div[1]/button/span/span')
    vipadd_park = (By.XPATH,'//form/div[1]/div[1]/div/div/div/div/input')
    vipadd_park_choose = (By.XPATH,'//div[1]/div[1]/ul/li/span[text()="自动化测试车场"]')
    vipadd_plate = (By.XPATH,'//form/div[1]/div[2]/div/div/div/input')
    vipadd_name = (By.XPATH,'//form/div[2]/div[1]/div/div/div/input')
    vipadd_phone = (By.XPATH,'//form/div[2]/div[2]/div/div/div/input')
    vipadd_time = (By.XPATH,'//form/div[3]/div/div/div/div/input')
    vipadd_data_choose = (By.XPATH,'//div[1]/div/div[1]/span[1]/div/input')
    vipadd_time_choose = (By.XPATH,'//div[1]/div/div[1]/span[2]/div[1]/input')
    vipadd_time_choose_confirm = (By.XPATH,'//span[2]/div[2]/div[2]/button[2]')
    vipadd_time_confirm = (By.XPATH,'//div[2]/button[2]/span')
    vipadd_explain = (By.XPATH,'//form/div[4]/div/div/div/div/textarea')
    vipadd_confirm = (By.XPATH,'//div/div[3]/div/button[1]/span')
    #修改贵宾车
    vipupdate = (By.XPATH,'//table/tbody/tr[1]/td[9]/div/button[1]/span')
    vipupdate_phone = (By.XPATH,'//form/div[2]/div/div/div/input')
    vipupdate_confirm = (By.XPATH,'//div/div[3]/div/button[1]/span')
    #查询贵宾车
    vipfind_park = (By.XPATH,'//form/div[1]/div/div/div[1]/input')
    vipfind_park_choose = (By.XPATH,'//div[1]/div[1]/ul/li/span[text()="吴忠测试车场"]')
    vipfind_plate = (By.XPATH,'//form/div[2]/div/div/input')
    vipfind_search = (By.XPATH,'//form/div[3]/div/button[1]/span')
    vipfind_reset = (By.XPATH,'//form/div[3]/div/button[2]/span')
    #导入贵宾车
    vipimport = (By.XPATH,'//div/div[2]/div[2]/div[1]/div[3]/button/span/span')
    vipimport_park = (By.XPATH,'//form/div[1]/div/div/div[1]/input')
    vipimport_park_choose = (By.XPATH,'//div[1]/div[1]/ul/li/span[text()="自动化测试车场"]')
    vipimport_file_choose = (By.XPATH,'//form/div[2]/div/div/div/button/span')
    #vip_file = r'F:\2020\untitled\Zong_TingChe\plateImportTemplate.xlsx'
    vipimport_confirm = (By.XPATH,'//div/div[3]/div/button[1]/span')
    #删除贵宾车
    vipdel_choose = (By.XPATH,'//table/thead/tr/th[1]/div/label/span/span')
    vipdel_del = (By.XPATH,'//div/div[2]/div[2]/div[1]/div[2]/button/span/span')
    vipdel_confirm = (By.XPATH,'//div/div[3]/button[2]/span')

    def park_service_vip(self):
        try:
            self.click_script_zong(OperaPage_Login.shrink)
        except:
            pass
        self.click_script_zong(Service_VIP_Zong.parkadmin)
        self.click_script_zong(Service_VIP_Zong.servicecar)
        self.click_zong(Service_VIP_Zong.vipcar)

    def login_service_vip(self,head,username,password):
        self.log_zong(head)
        self.login_zonglogin(username,password)
        self.park_service_vip()

    def service_vip_add(self,head,username,password,choose,plate,name,phone,date,time,explain):
        self.login_service_vip(head,username,password)
        self.click_zong(Service_VIP_Zong.vipadd)
        if choose == 'one':
            self.click_zong(Service_VIP_Zong.vipadd_park)
            self.click_eles_presence_zong(Service_VIP_Zong.vipadd_park_choose,-1)
            self.click_zong(Service_VIP_Zong.vipadd_time)
            self.send_key_zong(Service_VIP_Zong.vipadd_data_choose,date)
            self.click_zong(Service_VIP_Zong.vipadd_time_choose)
            self.send_key_zong(Service_VIP_Zong.vipadd_time_choose,Keys.CONTROL,'a')
            self.send_key_zong(Service_VIP_Zong.vipadd_time_choose,Keys.BACK_SPACE)
            self.send_key_zong(Service_VIP_Zong.vipadd_time_choose,time)
            self.click_zong(Service_VIP_Zong.vipadd_time_choose_confirm)
            self.click_zong(Service_VIP_Zong.vipadd_time_confirm)
        elif choose == 'two':
            self.click_zong(Service_VIP_Zong.vipadd_time)
            self.send_key_zong(Service_VIP_Zong.vipadd_data_choose,date)
            self.click_zong(Service_VIP_Zong.vipadd_time_choose)
            self.send_key_zong(Service_VIP_Zong.vipadd_time_choose,Keys.CONTROL,'a')
            self.send_key_zong(Service_VIP_Zong.vipadd_time_choose,Keys.BACK_SPACE)
            self.send_key_zong(Service_VIP_Zong.vipadd_time_choose,time)
            self.click_zong(Service_VIP_Zong.vipadd_time_choose_confirm)
            self.click_zong(Service_VIP_Zong.vipadd_time_confirm)
        elif choose == 'three':
            self.click_zong(Service_VIP_Zong.vipadd_park)
            self.click_eles_presence_zong(Service_VIP_Zong.vipadd_park_choose,-1)
        self.send_key_zong(Service_VIP_Zong.vipadd_plate,plate)
        self.send_key_zong(Service_VIP_Zong.vipadd_name,name)
        self.send_key_zong(Service_VIP_Zong.vipadd_phone,phone)
        self.send_key_zong(Service_VIP_Zong.vipadd_explain,explain)
        self.click_zong(Service_VIP_Zong.vipadd_confirm)


    def service_vip_update(self,head,username,password,phone):
        self.login_service_vip(head,username,password)
        self.service_vip_find_park()
        self.click_zong(Service_VIP_Zong.vipfind_search)
        self.click_zong(Service_VIP_Zong.vipupdate)
        self.send_key_zong(Service_VIP_Zong.vipupdate_phone,Keys.CONTROL,'a')
        self.send_key_zong(Service_VIP_Zong.vipupdate_phone,Keys.BACK_SPACE)
        self.send_key_zong(Service_VIP_Zong.vipupdate_phone,phone)
        self.click_eles_presence_zong(Service_VIP_Zong.vipupdate_confirm,-1)

    def service_vip_find_park(self):
        self.click_eles_presence_zong(Service_VIP_Zong.vipfind_park,-1)
        self.click_eles_presence_zong(Service_VIP_Zong.vipfind_park_choose,-1)

    def service_vip_find_search(self,head,username,password,value):
        self.login_service_vip(head,username,password)
        self.service_vip_find_park()
        self.send_key_zong(Service_VIP_Zong.vipfind_plate,value)
        self.click_zong(Service_VIP_Zong.vipfind_search)

    def service_vip_find_reset(self):
        self.click_zong(Service_VIP_Zong.vipfind_reset)
        self.service_vip_find_park()
        self.click_zong(Service_VIP_Zong.vipfind_search)

    def service_vip_import(self,head,username,password):
        self.login_service_vip(head,username,password)
        self.click_zong(Service_VIP_Zong.vipimport)
        self.click_eles_presence_zong(Service_VIP_Zong.vipimport_park,-1)
        sleep(1)
        self.click_eles_presence_zong(Service_VIP_Zong.vipimport_park_choose,-1)
        sleep(1)
        self.click_zong(Service_VIP_Zong.vipimport_file_choose)
        self.file_up(r"F:\servicevip.xlsx")
        sleep(1)
        self.click_eles_presence_zong(Service_VIP_Zong.vipimport_confirm,-1)


    def service_vip_del(self,head,username,password):
        self.login_service_vip(head,username,password)
        self.service_vip_find_park()
        self.click_zong(Service_VIP_Zong.vipfind_search)
        self.click_zong(Service_VIP_Zong.vipdel_choose)
        self.click_zong(Service_VIP_Zong.vipdel_del)
        self.click_zong(Service_VIP_Zong.vipdel_confirm)