from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Zong_TingChe.Zongoperationpage import OperaPage_Login
from time import sleep
import random


class ParkList_Zong(OperaPage_Login):

    parkadmin = (By.XPATH,'//div/ul/div[4]/li/div/span')
    parklist = (By.XPATH,'//div/ul/div[4]/li/ul/div[1]/a/li/span')
    #新增车场
    parkadd = (By.XPATH,'//div/div[1]/div[2]/div[1]/div[1]/button/span/span')
    parkadd_name = (By.XPATH,'//form/div[1]/div[2]/div[1]/div/div/div/input')
    parkadd_region = (By.XPATH,'//form/div[1]/div[2]/div[2]/div/div/div/div[1]/div[1]/div[2]/input')
    parkadd_address = (By.XPATH,'//form/div[1]/div[2]/div[3]/div/div/div/div')
    parkadd_address_one = (By.XPATH,'//div[1]/div[2]/div[2]/span')
    parkadd_address_confirm = (By.XPATH,'//div/div[2]/div[3]/div/div[3]/div/button[1]/span')
    parkadd_owner = (By.XPATH,'//form/div[1]/div[4]/div[1]/div/div/div/div[1]/input')
    parkadd_owner_one = (By.XPATH,'//div[1]/div[1]/ul/li/span[text()="策一"]')
    parkadd_type_one = (By.XPATH,'//div/div[2]/div[1]/div[2]/div[2]/form/div[3]/div[1]/div')
    parkadd_type_two = (By.XPATH,'//div/div[2]/div[1]/div[2]/div[2]/form/div[3]/div[2]/div')
    parkadd_Temporary_car_amount = (By.XPATH,'//form/div[5]/div[2]/div[2]/div/div/div/input')
    parkadd_Temporary_car_surplus = (By.XPATH,'//form/div[5]/div[2]/div[3]/div/div/div/input')
    parkadd_member_car_amount = (By.XPATH,'//form/div[5]/div[2]/div[4]/div/div/div/input')
    parkadd_member_car_surplus = (By.XPATH,'//form/div[5]/div[2]/div[5]/div/div/div/input')
    parkadd_confirm = (By.XPATH,'//div/div[2]/div[2]/button[1]/span')
    #修改车场
    parkupdate = (By.XPATH,'//div/div[1]/div[2]/div[2]/div/div[3]/table/tbody/tr[1]/td[11]/div/button[2]/span')
    parkupdate_confirm = (By.XPATH,'//div/div[2]/div[2]/button[1]/span')
    #查询车场
    parkfind_search = (By.XPATH,'//div/div[1]/div[1]/form/div[4]/div/button[1]/span')
    parkfind_reset = (By.XPATH,'//div/div[1]/div[1]/form/div[4]/div/button[2]/span')

    def parkpark(self):
        try:
            self.click_script_zong(OperaPage_Login.shrink)
        except:
            pass
        self.click_script_zong(ParkList_Zong.parkadmin)
        self.click_script_zong(ParkList_Zong.parklist)

    def login_park(self,head,username,password):
        self.log_zong(head)
        self.login_zonglogin(username,password)
        self.parkpark()

    def park_add_one(self,head,username,password,choose,name,temporary_amount,temporary_surplus,
                     member_amount,member_surplus):
        self.login_park(head,username,password)
        sleep(5)
        self.click_script_zong(ParkList_Zong.parkadd)
        sleep(2)
        self.send_key_zong(ParkList_Zong.parkadd_name,name)
        if choose == 'one':
            self.click_script_zong(ParkList_Zong.parkadd_region)
            self.send_key_zong(ParkList_Zong.parkadd_region,Keys.DOWN,Keys.DOWN,Keys.RIGHT,Keys.DOWN,
                                                             Keys.DOWN,Keys.RIGHT,Keys.DOWN,Keys.ENTER)
            sleep(2)
            self.click_zong(ParkList_Zong.parkadd_address)
            sleep(2)
            self.click_zong(ParkList_Zong.parkadd_address_one)
            sleep(2)
            self.click_zong(ParkList_Zong.parkadd_address_confirm)
            self.click_zong(ParkList_Zong.parkadd_owner)
            self.click_zong(ParkList_Zong.parkadd_owner_one)
        elif choose == 'two':
            sleep(1)
            self.click_zong(ParkList_Zong.parkadd_address)
            sleep(1)
            self.click_zong(ParkList_Zong.parkadd_address_one)
            sleep(1)
            self.click_zong(ParkList_Zong.parkadd_address_confirm)
            self.click_zong(ParkList_Zong.parkadd_owner)
            self.click_zong(ParkList_Zong.parkadd_owner_one)
        elif choose == 'three':
            sleep(1)
            self.click_script_zong(ParkList_Zong.parkadd_region)
            self.send_key_zong(ParkList_Zong.parkadd_region,Keys.DOWN,Keys.DOWN,Keys.RIGHT,Keys.DOWN,
                                                             Keys.DOWN,Keys.RIGHT,Keys.DOWN,Keys.ENTER)
            self.click_zong(ParkList_Zong.parkadd_owner)
            self.click_zong(ParkList_Zong.parkadd_owner_one)
        elif choose == 'four':
            self.click_script_zong(ParkList_Zong.parkadd_region)
            self.send_key_zong(ParkList_Zong.parkadd_region,Keys.DOWN,Keys.DOWN,Keys.RIGHT,Keys.DOWN,
                                                             Keys.DOWN,Keys.RIGHT,Keys.DOWN,Keys.ENTER)
            sleep(1)
            self.click_zong(ParkList_Zong.parkadd_address)
            self.click_zong(ParkList_Zong.parkadd_address_one)
            self.click_zong(ParkList_Zong.parkadd_address_confirm)
        self.send_key_zong(ParkList_Zong.parkadd_Temporary_car_amount,temporary_amount)
        self.send_key_zong(ParkList_Zong.parkadd_Temporary_car_surplus,temporary_surplus)
        self.send_key_zong(ParkList_Zong.parkadd_member_car_amount,member_amount)
        self.send_key_zong(ParkList_Zong.parkadd_member_car_surplus,member_surplus)
        self.click_zong(ParkList_Zong.parkadd_confirm)

    def park_update_one(self,head,username,password,ele,choose,values):
        self.login_park(head,username,password)
        sleep(5)
        self.click_zong(ParkList_Zong.parkupdate)
        park_redact = (By.XPATH,ele)
        if choose == 'one':
            self.send_key_zong(park_redact,Keys.CONTROL,'a')
            self.send_key_zong(park_redact,Keys.BACK_SPACE)
        elif choose == 'two':
            self.click_zong(park_redact)
        elif choose == 'three':
            self.send_key_zong(park_redact,Keys.CONTROL,'a')
            self.send_key_zong(park_redact,Keys.BACK_SPACE)
            self.send_key_zong(park_redact,values)
        self.click_zong(ParkList_Zong.parkupdate_confirm)

    def park_find_search(self,head,username,password,ele,values):
        self.login_park(head,username,password)
        sleep(5)
        park_redact = (By.XPATH,ele)
        self.send_key_zong(park_redact,values)
        self.click_zong(ParkList_Zong.parkfind_search)

    def park_find_reset(self):
        self.click_zong(ParkList_Zong.parkfind_reset)
