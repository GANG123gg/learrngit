from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Zong_TingChe.Zongoperationpage import OperaPage_Login
from time import sleep
import random


class Set_Tag(OperaPage_Login):
    systemadmin = (By.XPATH,'//div/ul/div[6]/li/div/span')
    systemtag = (By.XPATH,'//div/ul/div[6]/li/ul/div[1]/a/li/span')
    tagup = (By.XPATH,'//section/div/div[1]/div/div/div[1]/div/div/button/span')
    plateform_name = (By.XPATH,'//form/div[1]/form[1]/div/div/div/div[1]/div/div/input')
    plateform_picture_del = (By.XPATH,'//form/div[1]/form[1]/div/div/div/div[2]/ul/li/label/i')
    plateform_picture = (By.XPATH,'//form/div[1]/form[1]/div/div/div/div[2]/div/button/span')
    plateform_picture_xpath = r'F:\picture\picture\bmp\3.bmp'
    title_picture_del = (By.XPATH,'//form/div[2]/div[1]/div/div/div/div/div/ul/li/label/i')
    title_picture = (By.XPATH,'//form/div[2]/div[1]/div/div/div/div/div/div/button/span')
    title_picture_xpath = r'F:\picture\icon\ico\3.ico'
    data_name = (By.XPATH,'//form/div[1]/form[2]/div/div/div/div[1]/div/div/input')
    data_picture_del = (By.XPATH,'//form/div[1]/form[2]/div/div/div/div[2]/ul/li/label/i')
    data_picture = (By.XPATH,'//form/div[1]/form[2]/div/div/div/div[2]/div/button/span')
    data_picture_xpath = r'F:\picture\picture\bmp\3.bmp'
    tag_confirm = (By.XPATH,'//section/div/div/div[2]/button[1]/span')


    def system_tag(self):
        try:
            self.click_script_zong(OperaPage_Login.shrink)
        except:
            self.click_script_zong(OperaPage_Login.open_shrink)
            self.sav_creenshot()
        self.click_script_zong(Set_Tag.systemadmin)
        self.click_script_zong(Set_Tag.systemtag)
        self.click_zong(Set_Tag.tagup)

    def login_tag(self,head,username,password):
        self.log_zong(head)
        self.login_zonglogin(username,password)
        self.system_tag()

    def tag_update(self,platefrom_name,data_name):
        self.click_zong(Set_Tag.plateform_name)
        self.send_key_zong(Set_Tag.plateform_name,Keys.CONTROL,'a')
        sleep(1)
        self.send_key_zong(Set_Tag.plateform_name,Keys.BACK_SPACE)
        sleep(1)
        self.send_key_zong(Set_Tag.plateform_name,platefrom_name)
        sleep(1)
        self.click_zong(Set_Tag.plateform_picture_del)
        sleep(1)
        self.click_zong(Set_Tag.plateform_picture)
        sleep(1)
        self.file_up(Set_Tag.plateform_picture_xpath)
        sleep(3)
        self.click_zong(Set_Tag.title_picture_del)
        self.click_zong(Set_Tag.title_picture)
        sleep(1)
        self.file_up(Set_Tag.title_picture_xpath)
        sleep(3)
        self.send_key_zong(Set_Tag.data_name,Keys.CONTROL,'a')
        sleep(2)
        self.send_key_zong(Set_Tag.data_name,Keys.BACK_SPACE)
        sleep(1)
        self.send_key_zong(Set_Tag.data_name,data_name)
        sleep(1)
        self.click_zong(Set_Tag.data_picture_del)
        sleep(1)
        self.click_zong(Set_Tag.data_picture)
        sleep(1)
        self.file_up(Set_Tag.data_picture_xpath)
        sleep(3)
        self.click_zong(Set_Tag.tag_confirm)


