from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Zong_TingChe.Zongoperationpage import OperaPage_Login
from time import sleep
import random


class Camera_Zong(OperaPage_Login):

    parkadmin = (By.XPATH,'//div/ul/div[4]/li/div/span')
    deviceadmin = (By.XPATH,'//div[1]/div[2]/div[1]/div/ul/div[4]/li/ul/div[2]/a/li/span')
    camera = (By.XPATH,'//div/div[1]/ul/li[2]/span[text()="相机"]')
    #新增相机
    cameraadd = (By.XPATH,'//div/div[2]/div[2]/div[1]/div[1]/button/span/span')
    cameraadd_park = (By.XPATH,'//form/div[1]/div[1]/div/div/div/div[1]/input')
    cameraadd_park_choose = (By.XPATH,'//div[1]/div[1]/ul/li/span[text()="吴忠测试车场"]')
    cameraadd_region = (By.XPATH,'//form/div[1]/div[2]/div/div/div/div[1]/input')
    cameraadd_region_choose = (By.XPATH,'//div[1]/div[1]/ul/li/span[text()="外区"]')
    cameraadd_channel = (By.XPATH,'//form/div[2]/div[1]/div/div/div/div[1]/input')
    cameraadd_channel_choose = (By.XPATH,'//div[1]/div[1]/ul/li/span[text()="外_1进"]')
    cameraadd_sequence = (By.XPATH,'//form/div[2]/div[2]/div/div/div/input')
    cameraadd_IP = (By.XPATH,'//form/div[3]/div[1]/div/div/div/input')
    cameraadd_type = (By.XPATH,'//form/div[3]/div[2]/div/div/div/div[1]/input')
    cameraadd_type_main = (By.XPATH,'//div[1]/div[1]/ul/li/span[text()="主相机"]')
    cameraadd_type_subsidiary = (By.XPATH,'//div[1]/div[1]/ul/li/span[text()="辅相机"]')
    cameraadd_type_surroundings = (By.XPATH,'//div[1]/div[1]/ul/li/span[text()="环境相机"]')
    cameraadd_confirm = (By.XPATH,'//div/div[3]/div/button[1]/span')
    #修改相机
    cameraupdate = (By.XPATH,'//table/tbody/tr[1]/td[11]/div/button[1]/span')
    cameraupdate_confirm = (By.XPATH,'//div/div[3]/div/button[1]/span')
    #查询相机信息
    camerafind_search = (By.XPATH,'//form/div[3]/div/button[1]/span')
    camerafind_reset = (By.XPATH,'//form/div[3]/div/button[2]/span')
    #删除相机
    cameradel_choose = (By.XPATH,'//table/tbody/tr[1]/td[2]/div')
    cameradel_del = (By.XPATH,'//div/div[2]/div[2]/div[1]/div[2]/button/span/span')
    cameradel_confirm = (By.XPATH,'//div/div[3]/button[2]/span')

    def park_camera(self):
        try:
            self.click_script_zong(OperaPage_Login.shrink)
        except:
            pass
        self.click_script_zong(Camera_Zong.parkadmin)
        self.click_script_zong(Camera_Zong.deviceadmin)
        self.click_zong(Camera_Zong.camera)

    def login_camera(self,head,username,password):
        self.log_zong(head)
        self.login_zonglogin(username,password)
        self.park_camera()

    def camera_add(self,head,username,password,choose,delete,sequence,ip,genre):
        self.login_camera(head,username,password)
        if delete == 'Y':
            self.camera_del()
        elif delete == 'N':
            pass
        self.click_zong(Camera_Zong.cameraadd)
        if choose == 'one':
            self.click_zong(Camera_Zong.cameraadd_park)
            self.click_zong(Camera_Zong.cameraadd_park_choose)
            self.click_zong(Camera_Zong.cameraadd_region)
            self.click_zong(Camera_Zong.cameraadd_region_choose)
            self.click_zong(Camera_Zong.cameraadd_channel)
            self.click_zong(Camera_Zong.cameraadd_channel_choose)
            self.send_key_zong(Camera_Zong.cameraadd_sequence,sequence)
            self.send_key_zong(Camera_Zong.cameraadd_IP,ip)
            self.click_zong(Camera_Zong.cameraadd_type)
            if genre == '主':
                self.click_zong(Camera_Zong.cameraadd_type_main)
            elif genre == '辅':
                self.click_zong(Camera_Zong.cameraadd_type_subsidiary)
            elif genre == '环境':
                self.click_zong(Camera_Zong.cameraadd_type_surroundings)
        elif choose == 'two':
            self.click_zong(Camera_Zong.cameraadd_park)
            self.click_zong(Camera_Zong.cameraadd_park_choose)
            self.click_zong(Camera_Zong.cameraadd_region)
            self.click_zong(Camera_Zong.cameraadd_region_choose)
            self.click_zong(Camera_Zong.cameraadd_channel)
            self.click_zong(Camera_Zong.cameraadd_channel_choose)
            self.send_key_zong(Camera_Zong.cameraadd_sequence,sequence)
            self.send_key_zong(Camera_Zong.cameraadd_IP,ip)
        elif choose == 'three':
            self.click_zong(Camera_Zong.cameraadd_park)
            self.click_zong(Camera_Zong.cameraadd_park_choose)
            self.click_zong(Camera_Zong.cameraadd_region)
            self.click_zong(Camera_Zong.cameraadd_region_choose)
            self.send_key_zong(Camera_Zong.cameraadd_sequence,sequence)
            self.send_key_zong(Camera_Zong.cameraadd_IP,ip)
            self.click_zong(Camera_Zong.cameraadd_type)
            if genre == '主':
                self.click_zong(Camera_Zong.cameraadd_type_main)
            elif genre == '辅':
                self.click_zong(Camera_Zong.cameraadd_type_subsidiary)
            elif genre == '环境':
                self.click_zong(Camera_Zong.cameraadd_type_surroundings)
        elif choose == 'four':
            self.click_zong(Camera_Zong.cameraadd_park)
            self.click_zong(Camera_Zong.cameraadd_park_choose)
            self.send_key_zong(Camera_Zong.cameraadd_sequence,sequence)
            self.send_key_zong(Camera_Zong.cameraadd_IP,ip)
            self.click_zong(Camera_Zong.cameraadd_type)
            if genre == '主':
                self.click_zong(Camera_Zong.cameraadd_type_main)
            elif genre == '辅':
                self.click_zong(Camera_Zong.cameraadd_type_subsidiary)
            elif genre == '环境':
                self.click_zong(Camera_Zong.cameraadd_type_surroundings)
        elif choose == 'five':
            self.send_key_zong(Camera_Zong.cameraadd_sequence,sequence)
            self.send_key_zong(Camera_Zong.cameraadd_IP,ip)
            self.click_zong(Camera_Zong.cameraadd_type)
            if genre == '主':
                self.click_zong(Camera_Zong.cameraadd_type_main)
            elif genre == '辅':
                self.click_zong(Camera_Zong.cameraadd_type_subsidiary)
            elif genre == '环境':
                self.click_zong(Camera_Zong.cameraadd_type_surroundings)
        self.click_zong(Camera_Zong.cameraadd_confirm)

    def camera_update(self,head,username,password,choose,ele,values):
        self.login_camera(head,username,password)
        self.click_zong(Camera_Zong.cameraupdate)
        camera_redact = (By.XPATH,ele)
        if choose == 'one':
            self.send_key_zong(camera_redact,Keys.CONTROL,'a')
            self.send_key_zong(camera_redact,Keys.BACK_SPACE)
        elif choose == 'two':
            self.send_key_zong(camera_redact,Keys.CONTROL,'a')
            self.send_key_zong(camera_redact,Keys.BACK_SPACE)
            self.send_key_zong(camera_redact,values)
        self.click_zong(Camera_Zong.cameraupdate_confirm)

    def camera_find_search(self,head,username,password,ele,values):
        self.login_camera(head,username,password)
        camera_redact = (By.XPATH,ele)
        self.send_key_zong(camera_redact,values)
        self.click_zong(Camera_Zong.camerafind_search)

    def camera_find_reset(self):
        self.click_zong(Camera_Zong.camerafind_reset)

    def camera_del(self):
        self.click_zong(Camera_Zong.cameradel_choose)
        self.click_zong(Camera_Zong.cameradel_del)
        self.click_zong(Camera_Zong.cameradel_confirm)

    def camera_delete(self,head,username,password):
        self.login_camera(head,username,password)
        self.camera_del()