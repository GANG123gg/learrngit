from selenium.webdriver.common.by import By
from Zong_TingChe.Zongoperationpage import OperaPage_Login
from selenium.webdriver.common.keys import Keys
from time import sleep



class GroupAdmin_zong(OperaPage_Login):


    uesradmin = (By.XPATH,'//div/div[1]/div[2]/div[1]/div/ul/div[3]/li/div/span')
    groupadmin = (By.XPATH,'//div[1]/div/ul/div[3]/li/ul/div[1]/a/li/span')
    #集团账号新增
    groupadd = (By.XPATH,'//div/div[2]/div/div[1]/div/button/span')
    groupadd_groupname = (By.XPATH,'//div[1]/div/div[2]/form/div[1]/div[1]/div/div/div/input')
    groupadd_region = (By.XPATH,'//div[1]/div/div[2]/form/div[1]/div[2]/div/div/div/div[1]/div[1]/div[2]/input')
    groupadd_name = (By.XPATH,'//div[1]/div/div[2]/form/div[2]/div[1]/div/div/div/input')
    groupadd_phone = (By.XPATH,'//div[1]/div/div[2]/form/div[2]/div[2]/div/div/div/input')
    groupadd_email = (By.XPATH,'//div[1]/div/div[2]/form/div[3]/div/div/div/div[1]/input')
    groupadd_address = (By.XPATH,'//div[1]/div/div[2]/form/div[4]/div/div/div/input')
    groupadd_next_step = (By.XPATH,'//div[1]/div/div[3]/div/button[1]/span')#下一步
    groupadd_account = (By.XPATH,'//section/div/div[5]/div[2]/div/div[2]/form/div[1]/div[1]/div/div/div[1]/input')
    #生效日期
    groupadd_effective_date = (By.XPATH,'//div[2]/div/div[2]/form/div[2]/div[1]/div/div/div/input')
    groupadd_select_date_one = (By.XPATH,'//div[1]/div/div[1]/span[1]/div/input')
    groupadd_confirm_one = (By.XPATH,'//div[2]/button[2]/span')
    #截止日期
    groupadd_expiration_date = (By.XPATH,'//div[2]/div/div[2]/form/div[2]/div[2]/div/div/div/input')
    groupadd_select_date_two = '//div[1]/div/div[1]/span[1]/div/input'
    groupadd_select_time_two = '//div[1]/div/div[1]/span[2]/div[1]/input'
    groupadd_confirm_two = '//div[2]/button[2]/span'
    groupadd_finish = (By.XPATH,'//div[2]/div/div[3]/div/button[1]/span')
    #所属区域
    groupadd_region_data = Keys.DOWN,Keys.DOWN,Keys.RIGHT,Keys.DOWN,Keys.DOWN,Keys.RIGHT,Keys.DOWN,Keys.ENTER
    groupadd_region_null = ''
    #Esc键
    groupadd_region_null_effective = Keys.ESCAPE

    #集团修改
    group_redact = (By.XPATH,'//div/div[2]/div/div[2]/div[3]/table/tbody/tr[1]/td[12]/div/button[1]/span')
    group_redact_effective = (By.XPATH,'//div/div[2]/form/div[7]/div[1]/div/div/div/input')
    group_redact_effective_date = '//div[1]/div/div[1]/span[1]/div/input'
    group_redact_effective_time = '//div[1]/div/div[1]/span[2]/div[1]/input'
    group_redact_effective_con = '//div[1]/div/div[1]/span[2]/div[2]/div[2]/button[2]'
    group_redact_effective_confirm = '//div[2]/button[2]/span'
    group_redact_expiration = (By.XPATH,'//div/div[2]/form/div[7]/div[2]/div/div/div/input')
    group_redact_expiration_date = (By.XPATH,'//div[1]/div/div[1]/span[1]/div/input')
    group_redact_expiration_time =(By.XPATH, '//div[1]/div/div[1]/span[2]/div[1]/input')
    group_redact_expiration_con = (By.XPATH,'//div[1]/div/div[1]/span[2]/div[2]/div[2]/button[2]')
    group_redact_expiration_confirm = (By.XPATH,'//div[2]/button[2]/span')
    group_redact_finish = (By.XPATH,'//div/div[3]/div/button[1]/span')

    #集团账号查询
    group_find_search = (By.XPATH,'//div/div[1]/form/div[4]/div/button[1]/span')
    group_find_reset = (By.XPATH,'//div/div[1]/form/div[4]/div/button[2]/span')
    group_find_details = (By.XPATH,'//div/div[2]/div/div[2]/div[3]/table/tbody/tr[1]/td[12]/div/button[2]/span')

    def usergroup(self):
        try:
            self.click_script_zong(OperaPage_Login.shrink)
        except:
            self.click_script_zong(OperaPage_Login.open_shrink)
            self.sav_creenshot()
        self.click_script_zong(GroupAdmin_zong.uesradmin)
        self.click_script_zong(GroupAdmin_zong.groupadmin)

    def login_user(self,head,username,password):
        self.log_zong(head)
        self.login_zonglogin(username,password)
        self.usergroup()

    def group_adduser(self,head,username,password,choose,group_name,name,phone,email,address,account,select_date_one,
                      select_date_two,select_time_two):
        self.login_user(head,username,password)
        self.click_script_zong(GroupAdmin_zong.groupadd)
        if choose == 'one':
            self.send_key_zong(GroupAdmin_zong.groupadd_groupname,group_name)
            self.send_key_zong(GroupAdmin_zong.groupadd_name,name)
            self.send_key_zong(GroupAdmin_zong.groupadd_phone,phone)
            self.send_key_zong(GroupAdmin_zong.groupadd_email,email)
            self.send_key_zong(GroupAdmin_zong.groupadd_address,address)
            self.send_key_zong(GroupAdmin_zong.groupadd_region,Keys.DOWN,Keys.DOWN,
                               Keys.RIGHT,Keys.DOWN,Keys.DOWN,Keys.RIGHT,Keys.DOWN,Keys.ENTER)
            self.click_script_zong(GroupAdmin_zong.groupadd_next_step)#下一步
            sleep(1)
            self.send_key_zong(GroupAdmin_zong.groupadd_account,account)
            #生效时间
            self.click_zong(GroupAdmin_zong.groupadd_effective_date)
            self.send_key_zong(GroupAdmin_zong.groupadd_select_date_one,select_date_one)
            self.click_script_zong(GroupAdmin_zong.groupadd_confirm_one)
            #截止时间
            self.click_zong(GroupAdmin_zong.groupadd_expiration_date)
            sleep(1)
            ele_data =self.driver.find_elements_by_xpath(GroupAdmin_zong.groupadd_select_date_two)
            ele_data[1].send_keys(select_date_two)
            sleep(1)
            ele_time = self.driver.find_elements_by_xpath(GroupAdmin_zong.groupadd_select_time_two)
            ele_time[1].click()
            ele_time[1].clear()
            sleep(1)
            ele_time[1].send_keys(select_time_two)
            sleep(1)
            ele_confirm = self.driver.find_elements_by_xpath(GroupAdmin_zong.groupadd_confirm_two)
            ele_confirm[1].click()
            self.click_zong(GroupAdmin_zong.groupadd_finish)
        elif choose == 'two':
            self.send_key_zong(GroupAdmin_zong.groupadd_groupname,group_name)
            self.send_key_zong(GroupAdmin_zong.groupadd_region,Keys.DOWN,Keys.DOWN,
                               Keys.RIGHT,Keys.DOWN,Keys.DOWN,Keys.RIGHT,Keys.DOWN,Keys.ENTER)
            self.send_key_zong(GroupAdmin_zong.groupadd_name,name)
            self.send_key_zong(GroupAdmin_zong.groupadd_phone,phone)
            self.send_key_zong(GroupAdmin_zong.groupadd_email,email)
            self.send_key_zong(GroupAdmin_zong.groupadd_address,address)
            self.click_script_zong(GroupAdmin_zong.groupadd_next_step)#下一步
        elif choose == 'three':
            self.send_key_zong(GroupAdmin_zong.groupadd_groupname,group_name)
            self.send_key_zong(GroupAdmin_zong.groupadd_name,name)
            self.send_key_zong(GroupAdmin_zong.groupadd_phone,phone)
            self.send_key_zong(GroupAdmin_zong.groupadd_email,email)
            self.send_key_zong(GroupAdmin_zong.groupadd_address,address)
            self.click_script_zong(GroupAdmin_zong.groupadd_next_step)#下一步
        elif choose == 'four':
            self.send_key_zong(GroupAdmin_zong.groupadd_groupname,group_name)
            self.send_key_zong(GroupAdmin_zong.groupadd_region,Keys.DOWN,Keys.DOWN,
                               Keys.RIGHT,Keys.DOWN,Keys.DOWN,Keys.RIGHT,Keys.DOWN,Keys.ENTER)
            self.send_key_zong(GroupAdmin_zong.groupadd_name,name)
            self.send_key_zong(GroupAdmin_zong.groupadd_phone,phone)
            self.send_key_zong(GroupAdmin_zong.groupadd_email,email)
            self.send_key_zong(GroupAdmin_zong.groupadd_address,address)
            self.click_script_zong(GroupAdmin_zong.groupadd_next_step)#下一步
            self.send_key_zong(GroupAdmin_zong.groupadd_account,account)
            self.click_zong(GroupAdmin_zong.groupadd_effective_date)
            self.send_key_zong(GroupAdmin_zong.groupadd_select_date_one,GroupAdmin_zong.groupadd_region_null_effective)
            #截止时间
            self.click_zong(GroupAdmin_zong.groupadd_expiration_date)
            sleep(1)
            ele_data =self.driver.find_elements_by_xpath(GroupAdmin_zong.groupadd_select_date_two)
            ele_data[1].send_keys(select_date_two)
            sleep(1)
            ele_time = self.driver.find_elements_by_xpath(GroupAdmin_zong.groupadd_select_time_two)
            ele_time[1].click()
            ele_time[1].clear()
            sleep(1)
            ele_time[1].send_keys(select_time_two)
            sleep(1)
            ele_confirm = self.driver.find_elements_by_xpath(GroupAdmin_zong.groupadd_confirm_two)
            ele_confirm[1].click()
            self.click_zong(GroupAdmin_zong.groupadd_finish)
        elif choose == 'five':
            self.send_key_zong(GroupAdmin_zong.groupadd_groupname,group_name)
            self.send_key_zong(GroupAdmin_zong.groupadd_region,Keys.DOWN,Keys.DOWN,
                               Keys.RIGHT,Keys.DOWN,Keys.DOWN,Keys.RIGHT,Keys.DOWN,Keys.ENTER)
            self.send_key_zong(GroupAdmin_zong.groupadd_name,name)
            self.send_key_zong(GroupAdmin_zong.groupadd_phone,phone)
            self.send_key_zong(GroupAdmin_zong.groupadd_email,email)
            self.send_key_zong(GroupAdmin_zong.groupadd_address,address)
            self.click_script_zong(GroupAdmin_zong.groupadd_next_step)#下一步
            self.send_key_zong(GroupAdmin_zong.groupadd_account,account)
            self.click_zong(GroupAdmin_zong.groupadd_effective_date)
            self.send_key_zong(GroupAdmin_zong.groupadd_select_date_one,select_date_one)
            self.click_script_zong(GroupAdmin_zong.groupadd_confirm_one)
            self.click_zong(GroupAdmin_zong.groupadd_finish)

    def group_update(self,head,username,password,choose,ele):
        self.login_user(head,username,password)
        self.click_script_zong(GroupAdmin_zong.group_redact)
        group_redact_ele = (By.XPATH,ele)
        sleep(2)
        if choose == 'one':
            self.send_key_zong(group_redact_ele,Keys.CONTROL,'a')
            self.send_key_zong(group_redact_ele,Keys.BACK_SPACE)
        elif choose == 'two':
            self.click_zong(group_redact_ele)
        self.click_zong(GroupAdmin_zong.group_redact_finish)

    def group_update_one(self,head,username,password,expiration_date,expiration_time,effective_date,effective_time,):
        self.login_user(head,username,password)
        self.click_script_zong(GroupAdmin_zong.group_redact)
        #截止时间
        self.click_zong(GroupAdmin_zong.group_redact_expiration)
        self.send_key_zong(GroupAdmin_zong.group_redact_expiration_date,Keys.CONTROL,'a')
        self.send_key_zong(GroupAdmin_zong.group_redact_expiration_date,Keys.BACK_SPACE)
        sleep(1)
        self.send_key_zong(GroupAdmin_zong.group_redact_expiration_date,expiration_date)
        self.send_key_zong(GroupAdmin_zong.group_redact_expiration_time,Keys.CONTROL,'a')
        self.send_key_zong(GroupAdmin_zong.group_redact_expiration_time,Keys.BACK_SPACE)
        sleep(1)
        self.send_key_zong(GroupAdmin_zong.group_redact_expiration_time,expiration_time)
        self.click_zong(GroupAdmin_zong.group_redact_expiration_con)
        self.click_script_zong(GroupAdmin_zong.group_redact_expiration_confirm)

        #生效时间
        self.click_zong(GroupAdmin_zong.group_redact_effective)
        sleep(1)
        ele_data =self.driver.find_elements_by_xpath(GroupAdmin_zong.group_redact_effective_date)
        ele_data[1].click()
        ele_data[1].clear()
        sleep(1)
        ele_data[1].send_keys(effective_date)
        sleep(1)
        ele_time = self.driver.find_elements_by_xpath(GroupAdmin_zong.group_redact_effective_time)
        ele_time[1].click()
        ele_time[1].clear()
        sleep(1)
        ele_time[1].send_keys(effective_time)
        sleep(1)
        ele_con = self.driver.find_elements_by_xpath(GroupAdmin_zong.group_redact_effective_con)
        ele_con[1].click()
        sleep(1)
        ele_confirm = self.driver.find_elements_by_xpath(GroupAdmin_zong.group_redact_effective_confirm)
        ele_confirm[1].click()
        self.click_zong(GroupAdmin_zong.group_redact_finish)



    def group_checkuser_search(self,head,username,password,loca,element,values):
        self.login_user(head,username,password)
        ele = (loca,element)
        self.send_key_zong(ele,values)
        self.click_zong(GroupAdmin_zong.group_find_search)
    def group_checkuser_reset(self):
        self.click_zong(GroupAdmin_zong.group_find_reset)

