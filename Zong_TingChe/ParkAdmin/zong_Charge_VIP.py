from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Zong_TingChe.Zongoperationpage import OperaPage_Login
from time import sleep
import random


class Charge_VIP_Zong(OperaPage_Login):

    parkadmin = (By.XPATH,'//div/ul/div[4]/li/div/span')
    chargealloca = (By.XPATH,'//div/ul/div[4]/li/ul/div[3]/a/li/span')
    vip = (By.XPATH,'//div/div[1]/ul/li[1]/span[text()="VIP"]')
    #新增VIP套餐
    vipadd = (By.XPATH,'//div/div[2]/div[2]/div[1]/div[1]/button/span/span')
    vipadd_park = (By.XPATH,'//form/div[1]/div/div/div/div/div/input')
    vipadd_park_choose = (By.XPATH,'//div[1]/div[1]/ul/li/span[text()="测试车场"]')
    vipadd_region_not_limit = (By.XPATH,'//form/div[2]/div/div/div/div[1]/label[1]/span[1]/span')
    vipadd_region_outer = (By.XPATH,'//form/div[2]/div/div/div/div[1]/label[2]/span[1]/span')
    vipadd_region_within = (By.XPATH,'//form/div[2]/div/div/div/div[1]/label[3]/span[1]/span')
    vipadd_duration = (By.XPATH,'//form/div[3]/div[2]/div/div/div/div/input')
    vipadd_duration_choose = (By.XPATH,'//div[1]/div[1]/ul/li/span[text()="30天月租套餐"]')
    vipadd_name = (By.XPATH,'//form/div[3]/div[1]/div/div/div/input')
    vipadd_car_type = (By.XPATH,'//form/div[4]/div[1]/div/div/div/div/input')
    vipadd_car_type_choose_small = (By.XPATH,'//div[1]/div[1]/ul/li/span[text()="小车"]')
    vipadd_car_type_choose_big = (By.XPATH,'//div[1]/div[1]/ul/li/span[text()="大车"]')
    vipadd_charge_money = (By.XPATH,'//form/div[5]/div/div/div/div/input')
    vipadd_start = (By.XPATH,'//form/div[6]/div/div/div/div/div[1]/input')
    vipadd_start_choose = (By.XPATH,'//div[1]/div[1]/ul/li/span[text()="正常"]')
    vipadd_explain = (By.XPATH,'//form/div[7]/div/div/div/div/textarea')
    vipadd_confirm = (By.XPATH,'//div/div[3]/div/button[1]/span')
    #修改VIP套餐
    vipupdate = (By.XPATH,'//table/tbody/tr[1]/td[9]/div/button[1]/span')
    vipupdate_name = (By.XPATH,'//form/div[3]/div[1]/div/div/div/input')
    vipupdate_charge_money = (By.XPATH,'//form/div[5]/div/div/div/div/input')
    vipupdate_confirm = (By.XPATH,'//div/div[3]/div/button[1]/span')
    #查询VIP套餐
    vipfind_park = (By.XPATH,'//form/div[1]/div/div/input')
    vipfind_search = (By.XPATH,'//form/div[2]/div/button[1]/span')
    vipfind_reset = (By.XPATH,'//form/div[2]/div/button[2]/span')
    #删除VIP套餐
    vipdel_choose = (By.XPATH,'//table/thead/tr[1]/th[1]/div/label/span/span')
    vipdel_del = (By.XPATH,'//div/div[2]/div[2]/div[1]/div[2]/button/span/span')
    vipdel_confirm = (By.XPATH,'//div/div[3]/button[2]/span')

    def park_charge_vip(self):
        try:
            self.click_script_zong(OperaPage_Login.shrink)
        except:
            pass
        self.click_script_zong(Charge_VIP_Zong.parkadmin)
        self.click_script_zong(Charge_VIP_Zong.chargealloca)
        self.click_zong(Charge_VIP_Zong.vip)

    def login_charge_vip(self,head,username,password):
        self.log_zong(head)
        self.login_zonglogin(username,password)
        self.park_charge_vip()

    def charge_vip_add(self,head,username,password,choose,car_type,vip_name,charge_money,explain):
        self.login_charge_vip(head,username,password)
        self.click_zong(Charge_VIP_Zong.vipadd)
        if choose == 'one':
            self.click_zong(Charge_VIP_Zong.vipadd_park)
            self.click_zong(Charge_VIP_Zong.vipadd_park_choose)
            self.click_zong(Charge_VIP_Zong.vipadd_region_not_limit)
            self.click_zong(Charge_VIP_Zong.vipadd_duration)
            self.click_zong(Charge_VIP_Zong.vipadd_duration_choose)
            self.send_key_zong(Charge_VIP_Zong.vipadd_name,vip_name)
            self.click_zong(Charge_VIP_Zong.vipadd_car_type)
            if car_type == 'small':
                self.click_zong(Charge_VIP_Zong.vipadd_car_type_choose_small)
            elif car_type == 'big':
                self.click_zong(Charge_VIP_Zong.vipadd_car_type_choose_big)
            self.send_key_zong(Charge_VIP_Zong.vipadd_charge_money,charge_money)
            self.click_zong(Charge_VIP_Zong.vipadd_start)
            self.click_zong(Charge_VIP_Zong.vipadd_start_choose)
            self.send_key_zong(Charge_VIP_Zong.vipadd_explain,explain)
        elif choose == 'two':
            self.click_zong(Charge_VIP_Zong.vipadd_duration)
            self.click_zong(Charge_VIP_Zong.vipadd_duration_choose)
            self.send_key_zong(Charge_VIP_Zong.vipadd_name,vip_name)
            self.send_key_zong(Charge_VIP_Zong.vipadd_charge_money,charge_money)
            self.click_zong(Charge_VIP_Zong.vipadd_start)
            self.click_zong(Charge_VIP_Zong.vipadd_start_choose)
            self.send_key_zong(Charge_VIP_Zong.vipadd_explain,explain)
        elif choose == 'three':
            self.click_zong(Charge_VIP_Zong.vipadd_park)
            self.click_zong(Charge_VIP_Zong.vipadd_park_choose)
            self.click_zong(Charge_VIP_Zong.vipadd_duration)
            self.click_zong(Charge_VIP_Zong.vipadd_duration_choose)
            self.send_key_zong(Charge_VIP_Zong.vipadd_name,vip_name)
            self.click_zong(Charge_VIP_Zong.vipadd_car_type)
            if car_type == 'small':
                self.click_zong(Charge_VIP_Zong.vipadd_car_type_choose_small)
            elif car_type == 'big':
                self.click_zong(Charge_VIP_Zong.vipadd_car_type_choose_big)
            self.send_key_zong(Charge_VIP_Zong.vipadd_charge_money,charge_money)
            self.click_zong(Charge_VIP_Zong.vipadd_start)
            self.click_zong(Charge_VIP_Zong.vipadd_start_choose)
            self.send_key_zong(Charge_VIP_Zong.vipadd_explain,explain)
        elif choose == 'four':
            self.click_zong(Charge_VIP_Zong.vipadd_park)
            self.click_zong(Charge_VIP_Zong.vipadd_park_choose)
            self.click_zong(Charge_VIP_Zong.vipadd_region_not_limit)
            self.send_key_zong(Charge_VIP_Zong.vipadd_name,vip_name)
            self.click_zong(Charge_VIP_Zong.vipadd_car_type)
            if car_type == 'small':
                self.click_zong(Charge_VIP_Zong.vipadd_car_type_choose_small)
            elif car_type == 'big':
                self.click_zong(Charge_VIP_Zong.vipadd_car_type_choose_big)
            self.send_key_zong(Charge_VIP_Zong.vipadd_charge_money,charge_money)
            self.click_zong(Charge_VIP_Zong.vipadd_start)
            self.click_zong(Charge_VIP_Zong.vipadd_start_choose)
            self.send_key_zong(Charge_VIP_Zong.vipadd_explain,explain)
        elif choose == 'five':
            self.click_zong(Charge_VIP_Zong.vipadd_park)
            self.click_zong(Charge_VIP_Zong.vipadd_park_choose)
            self.click_zong(Charge_VIP_Zong.vipadd_region_not_limit)
            self.send_key_zong(Charge_VIP_Zong.vipadd_name,vip_name)
            self.send_key_zong(Charge_VIP_Zong.vipadd_charge_money,charge_money)
            self.click_zong(Charge_VIP_Zong.vipadd_start)
            self.click_zong(Charge_VIP_Zong.vipadd_start_choose)
            self.send_key_zong(Charge_VIP_Zong.vipadd_explain,explain)
        elif choose == '':
            self.click_zong(Charge_VIP_Zong.vipadd_park)
            self.click_zong(Charge_VIP_Zong.vipadd_park_choose)
            self.click_zong(Charge_VIP_Zong.vipadd_region_not_limit)
            self.click_zong(Charge_VIP_Zong.vipadd_duration)
            self.click_zong(Charge_VIP_Zong.vipadd_duration_choose)
            self.send_key_zong(Charge_VIP_Zong.vipadd_name,vip_name)
            self.click_zong(Charge_VIP_Zong.vipadd_car_type)
            if car_type == 'small':
                self.click_zong(Charge_VIP_Zong.vipadd_car_type_choose_small)
            elif car_type == 'big':
                self.click_zong(Charge_VIP_Zong.vipadd_car_type_choose_big)
            self.send_key_zong(Charge_VIP_Zong.vipadd_charge_money,charge_money)
            self.send_key_zong(Charge_VIP_Zong.vipadd_explain,explain)
        self.click_zong(Charge_VIP_Zong.vipadd_confirm)
    def charge_vip_update(self,head,username,password,delete,ele,values):
        self.login_charge_vip(head,username,password)
        self.click_zong(Charge_VIP_Zong.vipupdate)
        charge_vip_redact = (By.XPATH,ele)
        self.send_key_zong(charge_vip_redact,Keys.CONTROL,'a')
        self.send_key_zong(charge_vip_redact,Keys.BACK_SPACE)
        if delete == 'N':
            self.send_key_zong(charge_vip_redact,values)
        elif delete == 'Y':
            pass
        self.click_zong(Charge_VIP_Zong.vipupdate_confirm)

    def charge_vip_find_search(self,head,username,password,values):
        self.login_charge_vip(head,username,password)
        self.send_key_zong(Charge_VIP_Zong.vipfind_park,values)
        self.click_zong(Charge_VIP_Zong.vipfind_search)

    def charge_vip_find_reset(self):
        self.click_zong(Charge_VIP_Zong.vipfind_reset)

    def charge_vip_del(self,head,username,password,values):
        self.charge_vip_find_search(head,username,password,values)
        self.click_zong(Charge_VIP_Zong.vipdel_choose)
        self.click_zong(Charge_VIP_Zong.vipdel_del)
        self.click_zong(Charge_VIP_Zong.vipdel_confirm)