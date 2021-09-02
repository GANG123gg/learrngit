from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Zong_TingChe.Zongoperationpage import OperaPage_Login
from time import sleep




class ShopAdmin_Zong(OperaPage_Login):

    uesradmin = (By.XPATH,'//div/div[1]/div[2]/div[1]/div/ul/div[3]/li/div/span')
    shopadmin = (By.XPATH,'//div/div[1]/div[2]/div[1]/div/ul/div[3]/li/ul/div[3]/a/li/span')
    #新增商家账号
    shopadd = (By.XPATH,'//div/div[2]/div/div[1]/div[1]/button/span')
    shopadd_shopname = (By.XPATH,'//div/div[2]/form/div/div[1]/div/div/div/input')
    shopadd_park = (By.XPATH,'//div/div[2]/form/div/div[2]/div/div/div/div[1]/input')
    shopadd_park_list = (By.XPATH,'//div[1]/div[1]/ul/li/span[text()="吴忠测试车场"]')
    shopadd_personname = (By.XPATH,'//div/div[2]/form/div/div[3]/div/div/div/input')
    shopadd_phone = (By.XPATH,'//div/div[2]/form/div/div[4]/div/div/div/input')
    shopadd_discount = (By.XPATH,'//div/div[2]/form/div/div[5]/div/div/div/input')
    shopadd_account = (By.XPATH,'//div/div[2]/form/div/div[6]/div/div/div/input')
    shopadd_confirm = (By.XPATH,'//div/div[3]/div/button[1]/span')
    #编辑商家账号
    shopupdate = (By.XPATH,'//div/div[2]/div/div[2]/div[3]/table/tbody/tr[1]/td[10]/div/button/span')
    shopupdate_confirm = (By.XPATH,'//div/div[3]/div/button[1]/span')
    #查询商家账号信息
    shopfind_search = (By.XPATH,'//div/div[1]/form/div[4]/div/button[1]/span')
    shopfind_reset = (By.XPATH,'//div/div[1]/form/div[4]/div/button[2]/span')
    #删除商家账号
    shopdel_account = (By.XPATH,'//div/div[2]/div/div[2]/div[3]/table/tbody/tr[1]/td[2]/div')
    shopdel_del = (By.XPATH,'//div/div[2]/div/div[1]/div[2]/button/span')
    shopdel_confirm = (By.XPATH,'//div/div[3]/button[2]/span')

    def usershop(self):
        try:
            self.click_script_zong(OperaPage_Login.shrink)
        except:
            self.click_script_zong(OperaPage_Login.open_shrink)
            self.sav_creenshot()
        self.click_script_zong(ShopAdmin_Zong.uesradmin)
        self.click_script_zong(ShopAdmin_Zong.shopadmin)

    def login_shop(self,head,username,password):
        self.log_zong(head)
        self.login_zonglogin(username,password)
        self.usershop()

    def shop_add_one(self,head,username,password,choose,shopname,personname,phone,discount,account):
        self.login_shop(head,username,password)
        self.click_zong(ShopAdmin_Zong.shopadd)
        self.send_key_zong(ShopAdmin_Zong.shopadd_shopname,shopname)
        if choose == 'one':
            self.click_zong(ShopAdmin_Zong.shopadd_park)
            self.click_zong(ShopAdmin_Zong.shopadd_park_list)
        elif choose == 'two':
            pass
        self.send_key_zong(ShopAdmin_Zong.shopadd_personname,personname)
        self.send_key_zong(ShopAdmin_Zong.shopadd_phone,phone)
        self.send_key_zong(ShopAdmin_Zong.shopadd_discount,discount)
        self.send_key_zong(ShopAdmin_Zong.shopadd_account,account)
        self.click_zong(ShopAdmin_Zong.shopadd_confirm)

    def shop_update_one(self,head,username,password,choose,ele,values):
        self.login_shop(head,username,password)
        self.click_script_zong(ShopAdmin_Zong.shopupdate)
        shop_redact_ele = (By.XPATH,ele)
        sleep(1)
        self.send_key_zong(shop_redact_ele,Keys.CONTROL,'a')
        self.send_key_zong(shop_redact_ele,Keys.BACK_SPACE)
        if choose == 'one':
            pass
        elif choose == 'two':
            self.send_key_zong(shop_redact_ele,values)
        self.click_zong(ShopAdmin_Zong.shopupdate_confirm)

    def shop_check_search(self,head,username,password,loca,ele,value):
        self.login_shop(head,username,password)
        ments = (loca,ele)
        self.send_key_zong(ments,value)
        self.click_zong(ShopAdmin_Zong.shopfind_search)

    def shop_check_reset(self):
        sleep(1)
        self.click_zong(ShopAdmin_Zong.shopfind_reset)
        sleep(1)
    def shop_del_one(self,head,username,password):
        self.login_shop(head,username,password)
        self.click_zong(ShopAdmin_Zong.shopdel_account)
        self.click_zong(ShopAdmin_Zong.shopdel_del)
        self.click_zong(ShopAdmin_Zong.shopdel_confirm)