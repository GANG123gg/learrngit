from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Zong_TingChe.Zongoperationpage import OperaPage_Login
from time import sleep
import random


class Platform_Admin_Zong(OperaPage_Login):

    uesradmin = (By.XPATH,'//div/div[1]/div[2]/div[1]/div/ul/div[3]/li/div/span')
    platformadmin = (By.XPATH,'//div[1]/div/ul/div[3]/li/ul/div[4]/a/li/span')
    #新增平台管理员
    platformadd = (By.XPATH,'//div/div[2]/div/div[1]/div[1]/button/span')
    platformadd_name = (By.XPATH,'//form/div[1]/div[1]/div/div/div/input')
    platformadd_phone = (By.XPATH,'//form/div[1]/div[2]/div/div/div/input')
    platformadd_account = (By.XPATH,'//form/div[2]/div[1]/div/div/div/input')
    platformadd_role = (By.XPATH,'//form/div[3]/div/div/div/div/div/input')
    platformadd_role_select = (By.XPATH,'//div[1]/div[1]/ul/li/span[text()="平台管理员"]')
    platformadd_remark = (By.XPATH,'//form/div[4]/div/div/div/div/input')
    platformadd_confirm = (By.XPATH,'//div/div[3]/div/button[1]/span')
    #编辑平台管理员
    platformupdate = (By.XPATH,'//table/tbody/tr[1]/td[7]/div/button[1]/span')
    platformupdate_confirm = (By.XPATH,'//div/div[3]/div/button[1]/span')
    #查询平台管理员
    platformfind_name = (By.XPATH,'//section/div/div[1]/form/div[1]/div/div/input')
    platformfind_phone = (By.XPATH,'//section/div/div[1]/form/div[2]/div/div/input')
    platformfind_search = (By.XPATH,'//section/div/div[1]/form/div[3]/div/button[1]/span')
    platformfind_reset = (By.XPATH,'//section/div/div[1]/form/div[3]/div/button[2]/span')
    #删除平台管理员
    platformdel_choose_one = (By.XPATH,'//div/div[2]/div[3]/table/tbody/tr/td[2]/div[text()="大白"]')
    platformdel_choose_two = (By.XPATH,'//div/div[2]/div[3]/table/tbody/tr/td[2]/div[text()="小黑"]')
    platformdel_del = (By.XPATH,'//section/div/div[2]/div/div[1]/div[3]/button/span')
    platformdel_confirm = (By.XPATH,'//div/div[3]/button[2]/span')


    def user_platform(self):
        try:
            self.click_script_zong(OperaPage_Login.shrink)
        except:
            self.click_script_zong(OperaPage_Login.open_shrink)
            self.sav_creenshot()
        self.click_script_zong(Platform_Admin_Zong.uesradmin)
        self.click_script_zong(Platform_Admin_Zong.platformadmin)

    def login_platform(self,head,username,password):
        self.log_zong(head)
        self.login_zonglogin(username,password)
        sleep(1)
        self.user_platform()

    def platform_admin_add(self,head,username,password,choose,name,phone,account,remark):
        self.login_platform(head,username,password)
        self.click_zong(Platform_Admin_Zong.platformadd)
        self.send_key_zong(Platform_Admin_Zong.platformadd_name,name)
        self.send_key_zong(Platform_Admin_Zong.platformadd_phone,phone)
        self.send_key_zong(Platform_Admin_Zong.platformadd_account,account)
        if choose == 'one':
            self.click_zong(Platform_Admin_Zong.platformadd_role)
            self.click_zong(Platform_Admin_Zong.platformadd_role_select)
        elif choose == 'two':
            pass
        self.send_key_zong(Platform_Admin_Zong.platformadd_remark,remark)
        self.click_zong(Platform_Admin_Zong.platformadd_confirm)

    def platform_admin_update(self,head,username,password,choose,ele,values):
        self.login_platform(head,username,password)
        self.click_zong(Platform_Admin_Zong.platformupdate)
        platform_redact_ele = (By.XPATH,ele)
        sleep(1)
        self.send_key_zong(platform_redact_ele,Keys.CONTROL,'a')
        self.send_key_zong(platform_redact_ele,Keys.BACK_SPACE)
        if choose == 'one':
            pass
        elif choose == 'two':
            self.send_key_zong(platform_redact_ele,values)
        self.click_zong(Platform_Admin_Zong.platformupdate_confirm)

    def platform_check_search(self,head,username,password,ele,value):
        self.login_platform(head,username,password)
        ments = (By.XPATH,ele)
        self.send_key_zong(ments,value)
        sleep(1)
        self.click_zong(Platform_Admin_Zong.platformfind_search)
        sleep(1)

    def platform_check_reset(self):
        self.click_zong(Platform_Admin_Zong.platformfind_reset)
        sleep(1)

    def platform_del(self,head,username,password):
        self.login_platform(head,username,password)
        choose_list = [Platform_Admin_Zong.platformdel_choose_one,Platform_Admin_Zong.platformdel_choose_two]
        for i in choose_list:
            self.click_zong(i)
        self.click_zong(Platform_Admin_Zong.platformdel_del)
        self.click_zong(Platform_Admin_Zong.platformdel_confirm)
        