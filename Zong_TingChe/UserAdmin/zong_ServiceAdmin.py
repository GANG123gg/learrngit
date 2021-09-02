from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Zong_TingChe.Zongoperationpage import OperaPage_Login
from time import sleep
import random

class ServiceAdmin_Zong(OperaPage_Login):

    uesradmin = (By.XPATH,'//div/div[1]/div[2]/div[1]/div/ul/div[3]/li/div/span')
    serviceadmin = (By.XPATH,'//div[2]/div[1]/div/ul/div[3]/li/ul/div[5]/a/li/span')
    #客服账号新增
    serviceadd = (By.XPATH,'//div/div[2]/div/div[1]/div[1]/button/span')
    serviceadd_name = (By.XPATH,'//div/div[2]/form/div[1]/div[1]/div/div/div/input')
    serviceadd_gender = (By.XPATH,'//div/div[2]/form/div[1]/div[2]/div/div/div/div[1]/input')
    serviceadd_gender_man = (By.XPATH,'//div[1]/div[1]/ul/li/span[text()="男"]')
    serviceadd_gender_woman = (By.XPATH,'//div[1]/div[1]/ul/li/span[text()="女"]')
    serviceadd_phoen = (By.XPATH,'//div/div[2]/form/div[2]/div[1]/div/div/div/input')
    serviceadd_account = (By.XPATH,'//div/div[2]/form/div[2]/div[2]/div/div/div/input')
    serviceadd_confirm = (By.XPATH,'//div/div[3]/div/button[1]/span')
    #客服账号编辑
    serviceupdate = (By.XPATH,'//div/div[2]/div/div[2]/div[3]/table/tbody/tr/td[9]/div/button/span')
    serviceupdate_confirm = (By.XPATH,'//div/div[3]/div/button[1]/span')
    #客服账号查询
    servicefind_search = (By.XPATH,'//div/div[1]/form/div[3]/div/button[1]/span')
    servicefind_reset = (By.XPATH,'//div/div[1]/form/div[3]/div/button[2]/span')
    #客服账号删除
    servicedel_account = (By.XPATH,'//div/div[2]/div/div[2]/div[3]/table/tbody/tr[1]/td[2]/div')
    servicedel_del = (By.XPATH,'//div/div[2]/div/div[1]/div[2]/button/span')
    servicedel_confirm = (By.XPATH,'//div/div[3]/button[2]/span')



    def userservice(self):
        try:
            self.click_script_zong(OperaPage_Login.shrink)
        except:
            self.click_script_zong(OperaPage_Login.open_shrink)
            self.sav_creenshot()
        self.click_script_zong(ServiceAdmin_Zong.uesradmin)
        self.click_script_zong(ServiceAdmin_Zong.serviceadmin)

    def login_service(self,head,username,password):
        self.log_zong(head)
        self.login_zonglogin(username,password)
        self.userservice()

    def service_add_one(self,head,username,password,choose,name,phone,account):
        self.login_service(head,username,password)
        self.click_zong(ServiceAdmin_Zong.serviceadd)
        self.send_key_zong(ServiceAdmin_Zong.serviceadd_name,name)
        if choose == 'one':
            self.click_zong(ServiceAdmin_Zong.serviceadd_gender)
            sex_service =(ServiceAdmin_Zong.serviceadd_gender_man,ServiceAdmin_Zong.serviceadd_gender_woman)
            ran_service = random.randint(0,1)
            sleep(1)
            self.click_zong(sex_service[ran_service])
        elif choose == 'two':
            pass
        self.send_key_zong(ServiceAdmin_Zong.serviceadd_phoen,phone)
        self.send_key_zong(ServiceAdmin_Zong.serviceadd_account,account)
        self.click_zong(ServiceAdmin_Zong.serviceadd_confirm)

    def service_update_one(self,head,username,password,choose,ele,values):
        self.login_service(head,username,password)
        self.click_zong(ServiceAdmin_Zong.serviceupdate)
        service_redact = (By.XPATH,ele)
        self.send_key_zong(service_redact,Keys.CONTROL,'a')
        self.send_key_zong(service_redact,Keys.BACK_SPACE)
        if choose == 'one':
            pass
        elif choose == 'two':
            self.send_key_zong(service_redact,values)
        self.click_zong(ServiceAdmin_Zong.serviceupdate_confirm)

    def service_check_search(self,head,username,password,ele,values):
        self.login_service(head,username,password)
        ments = (By.XPATH,ele)
        self.send_key_zong(ments,values)
        self.click_zong(ServiceAdmin_Zong.servicefind_search)

    def service_check_reset(self):
        self.click_zong(ServiceAdmin_Zong.servicefind_reset)

    def service_del(self,head,username,password):
        self.login_service(head,username,password)
        self.click_zong(ServiceAdmin_Zong.servicedel_account)
        self.click_zong(ServiceAdmin_Zong.servicedel_del)
        self.click_zong(ServiceAdmin_Zong.servicedel_confirm)