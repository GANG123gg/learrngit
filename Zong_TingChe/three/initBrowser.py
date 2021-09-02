from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Browser():
    def __init__(self,driver):
        self.driver=driver
    def wait_until_element_visible(self,loc):
        '''
        定义显示等待时间，10s
        :param loc:
        :return:等待到的元素
        '''
        ele=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
        return ele
    def input_my(self,loc,value):
        '''
        定义一个输入框输入，输入前自动调用显示等待
        :param loc:
        :return:
        '''
        ele=self.wait_until_element_visible(loc)
        ele.send_keys(value)
    def click_my(self,loc):
        '''
        定义一个点击确认，点击前自动调用显示等待
        :return:
        '''
        ele=self.wait_until_element_visible(loc)
        ele.click()





