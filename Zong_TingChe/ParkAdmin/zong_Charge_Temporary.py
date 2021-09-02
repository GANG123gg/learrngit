from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Zong_TingChe.Zongoperationpage import OperaPage_Login
from time import sleep
import random


class Charge_Temporary_Zong(OperaPage_Login):

    parkadmin = (By.XPATH,'//div/ul/div[4]/li/div/span')
    chargealloca = (By.XPATH,'//div/ul/div[4]/li/ul/div[3]/a/li/span')
    temporary = (By.XPATH,'//div/div[1]/ul/li[3]/span[text()="临时车收费配置"]')

    temporaryadd = (By.XPATH,'//div/div[2]/div[2]/div[1]/div[1]/button/span/span')
    temporaryadd_park = (By.XPATH,'//form/div[1]/div/div/div/div/div[1]/input')
    temporaryadd_park_choose = (By.XPATH,'//div[1]/div[1]/ul/li/span[text()="自动化测试车场"]')
    temporaryadd_charge_type = (By.XPATH,'//form/div[2]/div/div/div/div/div[1]/input')

    #新增单次计费规则
    once_temporaryadd_charge_type_choose = (By.XPATH,'//div[1]/div[1]/ul/li/span[text()="按次"]')
    once_temporaryadd_car_type = (By.XPATH,'//form[1]/div[3]/div/div/div/div/div[1]/input')
    once_temporaryadd_car_type_choose = (By.XPATH,'//div[1]/div[1]/ul/li/span[text()="小车"]')
    once_temporaryadd_free_time = (By.XPATH,'//form/div[4]/div[1]/div/div/div/input')
    once_temporaryadd_money = (By.XPATH,'//form/div[4]/div[2]/div/div/div/input')
    once_temporaryadd_state = (By.XPATH,'//form/div[5]/div/div/div/div/div[1]/input')
    once_temporaryadd_state_choose = (By.XPATH,'//div[1]/div[1]/ul/li/span[text()="正常"]')
    #新增间隔计费规则
    temporaryadd_charge_type_choose = (By.XPATH,'//div[1]/div[1]/ul/li/span[text()="按时间间隔"]')
    temporaryadd_service_type = (By.XPATH,'//form[1]/div[3]/div/div/div/div/div[1]/input')
    temporaryadd_service_type_choose = (By.XPATH,'//div[1]/div[1]/ul/li/span[text()="临时车"]')
    temporaryadd_car_type = (By.XPATH,'//form[1]/div[4]/div[2]/div/div/div/div[1]/input')
    temporaryadd_car_type_choose = (By.XPATH,'//div[1]/div[1]/ul/li/span[text()="小车"]')
    temporaryadd_charge_name = (By.XPATH,'//form[1]/div[4]/div[1]/div/div/div/input')
    temporaryadd_free_time = (By.XPATH,'//form[1]/div[5]/div/div/div/div/input')
    temporaryadd_maximum_limit = (By.XPATH,'//form[1]/div[6]/div[1]/div/div/div/input')
    temporaryadd_once_limit = (By.XPATH,'//form[1]/div[7]/div/div/div/div/input')
    temporaryadd_state = (By.XPATH,'//form[1]/div[6]/div[2]/div/div/div/div[1]/input')
    temporaryadd_state_choose = (By.XPATH,'//div[1]/div[1]/ul/li/span[text()="正常"]')
    temporaryadd_time_add = (By.XPATH,'//form/div[1]/div/div[8]/div/span[1]')
    temporaryadd_one_first_duration = (By.XPATH,'//form/div[1]/div/div[3]/div/div/div/input')
    temporaryadd_one_first_money = (By.XPATH,'//form/div[1]/div/div[4]/div/div/div/input')
    temporaryadd_one_interval_duration = (By.XPATH,'//form/div[1]/div/div[5]/div/div/div/input')
    temporaryadd_one_interval_money = (By.XPATH,'//form/div[1]/div/div[6]/div/div/div/input')
    temporaryadd_one_most_money = (By.XPATH,'//form/div[1]/div/div[7]/div/div/div/input')
    temporaryadd_two_first_duration = (By.XPATH,'//form/div[2]/div/div[3]/div/div/div/input')
    temporaryadd_two_first_money = (By.XPATH,'//form/div[2]/div/div[4]/div/div/div/input')
    temporaryadd_two_interval_duration = (By.XPATH,'//form/div[2]/div/div[5]/div/div/div/input')
    temporaryadd_two_interval_money = (By.XPATH,'//form/div[2]/div/div[6]/div/div/div/input')
    temporaryadd_two_most_money = (By.XPATH,'//form/div[2]/div/div[7]/div/div/div/input')
    temporaryadd_confirm = (By.XPATH,'//div/div[3]/div/button[1]/span')

    def park_charge_temporary(self):
        try:
            self.click_script_zong(OperaPage_Login.shrink)
        except:
            pass
        self.click_script_zong(Charge_Temporary_Zong.parkadmin)
        self.click_script_zong(Charge_Temporary_Zong.chargealloca)
        self.click_zong(Charge_Temporary_Zong.temporary)

    def login_charge_temporary(self,head,username,password):
        self.log_zong(head)
        self.login_zonglogin(username,password)
        self.park_charge_temporary()

    def charge_temporary_add(self,head,username,password,charge_name,free_time,maximum_limit,
                             once_limit,one_first_duration,one_first_money,one_interval_duration,
                             one_interval_money,one_most_money,two_first_duration,two_first_money,
                             two_interval_duration,two_interval_money,two_most_money):
        self.login_charge_temporary(head,username,password)
        self.click_zong(Charge_Temporary_Zong.temporaryadd)
        self.click_zong(Charge_Temporary_Zong.temporaryadd_park)
        self.click_eles_presence_zong(Charge_Temporary_Zong.temporaryadd_park_choose,-1)
        self.click_zong(Charge_Temporary_Zong.temporaryadd_charge_type)
        self.click_zong(Charge_Temporary_Zong.temporaryadd_charge_type_choose)
        self.click_zong(Charge_Temporary_Zong.temporaryadd_service_type)
        self.click_zong(Charge_Temporary_Zong.temporaryadd_service_type_choose)
        self.click_zong(Charge_Temporary_Zong.temporaryadd_car_type)
        self.click_zong(Charge_Temporary_Zong.temporaryadd_car_type_choose)
        self.send_key_zong(Charge_Temporary_Zong.temporaryadd_charge_name,charge_name)
        self.send_key_zong(Charge_Temporary_Zong.temporaryadd_free_time,free_time)
        self.send_key_zong(Charge_Temporary_Zong.temporaryadd_maximum_limit,maximum_limit)
        self.send_key_zong(Charge_Temporary_Zong.temporaryadd_once_limit,once_limit)
        self.click_zong(Charge_Temporary_Zong.temporaryadd_state)
        self.click_zong(Charge_Temporary_Zong.temporaryadd_time_add)
        self.send_key_zong(Charge_Temporary_Zong.temporaryadd_one_first_duration,one_first_duration)
        self.send_key_zong(Charge_Temporary_Zong.temporaryadd_one_first_money,one_first_money)
        self.send_key_zong(Charge_Temporary_Zong.temporaryadd_one_interval_duration,one_interval_duration)
        self.send_key_zong(Charge_Temporary_Zong.temporaryadd_one_interval_money,one_interval_money)
        self.send_key_zong(Charge_Temporary_Zong.temporaryadd_one_most_money,one_most_money)
        self.send_key_zong(Charge_Temporary_Zong.temporaryadd_two_first_duration,two_first_duration)
        self.send_key_zong(Charge_Temporary_Zong.temporaryadd_two_first_money,two_first_money)
        self.send_key_zong(Charge_Temporary_Zong.temporaryadd_two_interval_duration,two_interval_duration)
        self.send_key_zong(Charge_Temporary_Zong.temporaryadd_two_interval_money,two_interval_money)
        self.send_key_zong(Charge_Temporary_Zong.temporaryadd_two_most_money,two_most_money)
        self.click_zong(Charge_Temporary_Zong.temporaryadd_confirm)

    def charge_temporary_update(self):
        pass

    def charge_temporary_find_search(self):
        pass

    def charge_temporary_find_reset(self):
        pass

    def charge_temporary_del(self):
        pass

