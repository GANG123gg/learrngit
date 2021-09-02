from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Zong_TingChe.Zongoperationpage import OperaPage_Login
from time import sleep
import random



class Display_Zong(OperaPage_Login):

    parkadmin = (By.XPATH,'//div/ul/div[4]/li/div/span')
    deviceadmin = (By.XPATH,'//div[1]/div[2]/div[1]/div/ul/div[4]/li/ul/div[2]/a/li/span')
    display = (By.XPATH,'//div/div[1]/ul/li/span[text()="显示屏"]')
    #新增显示屏
    displayadd = (By.XPATH,'//div/div[2]/div[2]/div[1]/div[1]/button/span/span')
    displayadd_park = (By.XPATH,'//form/div[2]/div[1]/div[1]/div/div/div/div/input')
    displayadd_park_choose = (By.XPATH,'//div[1]/div[1]/ul/li/span[text()="吴忠测试车场"]')
    displayadd_region = (By.XPATH,'//form/div[2]/div[1]/div[2]/div/div/div/div/input')
    displayadd_region_choose = (By.XPATH,'//div[1]/div[1]/ul/li/span[text()="外区"]')
    displayadd_channel = (By.XPATH,'//form/div[2]/div[2]/div[1]/div/div/div/div/input')
    displayadd_channel_choose = (By.XPATH,'//div[1]/div[1]/ul/li/span[text()="外_1进"]')
    displayadd_type_one = (By.XPATH,'//form/div[2]/div[2]/div[2]/div/div/div/div/input')
    displayadd_type_one_choose = (By.XPATH,'//div[1]/div[1]/ul/li[1]/span[text()="串口屏"]')
    displayadd_type_two = (By.XPATH,'//form/div[2]/div[3]/div[1]/div/div/div/div/input')
    displayadd_type_two_choose = (By.XPATH,'//div[1]/div[1]/ul/li/span[text()="四行横屏"]')
    displayadd_confirm = (By.XPATH,'//div/div[3]/div/button[1]/span')
    #修改显示屏
    displayupdate = (By.XPATH,'//table/tbody/tr[1]/td[8]/div/button[1]/span')
    displayupdate_daytime_volume = (By.XPATH,'//form/div[4]/div[3]/div/div/div/div/input')
    displayupdate_daytime_volume_choose = (By.XPATH,'//div[1]/div[1]/ul/li/span[text()="2"]')
    displayupdate_confirm = (By.XPATH,'//div/div[3]/div/button[1]/span')
    #查询显示屏
    displayfind_park = (By.XPATH,'//form/div[1]/div/div/input')
    displayfind_search = (By.XPATH,'//form/div[3]/div/button[1]/span')
    displayfind_reset = (By.XPATH,'//form/div[3]/div/button[2]/span')
    #删除显示屏
    displaydel_choose = (By.XPATH,'//table/tbody/tr[1]/td[2]/div')
    displaydel_del = (By.XPATH,'//div/div[2]/div[2]/div[1]/div[2]/button/span/span')
    displaydel_confirm = (By.XPATH,'//div/div[3]/button[2]/span')


    def park_display(self):
        try:
            self.click_script_zong(OperaPage_Login.shrink)
        except:
            pass
        self.click_script_zong(Display_Zong.parkadmin)
        self.click_script_zong(Display_Zong.deviceadmin)
        self.click_zong(Display_Zong.display)

    def login_display(self,head,username,password):
        self.log_zong(head)
        self.login_zonglogin(username,password)
        self.park_display()

    def display_add(self,head,username,password,choose,delete):
        self.login_display(head,username,password)
        if delete== 'Y':
            self.display_del()
        elif delete == 'N':
            pass
        self.click_zong(Display_Zong.displayadd)
        if choose == 'one':
            self.click_zong(Display_Zong.displayadd_park)
            self.click_zong(Display_Zong.displayadd_park_choose)
            self.click_zong(Display_Zong.displayadd_region)
            self.click_zong(Display_Zong.displayadd_region_choose)
            self.click_zong(Display_Zong.displayadd_channel)
            self.click_zong(Display_Zong.displayadd_channel_choose)
            self.click_zong(Display_Zong.displayadd_type_one)
            self.send_key_zong(Display_Zong.displayadd_type_one,Keys.DOWN,Keys.ENTER)
            self.click_zong(Display_Zong.displayadd_type_two)
            self.click_zong(Display_Zong.displayadd_type_two_choose)
        elif choose == 'two':
            self.click_zong(Display_Zong.displayadd_park)
            self.click_zong(Display_Zong.displayadd_park_choose)
            self.click_zong(Display_Zong.displayadd_region)
            self.click_zong(Display_Zong.displayadd_region_choose)
            self.click_zong(Display_Zong.displayadd_channel)
            self.click_zong(Display_Zong.displayadd_channel_choose)
            self.click_zong(Display_Zong.displayadd_type_one)
            self.send_key_zong(Display_Zong.displayadd_type_one,Keys.DOWN,Keys.ENTER)
        elif choose == 'three':
            self.click_zong(Display_Zong.displayadd_park)
            self.click_zong(Display_Zong.displayadd_park_choose)
            self.click_zong(Display_Zong.displayadd_region)
            self.click_zong(Display_Zong.displayadd_region_choose)
            self.click_zong(Display_Zong.displayadd_channel)
            self.click_zong(Display_Zong.displayadd_channel_choose)
        elif choose == 'four':
            self.click_zong(Display_Zong.displayadd_park)
            self.click_zong(Display_Zong.displayadd_park_choose)
            self.click_zong(Display_Zong.displayadd_region)
            self.click_zong(Display_Zong.displayadd_region_choose)
            self.click_zong(Display_Zong.displayadd_type_one)
            self.send_key_zong(Display_Zong.displayadd_type_one,Keys.DOWN,Keys.ENTER)
            self.click_zong(Display_Zong.displayadd_type_two)
            self.click_zong(Display_Zong.displayadd_type_two_choose)
        elif choose == 'five':
            self.click_zong(Display_Zong.displayadd_park)
            self.click_zong(Display_Zong.displayadd_park_choose)
            self.click_zong(Display_Zong.displayadd_type_one)
            self.send_key_zong(Display_Zong.displayadd_type_one,Keys.DOWN,Keys.ENTER)
            self.click_zong(Display_Zong.displayadd_type_two)
            self.click_zong(Display_Zong.displayadd_type_two_choose)
        elif choose == 'six':
            self.click_zong(Display_Zong.displayadd_type_one)
            self.send_key_zong(Display_Zong.displayadd_type_one,Keys.DOWN,Keys.ENTER)
            self.click_zong(Display_Zong.displayadd_type_two)
            self.click_zong(Display_Zong.displayadd_type_two_choose)
        self.click_zong(Display_Zong.displayadd_confirm)

    def display_update(self,head,username,password):
        self.login_display(head,username,password)
        self.click_zong(Display_Zong.displayupdate)
        self.click_zong(Display_Zong.displayupdate_daytime_volume)
        self.click_eles_presence_zong(Display_Zong.displayupdate_daytime_volume_choose,1)
        self.click_zong(Display_Zong.displayupdate_confirm)

    def display_find_search(self,head,username,password,values):
        self.login_display(head,username,password)
        self.send_key_zong(Display_Zong.displayfind_park,values)
        self.click_zong(Display_Zong.displayfind_search)

    def display_find_reset(self):
        self.click_zong(Display_Zong.displayfind_reset)

    def display_del(self):
        self.click_zong(Display_Zong.displaydel_choose)
        self.click_zong(Display_Zong.displaydel_del)
        self.click_zong(Display_Zong.displaydel_confirm)

    def display_delete(self,head,username,password):
        self.login_display(head,username,password)
        self.display_del()
