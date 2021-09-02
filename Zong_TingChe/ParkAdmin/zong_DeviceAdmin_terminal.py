from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Zong_TingChe.Zongoperationpage import OperaPage_Login
from time import sleep
import random



class Terminal_Zong(OperaPage_Login):

    parkadmin = (By.XPATH,'//div/ul/div[4]/li/div/span')
    deviceadmin = (By.XPATH,'//div[1]/div[2]/div[1]/div/ul/div[4]/li/ul/div[2]/a/li/span')
    terminal = (By.XPATH,'//div/div[1]/ul/li[1]/span[text()="纵停终端"]')
    #新增终端
    terminaladd = (By.XPATH,'//div/div[2]/div[2]/div[1]/div[1]/button/span/span')
    terminaladd_park = (By.XPATH,'//form/div[1]/div[1]/div/div/div/div[1]/input')
    terminaladd_park_choose = (By.XPATH,'//div[1]/div[1]/ul/li/span[text()="吴忠测试车场"]')
    terminaladd_region = (By.XPATH,'//form/div[1]/div[2]/div/div/div/div[1]/input')
    terminaladd_region_choose = (By.XPATH,'//div[1]/div[1]/ul/li/span[text()="外区"]')
    terminaladd_channel = (By.XPATH,'//form/div[2]/div[1]/div/div/div/div/input')
    terminaladd_channel_choose = (By.XPATH,'//div[1]/div[1]/ul/li/span[text()="外_1进"]')
    terminaladd_sequence = (By.XPATH,'//form/div[2]/div[2]/div/div/div/input')
    terminaladd_confirm = (By.XPATH,'//div/div[3]/div/button[1]/span')
    #修改终端
    terminalupdate = (By.XPATH,'//table/tbody/tr/td[10]/div/button[2]/span')
    terminalupdate_sequence = (By.XPATH,'//form/div[2]/div[2]/div/div/div/input')
    terminalupdate_confirm = (By.XPATH,'//div/div[3]/div/button[1]/span')
    #查询终端
    terminalfind_search = (By.XPATH,'//div/div[2]/div[1]/form/div[3]/div/button[1]/span')
    terminalfind_reset = (By.XPATH,'//div/div[2]/div[1]/form/div[3]/div/button[2]/span')
    #删除终端
    terminaldel_choose = (By.XPATH,'//table/tbody/tr[1]/td[2]/div')
    terminaldel_del = (By.XPATH,'//div/div[2]/div[2]/div[1]/div[3]/button/span/span')
    terminaldel_confirm = (By.XPATH,'//div/div[3]/button[2]/span')



    def park_terminal(self):
        try:
            self.click_script_zong(OperaPage_Login.shrink)
        except:
            pass
        self.click_script_zong(Terminal_Zong.parkadmin)
        self.click_script_zong(Terminal_Zong.deviceadmin)
        self.click_zong(Terminal_Zong.terminal)

    def login_terminal(self,head,username,password):
        self.log_zong(head)
        self.login_zonglogin(username,password)
        self.park_terminal()

    def terminal_add(self,head,username,password,sequence,choose):
        self.login_terminal(head,username,password)
        self.click_zong(Terminal_Zong.terminaladd)
        if choose == 'one':
            self.click_zong(Terminal_Zong.terminaladd_park)
            self.click_zong(Terminal_Zong.terminaladd_park_choose)
            self.click_zong(Terminal_Zong.terminaladd_region)
            self.click_zong(Terminal_Zong.terminaladd_region_choose)
            self.click_zong(Terminal_Zong.terminaladd_channel)
            self.click_zong(Terminal_Zong.terminaladd_channel_choose)
        elif choose == 'two':#不选择通道
            self.click_zong(Terminal_Zong.terminaladd_park)
            self.click_zong(Terminal_Zong.terminaladd_park_choose)
            self.click_zong(Terminal_Zong.terminaladd_region)
            self.click_zong(Terminal_Zong.terminaladd_region_choose)
        elif choose == 'three':#不选择区域
            self.click_zong(Terminal_Zong.terminaladd_park)
            self.click_zong(Terminal_Zong.terminaladd_park_choose)
        elif choose == 'four':#不选择车场
            pass
        self.send_key_zong(Terminal_Zong.terminaladd_sequence,sequence)
        self.click_zong(Terminal_Zong.terminaladd_confirm)

    def terminal_update(self,head,username,password,choose,sequence):
        self.login_terminal(head,username,password)
        self.click_eles_zong(Terminal_Zong.terminalupdate,-1)
        if choose == 'one':
            self.send_key_zong(Terminal_Zong.terminalupdate_sequence,Keys.CONTROL,'a')
            self.send_key_zong(Terminal_Zong.terminalupdate_sequence,Keys.BACK_SPACE)
        elif choose == 'two':
            self.send_key_zong(Terminal_Zong.terminalupdate_sequence,Keys.CONTROL,'a')
            self.send_key_zong(Terminal_Zong.terminalupdate_sequence,Keys.BACK_SPACE)
            self.send_key_zong(Terminal_Zong.terminalupdate_sequence,sequence)
        self.click_zong(Terminal_Zong.terminalupdate_confirm)

    def terminal_find_search(self,head,username,password,ele,values):
        self.login_terminal(head,username,password)
        sleep(5)
        park_redact = (By.XPATH,ele)
        self.send_key_zong(park_redact,values)
        self.click_zong(Terminal_Zong.terminalfind_search)

    def terminal_find_reset(self):
        self.click_zong(Terminal_Zong.terminalfind_reset)

    def terminal_del(self,head,username,password):
        self.login_terminal(head,username,password)
        self.click_eles_zong(Terminal_Zong.terminaldel_choose,-1)
        self.click_zong(Terminal_Zong.terminaldel_del)
        self.click_zong(Terminal_Zong.terminaldel_confirm)


