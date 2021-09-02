from selenium.webdriver.common.by import By
from Zong_TingChe.Zongoperationpage import OperaPage_Login
from selenium.webdriver.common.keys import Keys
from time import sleep
import random



class OwnerAdmin_zong(OperaPage_Login):

    uesradmin = (By.XPATH,'//div/div[1]/div[2]/div[1]/div/ul/div[3]/li/div/span')
    owneradmin = (By.XPATH,'//div/div[1]/div[2]/div[1]/div/ul/div[3]/li/ul/div[2]/a/li/span')
    #业主账号新增
    owneradd = (By.XPATH,'//div/div[2]/div/div[1]/div[1]/button/span')
    owneradd_company = (By.XPATH,'//div/div[5]/div[1]/div/div[2]/form/div[1]/div[1]/div/div/div/input')
    owneradd_ownername = (By.XPATH,'//div/div[5]/div[1]/div/div[2]/form/div[1]/div[2]/div/div/div/input')
    owneradd_sex = (By.XPATH,'//div/div[5]/div[1]/div/div[2]/form/div[2]/div[1]/div/div/div/div/input')

    owneradd_sex_man = (By.XPATH,'//div[1]/div[1]/ul/li/span[text()="男"]')
    owneradd_sex_woman = (By.XPATH,'//div[1]/div[1]/ul/li/span[text()="女"]')
    owneradd_phone = (By.XPATH,'//div/div[5]/div[1]/div/div[2]/form/div[2]/div[2]/div/div/div/input')
    owneradd_card = (By.XPATH,'//div/div[5]/div[1]/div/div[2]/form/div[3]/div/div/div/div[1]/input')
    owneradd_address = (By.XPATH,'//div/div[5]/div[1]/div/div[2]/form/div[4]/div/div/div/div/input')
    owneradd_next_step = (By.XPATH,'//div/div[5]/div[1]/div/div[3]/div/button[1]/span')#下一步
    #生效时间
    owneradd_effective = (By.XPATH,'//div/div[5]/div[2]/div/div[2]/form/div[2]/div[1]/div/div/div/input')
    owneradd_effective_date = '//div[1]/div/div[1]/span[1]/div/input'
    owneradd_effective_time = '//div[1]/div/div[1]/span[2]/div[1]/input'
    owneradd_effective_time_confirm = '//div[1]/div/div[1]/span[2]/div[2]/div[2]/button[2]'
    owneradd_effective_confirm = '//div[2]/button[2]/span'
    #截止时间
    owneradd_expiration = (By.XPATH,'//div/div[5]/div[2]/div/div[2]/form/div[2]/div[2]/div/div/div/input')
    owneradd_expiration_date = (By.XPATH,'//div[1]/div/div[1]/span[1]/div/input')
    owneradd_expiration_time = (By.XPATH,'//div[1]/div/div[1]/span[2]/div[1]/input')
    owneradd_expiration_time_confirm = (By.XPATH,'//div[1]/div/div[1]/span[2]/div[2]/div[2]/button[2]')
    owneradd_expiration_confirm =(By.XPATH,'//div[2]/button[2]/span')
    owneradd_confirm = (By.XPATH,'//div/div[5]/div[2]/div/div[3]/div/button[1]/span')


    #修改业主账号
    ownerupdate = (By.XPATH,'//div/div[2]/div/div[2]/div[3]/table/tbody/tr[1]/td[9]/div/button[1]/span')
    #生效时间
    ownerupdate_effective = (By.XPATH,'//div/div[2]/form/div[4]/div[1]/div/div/div/input')
    ownerupdate_effective_date = '//div[1]/div/div[1]/span[1]/div/input'
    ownerupdate_effective_time = '//div[1]/div/div[1]/span[2]/div[1]/input'
    ownerupdate_effective_time_confirm = '//div[1]/div/div[1]/span[2]/div[2]/div[2]/button[2]'
    ownerupdate_effective_confirm = '//div[2]/button[2]/span'

    #截止时间
    ownerupdate_expiration = (By.XPATH,'//div/div[2]/form/div[4]/div[2]/div/div/div/input')
    ownerupdate_expiration_date = (By.XPATH,'//div[1]/div/div[1]/span[1]/div/input')
    ownerupdate_expiration_time = (By.XPATH,'//div[1]/div/div[1]/span[2]/div[1]/input')
    ownerupdate_expiration_time_confirm = (By.XPATH,'//div[1]/div/div[1]/span[2]/div[2]/div[2]/button[2]')
    ownerupdate_expiration_confirm = (By.XPATH,'//div[2]/button[2]/span')
    ownerupdate_confirm = (By.XPATH,'//div/div[3]/div/button[1]/span')

    #查询业主信息
    ownerfind_search = (By.XPATH,'//div/div[1]/form/div[4]/div/button[1]/span')#搜索
    ownerfind_reset = (By.XPATH,'//div/div[1]/form/div[4]/div/button[2]/span')#重置

    #删除业主账号
    ownerdel_name = (By.XPATH,'//div/div[2]/div/div[2]/div[3]/table/tbody/tr[1]/td[2]/div')
    ownerdel_del = (By.XPATH,'//div/div[2]/div/div[1]/div[2]/button/span')
    ownerdel_confirm = (By.XPATH,'//div/div[3]/button[2]')



    def userowner(self):
        try:
            self.click_script_zong(OperaPage_Login.shrink)
        except:
            self.click_script_zong(OperaPage_Login.open_shrink)
            self.sav_creenshot()
        self.click_script_zong(OwnerAdmin_zong.uesradmin)
        self.click_script_zong(OwnerAdmin_zong.owneradmin)

    def login_owner(self,head,username,password):
        self.log_zong(head)
        self.login_zonglogin(username,password)
        self.userowner()

    def owner_add_one(self,head,username,password,choose,company_name,ownername,phone,card,address,
                  expiration_date,expiration_time,effective_date,effective_time):
        self.login_owner(head,username,password)
        self.click_script_zong(OwnerAdmin_zong.owneradd)
        if choose == 'one':
            self.send_key_zong(OwnerAdmin_zong.owneradd_company,company_name)
            self.send_key_zong(OwnerAdmin_zong.owneradd_ownername,ownername)
            self.click_zong(OwnerAdmin_zong.owneradd_sex)
            sex_owner = (OwnerAdmin_zong.owneradd_sex_man,OwnerAdmin_zong.owneradd_sex_woman)
            ran_owner = random.randint(0,1)
            self.click_zong(sex_owner[ran_owner])
            self.send_key_zong(OwnerAdmin_zong.owneradd_phone,phone)
            self.send_key_zong(OwnerAdmin_zong.owneradd_card,card)
            self.send_key_zong(OwnerAdmin_zong.owneradd_address,address)
            self.click_script_zong(OwnerAdmin_zong.owneradd_next_step)

            #截止时间
            self.click_zong(OwnerAdmin_zong.owneradd_expiration)
            self.send_key_zong(OwnerAdmin_zong.owneradd_expiration_date,expiration_date)
            self.send_key_zong(OwnerAdmin_zong.owneradd_expiration_time,Keys.CONTROL,'a')
            self.send_key_zong(OwnerAdmin_zong.owneradd_expiration_time,Keys.BACK_SPACE)
            self.send_key_zong(OwnerAdmin_zong.owneradd_expiration_time,expiration_time)
            self.click_zong(OwnerAdmin_zong.owneradd_expiration_time_confirm)
            self.click_zong(OwnerAdmin_zong.owneradd_expiration_confirm)
            #生效时间
            self.click_zong(OwnerAdmin_zong.owneradd_effective)
            sleep(1)
            ele_data =self.driver.find_elements_by_xpath(OwnerAdmin_zong.owneradd_effective_date)
            ele_data[1].click()
            ele_data[1].clear()
            sleep(1)
            ele_data[1].send_keys(effective_date)
            sleep(1)
            ele_time = self.driver.find_elements_by_xpath(OwnerAdmin_zong.owneradd_effective_time)
            ele_time[1].click()
            ele_time[1].clear()
            sleep(1)
            ele_time[1].send_keys(effective_time)
            sleep(1)
            ele_con = self.driver.find_elements_by_xpath(OwnerAdmin_zong.owneradd_effective_time_confirm)
            ele_con[1].click()
            sleep(1)
            ele_confirm = self.driver.find_elements_by_xpath(OwnerAdmin_zong.owneradd_effective_confirm)
            ele_confirm[1].click()
            self.click_zong(OwnerAdmin_zong.owneradd_confirm)
        elif choose == 'two':
            self.send_key_zong(OwnerAdmin_zong.owneradd_company,company_name)
            self.send_key_zong(OwnerAdmin_zong.owneradd_ownername,ownername)
            self.click_zong(OwnerAdmin_zong.owneradd_sex)
            sex_owner = (OwnerAdmin_zong.owneradd_sex_man,OwnerAdmin_zong.owneradd_sex_woman)
            ran_owner = random.randint(0,1)
            self.click_zong(sex_owner[ran_owner])
            self.send_key_zong(OwnerAdmin_zong.owneradd_phone,phone)
            self.send_key_zong(OwnerAdmin_zong.owneradd_card,card)
            self.send_key_zong(OwnerAdmin_zong.owneradd_address,address)
            self.click_script_zong(OwnerAdmin_zong.owneradd_next_step)
        elif choose == 'three':
            self.send_key_zong(OwnerAdmin_zong.owneradd_company,company_name)
            self.send_key_zong(OwnerAdmin_zong.owneradd_ownername,ownername)
            self.click_zong(OwnerAdmin_zong.owneradd_sex)
            sex_owner = (OwnerAdmin_zong.owneradd_sex_man,OwnerAdmin_zong.owneradd_sex_woman)
            ran_owner = random.randint(0,1)
            self.click_zong(sex_owner[ran_owner])
            self.send_key_zong(OwnerAdmin_zong.owneradd_phone,phone)
            self.send_key_zong(OwnerAdmin_zong.owneradd_card,card)
            self.send_key_zong(OwnerAdmin_zong.owneradd_address,address)
            self.click_script_zong(OwnerAdmin_zong.owneradd_next_step)
            self.click_zong(OwnerAdmin_zong.owneradd_expiration)
            self.send_key_zong(OwnerAdmin_zong.owneradd_expiration_date,Keys.ESCAPE)
            #不设置截止日期
            self.click_zong(OwnerAdmin_zong.owneradd_effective)
            sleep(1)
            ele_data =self.driver.find_elements_by_xpath(OwnerAdmin_zong.owneradd_effective_date)
            ele_data[1].click()
            ele_data[1].clear()
            sleep(1)
            ele_data[1].send_keys(effective_date)
            sleep(1)
            ele_time = self.driver.find_elements_by_xpath(OwnerAdmin_zong.owneradd_effective_time)
            ele_time[1].click()
            ele_time[1].clear()
            sleep(1)
            ele_time[1].send_keys(effective_time)
            sleep(1)
            ele_con = self.driver.find_elements_by_xpath(OwnerAdmin_zong.owneradd_effective_time_confirm)
            ele_con[1].click()
            sleep(1)
            ele_confirm = self.driver.find_elements_by_xpath(OwnerAdmin_zong.owneradd_effective_confirm)
            ele_confirm[1].click()
            self.click_zong(OwnerAdmin_zong.owneradd_confirm)
        elif choose == 'four':
            self.send_key_zong(OwnerAdmin_zong.owneradd_company,company_name)
            self.send_key_zong(OwnerAdmin_zong.owneradd_ownername,ownername)
            self.click_zong(OwnerAdmin_zong.owneradd_sex)
            sex_owner = (OwnerAdmin_zong.owneradd_sex_man,OwnerAdmin_zong.owneradd_sex_woman)
            ran_owner = random.randint(0,1)
            self.click_zong(sex_owner[ran_owner])
            self.send_key_zong(OwnerAdmin_zong.owneradd_phone,phone)
            self.send_key_zong(OwnerAdmin_zong.owneradd_card,card)
            self.send_key_zong(OwnerAdmin_zong.owneradd_address,address)
            self.click_script_zong(OwnerAdmin_zong.owneradd_next_step)
            #不设置生效日期
            self.click_zong(OwnerAdmin_zong.owneradd_expiration)
            self.send_key_zong(OwnerAdmin_zong.owneradd_expiration_date,expiration_date)
            self.send_key_zong(OwnerAdmin_zong.owneradd_expiration_time,Keys.CONTROL,'a')
            self.send_key_zong(OwnerAdmin_zong.owneradd_expiration_time,Keys.BACK_SPACE)
            self.send_key_zong(OwnerAdmin_zong.owneradd_expiration_time,expiration_time)
            self.click_zong(OwnerAdmin_zong.owneradd_expiration_time_confirm)
            self.click_zong(OwnerAdmin_zong.owneradd_expiration_confirm)
            self.click_zong(OwnerAdmin_zong.owneradd_confirm)


    def owner_update_one(self,head,username,password,choose,ele):
        self.login_owner(head,username,password)
        self.click_script_zong(OwnerAdmin_zong.ownerupdate)
        owner_redact_ele = (By.XPATH,ele)
        sleep(1)
        if choose == 'one':
            self.send_key_zong(owner_redact_ele,Keys.CONTROL,'a')
            self.send_key_zong(owner_redact_ele,Keys.BACK_SPACE)
            self.click_zong(OwnerAdmin_zong.ownerupdate_confirm)
        elif choose == 'two':
            self.send_key_zong(owner_redact_ele,Keys.BACKSPACE)
            self.click_zong(OwnerAdmin_zong.ownerupdate_confirm)

    def owner_update_three(self,head,username,password,expiration_date,expiration_time,
                           effective_date,effective_time):
        self.login_owner(head,username,password)
        self.click_zong(OwnerAdmin_zong.ownerupdate)
        self.click_zong(OwnerAdmin_zong.ownerupdate_expiration)
        self.send_key_zong(OwnerAdmin_zong.ownerupdate_expiration_date,Keys.CONTROL,'a')
        self.send_key_zong(OwnerAdmin_zong.ownerupdate_expiration_date,Keys.BACK_SPACE)
        self.send_key_zong(OwnerAdmin_zong.ownerupdate_expiration_date,expiration_date)
        self.send_key_zong(OwnerAdmin_zong.ownerupdate_expiration_time,Keys.CONTROL,'a')
        self.send_key_zong(OwnerAdmin_zong.ownerupdate_expiration_time,Keys.BACK_SPACE)
        self.send_key_zong(OwnerAdmin_zong.ownerupdate_expiration_time,expiration_time)
        self.click_zong(OwnerAdmin_zong.ownerupdate_expiration_time_confirm)
        self.click_zong(OwnerAdmin_zong.ownerupdate_expiration_confirm)
        #生效时间
        self.click_zong(OwnerAdmin_zong.ownerupdate_effective)
        sleep(1)
        ele_data =self.driver.find_elements_by_xpath(OwnerAdmin_zong.ownerupdate_effective_date)
        ele_data[1].click()
        ele_data[1].clear()
        sleep(1)
        ele_data[1].send_keys(effective_date)
        sleep(1)
        ele_time = self.driver.find_elements_by_xpath(OwnerAdmin_zong.ownerupdate_effective_time)
        ele_time[1].click()
        ele_time[1].clear()
        sleep(1)
        ele_time[1].send_keys(effective_time)
        sleep(1)
        ele_con = self.driver.find_elements_by_xpath(OwnerAdmin_zong.ownerupdate_effective_time_confirm)
        ele_con[1].click()
        sleep(1)
        ele_confirm = self.driver.find_elements_by_xpath(OwnerAdmin_zong.ownerupdate_effective_confirm)
        ele_confirm[1].click()
        sleep(1)
        self.click_zong(OwnerAdmin_zong.ownerupdate_confirm)

    def owner_check_search(self,head,username,password,ele,value):
        self.login_owner(head,username,password)
        ments = (By.XPATH,ele)
        self.send_key_zong(ments,value)
        self.click_zong(OwnerAdmin_zong.ownerfind_search)


    def owner_check_reset(self):
            self.click_zong(OwnerAdmin_zong.ownerfind_reset)

    def owner_del(self,head,username,password):
        self.login_owner(head,username,password)
        self.click_zong(OwnerAdmin_zong.ownerdel_name)
        self.click_zong(OwnerAdmin_zong.ownerdel_del)
        self.click_zong(OwnerAdmin_zong.ownerdel_confirm)







