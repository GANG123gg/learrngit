from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Zong_TingChe.Zongoperationpage import OperaPage_Login
from time import sleep
import random


class PatrolAdmin_Zong(OperaPage_Login):

    uesradmin = (By.XPATH,'//div/div[1]/div[2]/div[1]/div/ul/div[3]/li/div/span')
    patroladmin = (By.XPATH,'//div[2]/div[1]/div/ul/div[3]/li/ul/div[6]/a/li/span')
    #新增巡逻岗账号
    patroladd = (By.XPATH,'//div/div[2]/div/div[1]/div[1]/button/span')
    patroladd_name = (By.XPATH,'//form/div[1]/div[1]/div/div/div/input')
    patroladd_gender = (By.XPATH,'//form/div[1]/div[2]/div/div/div/div/input')
    patroladd_gender_man = (By.XPATH,'//div[1]/div[1]/ul/li[1]/span[text()="男"]')
    patroladd_gender_woman = (By.XPATH,'//div[1]/div[1]/ul/li[2]/span[text()="女"]')
    patroladd_phone = (By.XPATH,'//form/div[2]/div[1]/div/div/div/input')
    patroladd_account = (By.XPATH,'//form/div[2]/div[2]/div/div/div/input')
    patroladd_confirm = (By.XPATH,'//div/div[3]/div/button[1]/span')
    #修改巡逻岗账号
    patrolupdate = (By.XPATH,'//div/div[2]/div/div[2]/div[3]/table/tbody/tr/td[9]/div/button/span')
    patrolupdate_confirm = (By.XPATH,'//div/div[3]/div/button[1]/span')
    #查询巡逻岗
    patrolfind_search = (By.XPATH,'//div/div[1]/form/div[3]/div/button[1]/span')
    patrolfind_reset = (By.XPATH,'//div/div[1]/form/div[3]/div/button[2]/span')
    #删除巡逻岗
    patroldel_account = (By.XPATH,'//div/div[2]/div/div[2]/div[3]/table/tbody/tr[1]/td[2]/div')
    patroldel_del = (By.XPATH,'//div/div[2]/div/div[1]/div[2]/button/span')
    patroldel_confirm = (By.XPATH,'//div/div[3]/button[2]/span')



    def userpatrol(self):
        try:
            self.click_script_zong(OperaPage_Login.shrink)
        except:
            self.click_script_zong(OperaPage_Login.open_shrink)
            self.sav_creenshot()
        self.click_script_zong(PatrolAdmin_Zong.uesradmin)
        self.click_script_zong(PatrolAdmin_Zong.patroladmin)

    def login_patrol(self,head,username,password):
        self.log_zong(head)
        self.login_zonglogin(username,password)
        self.userpatrol()

    def patrol_add_one(self,head,username,password,choose,name,phone,account):
        self.login_patrol(head,username,password)
        sleep(1)
        self.click_zong(PatrolAdmin_Zong.patroladd)
        self.send_key_zong(PatrolAdmin_Zong.patroladd_name,name)
        if choose == 'one':
            self.click_zong(PatrolAdmin_Zong.patroladd_gender)
            sex_gender = (PatrolAdmin_Zong.patroladd_gender_man,PatrolAdmin_Zong.patroladd_gender_woman)
            ran_gender = random.randint(0,1)
            self.click_zong(sex_gender[ran_gender])
        elif choose == 'two':
            pass
        self.send_key_zong(PatrolAdmin_Zong.patroladd_phone,phone)
        self.send_key_zong(PatrolAdmin_Zong.patroladd_account,account)
        self.click_zong(PatrolAdmin_Zong.patroladd_confirm)

    def patrol_update_one(self,head,username,password,choose,ele,values):
        self.login_patrol(head,username,password)
        self.click_zong(PatrolAdmin_Zong.patrolupdate)
        patrol_redact = (By.XPATH,ele)
        self.send_key_zong(patrol_redact,Keys.CONTROL,'a')
        self.send_key_zong(patrol_redact,Keys.BACK_SPACE)
        if choose == 'one':
            pass
        elif choose == 'two':
            self.send_key_zong(patrol_redact,values)
        self.click_zong(PatrolAdmin_Zong.patrolupdate_confirm)

    def patrol_find_search(self,head,username,password,ele,values):
        self.login_patrol(head,username,password)
        ments = (By.XPATH,ele)
        self.send_key_zong(ments,values)
        self.click_zong(PatrolAdmin_Zong.patrolfind_search)

    def patrol_find_reset(self):
        self.click_zong(PatrolAdmin_Zong.patrolfind_reset)

    def patrol_del(self,head,username,password):
        self.login_patrol(head,username,password)
        self.click_zong(PatrolAdmin_Zong.patroldel_account)
        self.click_zong(PatrolAdmin_Zong.patroldel_del)
        self.click_zong(PatrolAdmin_Zong.patroldel_confirm)
