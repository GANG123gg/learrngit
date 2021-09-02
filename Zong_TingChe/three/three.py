from selenium.webdriver.common.by import By
from Zong_TingChe.Zongoperationpage import OperaPage_Login
from time import sleep



class UserAdmin_zong(OperaPage_Login):

    uesradmin = (By.XPATH,'//div/div[1]/div[2]/div[1]/div/ul/div[3]/li/div/span')
    groupadmin = (By.XPATH,'//div/div[1]/div[2]/div[1]/div/ul/div[3]/li/ul/div[1]/a/li/span')
    groupadd = (By.XPATH,'//div/div[2]/div/div[1]/div/button/span')
    groupadd_groupname = (By.XPATH,'//div[1]/div/div[2]/form/div[1]/div[1]/div/div/div/input')
    groupadd_region = (By.XPATH,'//div[1]/div/div[2]/form/div[1]/div[2]/div/div/div/div[1]/div[1]/div[2]/input')
    groupadd_name = (By.XPATH,'//div[1]/div/div[2]/form/div[2]/div[1]/div/div/div/input')
    groupadd_phone = (By.XPATH,'//div[1]/div/div[2]/form/div[2]/div[2]/div/div/div/input')
    groupadd_email = (By.XPATH,'//div[1]/div/div[2]/form/div[3]/div/div/div/div[1]/input')
    groupadd_address = (By.XPATH,'//div[1]/div/div[2]/form/div[4]/div/div/div/input')
    groupadd_next_step = (By.XPATH,'//div[1]/div/div[3]/div/button[1]/span')
    groupadd_effective_date = (By.XPATH,'//div[2]/div/div[2]/form/div[2]/div[1]/div/div/div/input')
    groupadd_select_date_one = (By.XPATH,'//div[1]/div/div[1]/span[1]/div/input')
    groupadd_select_time_one = (By.XPATH,'//div[1]/div/div[1]/span[2]/div[1]/input')
    groupadd_confirm_one = (By.XPATH,'//div[2]/button[2]')
    groupadd_expiration_date = (By.XPATH,'//div[2]/div/div[2]/form/div[2]/div[2]/div/div/div/input')
    groupadd_select_date_two = (By.XPATH,'//div[1]/div/div[1]/span[1]/div/input')
    groupadd_select_time_two = (By.XPATH,'//div[1]/div/div[1]/span[2]/div[1]/input')
    groupadd_confirm_two = (By.XPATH,'//div[2]/button[2]/span')
    groupadd_finish = (By.XPATH,'//div[2]/div/div[3]/div/button[1]/span')

    def usergroup(self):
        self.click_script_zong(UserAdmin_zong.uesradmin)
        self.click_script_zong(UserAdmin_zong.groupadmin)

    def group_adduser(self,group_name,name,phone):


        self.click_script_zong(UserAdmin_zong.groupadd)
        sleep(1)
        self.send_key_zong(UserAdmin_zong.groupadd_groupname,group_name)
        sleep(1)
        self.send_key_keyboard_zong(UserAdmin_zong.groupadd_region)
        sleep(1)
        self.send_key_zong(UserAdmin_zong.groupadd_name,name)
        self.send_key_zong(UserAdmin_zong.groupadd_phone,phone)
        # self.send_key_zong(UserAdmin_zong.groupadd_email,email)
        # self.send_key_zong(UserAdmin_zong.groupadd_address,address)
        # self.click_zong(UserAdmin_zong.groupadd_next_step)
        # self.click_zong(UserAdmin_zong.groupadd_effective_date)
        # self.send_key_zong(UserAdmin_zong.groupadd_select_date_one,select_date_one)
        # self.click_zong(UserAdmin_zong.groupadd_confirm_one)
        # self.click_zong(UserAdmin_zong.groupadd_expiration_date)
        # self.send_key_zong(UserAdmin_zong.groupadd_select_date_two,select_date_two)
        # self.click_zong(UserAdmin_zong.groupadd_confirm_two)
        # self.click_zong(UserAdmin_zong.groupadd_finish)

    def group_updateuser(self):
        pass

    def group_checkuser(self):
        pass

    def group_deluser(self):
        pass