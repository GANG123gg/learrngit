from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Zong_TingChe.Zongoperationpage import OperaPage_Login
from time import sleep
import random



class Discounts_List_Zong(OperaPage_Login):

    parkadmin = (By.XPATH,'//div/ul/div[4]/li/div/span')
    discountadmin = (By.XPATH,'//div/ul/div[4]/li/ul/div[6]/a/li/span')
    discountlist = (By.XPATH,'//section/div/div[1]/ul/li[1]/span')
    #新增优惠券
    listadd = (By.XPATH,'//section/div/div[2]/div[2]/div[1]/div[1]/button/span/span')
    listadd_name = (By.XPATH,'//form/div[1]/div/div/div/div/input')
    listadd_park = (By.XPATH,'//form/div[2]/div[1]/div/div/div/div[1]/input')
    listadd_park_choose = (By.XPATH,'//div[1]/div[1]/ul/li/span[text()="吴忠测试车场"]')
    listadd_type = (By.XPATH,'//form/div[2]/div[2]/div/div/div[1]/div/div/div[1]/input')
    listadd_type_choose = (By.XPATH,'')
    listadd_type_value = (By.XPATH,'//form/div[2]/div[2]/div/div/div[2]/div/div/input')
    listadd_money = (By.XPATH,'//form/div[3]/div[2]/div/div/div/input')
    listadd_distribute = (By.XPATH,'//form/div[4]/div[1]/div[1]/div/div[1]/div/div/div/input')
    listadd_distribute_value = (By.XPATH,'//form/div[4]/div[1]/div[1]/div/div[2]/div/div/input')
    listadd_use = (By.XPATH,'//form/div[4]/div[2]/div[1]/div/div[1]/div/div/div[1]/input')
    listadd_use_value = (By.XPATH,'//form/div[4]/div[2]/div[1]/div/div[2]/div/div/input')
    listadd_confirm = (By.XPATH,'//div/div[3]/div/button[1]/span')
    #优惠券充值
    listrecharge = (By.XPATH,'//table/tbody/tr[1]/td[9]/div/button[1]/span')
    listrecharge_name = (By.XPATH,'//form/div[1]/div[1]/div/div/div/div[1]/input')
    listrecharge_name_choose = (By.XPATH,'//div[1]/div[1]/ul/li/span[text()="九九"]')
    listrecharge_amount = (By.XPATH,'//form/div[1]/div[2]/div/div/div/input')
    listrecharge_money = (By.XPATH,'//form/div[3]/div/div/div/div/input')
    listrecharge_confirm = (By.XPATH,'//div/div[3]/div/button[1]/span')
    #查询优惠券
    listfind_search = (By.XPATH,'//form/div[4]/div/button[1]/span')
    listfind_reset = (By.XPATH,'//form/div[4]/div/button[2]/span')
    #删除优惠券
    listdel_choose = (By.XPATH,'//table/tbody/tr/td[2]/div')
    listdel_del = (By.XPATH,'//section/div/div[2]/div[2]/div[1]/div[2]/button/span/span')
    listdel_confirm = (By.XPATH,'//div/div[3]/button[2]/span')


    def park_discount_list(self):
        try:
            self.click_script_zong(OperaPage_Login.shrink)
        except:
            pass
        self.click_script_zong(Discounts_List_Zong.parkadmin)
        self.click_script_zong(Discounts_List_Zong.discountadmin)
        self.click_zong(Discounts_List_Zong.discountlist)

    def login_discount_list(self,head,username,password):
        self.log_zong(head)
        self.login_zonglogin(username,password)
        self.park_discount_list()

    def discount_list_add(self,head,username,password,name,choose,park_choose,type_choose,type_value,money,
                          unit,distribute_unit_choose,distribute_value,ues_unit_choose,use_value):
        self.login_discount_list(head,username,password)
        self.click_zong(Discounts_List_Zong.listadd)
        self.send_keys_presence_zong(Discounts_List_Zong.listadd_name,-1,name)
        if choose == 'one':
            self.click_zong(Discounts_List_Zong.listadd_park)
            park = (By.XPATH,park_choose)
            self.click_eles_presence_zong(park,-1)
        else:
            pass
        self.click_zong(Discounts_List_Zong.listadd_type)
        discount_type = (By.XPATH,type_choose)
        self.click_zong(discount_type)
        if name == '自动5元券':
            self.send_key_zong(Discounts_List_Zong.listadd_type_value,type_value)
        elif name == '自动10分券':
            self.send_key_zong(Discounts_List_Zong.listadd_type_value,type_value)
        else:
            pass
        self.send_key_zong(Discounts_List_Zong.listadd_money,money)
        self.click_zong(Discounts_List_Zong.listadd_distribute)
        distribute_unit = (By.XPATH,distribute_unit_choose)
        self.click_eles_presence_zong(distribute_unit,-1)
        if unit == '天':
            self.send_key_zong(Discounts_List_Zong.listadd_distribute_value,distribute_value)
        else:
            pass
        self.click_zong(Discounts_List_Zong.listadd_use)
        use_unit = (By.XPATH,ues_unit_choose)
        self.click_eles_presence_zong(use_unit,-1)
        if unit == '天':
            self.send_key_zong(Discounts_List_Zong.listadd_use_value,use_value)
        else:
            pass
        self.click_eles_presence_zong(Discounts_List_Zong.listadd_confirm,-1)

    def discount_list_recharge(self,head,username,password,choose,amount,money):
        self.login_discount_list(head,username,password)
        self.click_zong(Discounts_List_Zong.listrecharge)
        if choose == 'one':
            self.click_zong(Discounts_List_Zong.listrecharge_name)
            self.click_zong(Discounts_List_Zong.listrecharge_name_choose)
        else:
            pass
        self.send_key_zong(Discounts_List_Zong.listrecharge_amount,amount)
        self.click_zong(Discounts_List_Zong.listrecharge_money)
        self.send_key_zong(Discounts_List_Zong.listrecharge_money,Keys.CONTROL,'a')
        self.send_key_zong(Discounts_List_Zong.listrecharge_money,Keys.BACK_SPACE)
        self.send_key_zong(Discounts_List_Zong.listrecharge_money,money)
        self.click_zong(Discounts_List_Zong.listrecharge_confirm)

    def discount_list_find_search(self,head,username,password,ele,value):
        self.login_discount_list(head,username,password)
        find_redact = (By.XPATH,ele)
        self.send_key_zong(find_redact,value)
        self.send_key_zong(find_redact,Keys.DOWN,Keys.ENTER)
        self.click_zong(Discounts_List_Zong.listfind_search)

    def discount_list_find_reset(self):
        self.click_zong(Discounts_List_Zong.listfind_reset)

    def discount_list_del(self,head,username,password):
        self.login_discount_list(head,username,password)
        number = [1,2,3,4]
        for i in number:
            self.click_eles_presence_zong(Discounts_List_Zong.listdel_choose,i-1)
        self.click_zong(Discounts_List_Zong.listdel_del)
        sleep(1)
        self.click_zong(Discounts_List_Zong.listdel_confirm)