from selenium.webdriver.common.by import By
from Zong_TingChe.ZongBrowser import assist


class OperaPage_Login(assist):

    login_user = (By.NAME,'username')
    login_passwd = (By.NAME,'password')
    login_login = (By.XPATH,'//div/form/button/span')
    data_login_user = (By.XPATH,'//div/div/p[1]/input')
    data_login_passwd = (By.XPATH,'//div/div/p[2]/div/input')
    data_login_login = (By.XPATH,'//div/div/button')
    login_assert = By.XPATH
    shrink = (By.CLASS_NAME,'sidebar-title')
    open_shrink = (By.CLASS_NAME,'hamburger-container')
    def login_zongInput(self,username,passward):
        '''
        输入登录账号密码
        :param value:
        :return:
        '''
        self.send_key_zong(OperaPage_Login.login_user,username)
        self.send_key_zong(OperaPage_Login.login_passwd,passward)

    def login_zongClick(self):
        '''
        点击登录
        :return:
        '''
        self.click_zong(OperaPage_Login.login_login)

    # def login_zongLenAssert(self):
    #     '''
    #     判断元素是否唯一
    #     :return:
    #     '''
    #     ele = self.assert_amoun_zong(OperaPage_Login.login_assert)
    #     return ele
    #
    # def login_zongTextAssert(self):
    #     '''
    #     判断文本内容是否一致
    #     :return:
    #     '''
    #     ele = self.assert_text_zong(OperaPage_Login.login_assert)
    #     return ele

    def login_zonglogin(self,username,password):
        self.login_zongInput(username,password)
        self.login_zongClick()

    def dade_login_zonglogin(self,username,password):
        self.send_key_zong(OperaPage_Login.data_login_user,username)
        self.send_key_zong(OperaPage_Login.data_login_passwd,password)
        self.click_zong(OperaPage_Login.data_login_login)





