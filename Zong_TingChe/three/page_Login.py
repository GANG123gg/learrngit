from selenium.webdriver.common.by import By
from Zong_TingChe.three.initBrowser import Browser
class login(Browser):
    tenant=(By.ID,'login_user')
    user=(By.ID,'login_username')
    passwd=(By.ID,'login_password')
    login_button=(By.ID,'login_confirm')
    def tenant_input(self,value):
        self.input_my(login.tenant,value)
    def user_input(self,value):
        self.input_my(login.user,value)
    def passwd_input(self,value):
        self.input_my(login.passwd,value)
    def login_click(self):
        self.click_my(login.login_button)


