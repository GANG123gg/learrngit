'''
定义常用方法：点击、输入、等待时间、日志、截图、断言、切换frame、鼠标移动
'''
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Zong_TingChe.logging_fun import log_object
import time
import os
from pywinauto import Desktop
from datetime import datetime
import traceback
from PIL import Image
class ZongBrowser():

    def __init__(self,driver):
        self.driver = driver

    def click_zong(self,loca):
        '''
        封装点击方法
        :param loca:
        :return:
        '''
        ele = self.wait_until_ele(loca)
        ele.click()

    def click_eles_zong(self,loca,number):
        '''
        定位元素组进行点击
        :param loca:
        :return:
        '''
        eles = self.wait_until_eles(loca)
        eles[number].click()

    def click_eles_presence_zong(self,loca,number):
        '''
        定位元素组进行点击
        :param loca:
        :return:
        '''
        eles = self.wait_until_presence_eles(loca)
        eles[number].click()

    def click_find_eles_xpath_zong(self,loca,number):
        '''
        定位元素组
        :return:
        '''
        eles = self.driver.find_elements_by_xpath(loca)
        eles[number].click()

    def click_script_zong(self,loca):
        '''
        封装script点击方法
        :return:
        '''
        ele = self.wait_until_ele(loca)
        self.driver.execute_script("arguments[0].click();", ele)

    def click_script_eles_zong(self,loca,number):
        '''
        封装script元素组点击方法
        :return:
        '''
        eles = self.wait_until_eles(loca)
        self.driver.execute_script("arguments[0].click();", eles[number])

    def send_key_zong(self,loca,*value):
        '''
        封装输入方法
        '''
        ele = self.wait_until_ele(loca)
        ele.send_keys(value)

    def send_keys_zong(self,loca,number,*value):
        '''
        封装获取到多个相同元素的输入方法
        :param loca:
        :param value:
        :return:
        '''
        eles = self.wait_until_eles(loca)
        eles[number].send_keys(value)

    def send_keys_presence_zong(self,loca,number,*value):
        '''
        定位元素组进行输入
        :return:
        '''
        eles = self.wait_until_presence_eles(loca)
        eles[number].send_keys(value)

    def send_key_keyboard_zong(self,loca):
        '''
        封装键盘值输入方法
        :param loca:
        :return:
        '''

        ele = self.wait_until_ele(loca)
        ele.send_keys(Keys.DOWN,Keys.DOWN,Keys.RIGHT,Keys.DOWN,Keys.DOWN,Keys.RIGHT,Keys.DOWN,Keys.DOWN,Keys.ENTER)

    def clear_zong(self,loca):
        '''
        封装清除方法
        :param loca:
        :return:
        '''
        ele = self.driver.find_element(loca)
        ele.clear()

    def elements_zong(self,ele):
        eles = self.driver.find_elements_by_xpath(ele)
        return eles

    def wait_until_ele(self,loca):
        '''
        显式等待时间,定位到该元素
        '''
        ele = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loca),message='未定位到元素')
        return ele

    def wait_until_eles(self,loca):
        '''
        显式等待时间,定位到多个相同元素
        :param loca:
        :return:
        '''
        ele = WebDriverWait(self.driver,10).until(EC.visibility_of_all_elements_located((loca)),message='未定位到元素')
        return ele

    def wait_until_presence_eles(self,loca):
        '''
        显式等待时间,定位到多个相同元素
        :param loca:
        :return:
        '''
        eles = WebDriverWait(self.driver,10).until(EC.presence_of_all_elements_located(loca),message='未定位到元素')
        return eles

    def wait_until_title(self,name):
        '''
        判断title是否正确
        :return:
        '''
        res = WebDriverWait(self.driver,10).until(EC.title_is(name),message='未获取到title名称')
        return res

    def wait_until_elements(self,loc):
        '''
        显式等待时间,定位元素在页面出现的次数
        :param loc:
        :return:
        '''
        ele = len(WebDriverWait(self.driver,10).until(lambda x:x.find_elements(*loc)))
        return ele

    def log_zong(self,value):
        '''
        web自动化日志
        :return:
        '''
        logger = log_object()
        log = logger.get_log(u'E:/xjwjj/python/ui自动化测试日志记录.log')
        logger_zong = log.info(value)
        return logger_zong

    def log_port_zong(self,value):
        '''
        接口自动化日志
        :return:
        '''
        logger = log_object()
        log = logger.get_log(u'E:/xjwjj/python/接口自动化测试日志记录.log')
        logger_zong = log.info(value)
        return logger_zong


class assist(ZongBrowser):

    def assert_amoun_zong(self,zong_loca,zong_element):
        '''
        定位元素在页面出现的次数
        :param zong_ele:
        :return:
        '''
        zong_ele = (zong_loca,zong_element)
        ele_list_amoun = self.wait_until_presence_eles(zong_ele)
        return ele_list_amoun
        #self.driver.assertEqual(len(ele_list_amoun),1)

    def assert_text_zong(self,zong_loca,zong_element):
        '''
        断言文本是否一致
        :param zong_ele:
        :param text:
        :return:
        '''
        zong_ele = (zong_loca,zong_element)
        ele_list_text = self.wait_until_ele(zong_ele).text
        return ele_list_text
        #self.driver.assertEqual(ele_list_text,text)


    def iframe_zong_into(self,loca):
        '''
        切换进iframe
        :return:
        '''
        ele = self.wait_until_ele(loca)
        self.driver.switch_to_frame(ele)

    def iframe_zong_out(self):
        '''
        切换出iframe
        :param loca:
        :return:
        '''
        self.driver.switch_to_default_content()

    def currentDate(self):
        '''
        生成当前日期字符串
        :return:
        '''
        date = time.localtime()
        return '-'.join([str(date.tm_year),str(date.tm_mon),str(date.tm_mday)])

    def currentTime(self):
        '''
        生成当前时间字符串
        :return:
        '''
        date = time.localtime()
        return '-'.join([str(date.tm_hour), str(date.tm_min),str(date.tm_sec)])

    def createDir(self):
        '''
        创建当前日期和当前时间目录
        :return:
        '''
        path = os.path.dirname(os.path.abspath(__file__))
        dateDir = os.path.join(path,self.currentDate())
        #如果当前日期目录不存的话就创建
        if not os.path.exists(dateDir):
                os.mkdir(dateDir)
        timeDir = os.path.join(path,self.currentTime())
        #如果当前日期目录存在的话就创建时间目录
        if os.path.exists(dateDir):
            pass
        return timeDir

    def takeScreenshot(self,driver,savePath,pictureName):
        '''
        截图
        '''
        picturePath = os.path.join(savePath, pictureName+'.png')
        try:
            self.driver.get_screenshot_as_file(picturePath)
        except:
            print(traceback.print_exc())

    def full_screen_zong(self):
        '''
        全屏截图
        :return:
        '''

        self.driver.get_screenshot_as_file("截图\\"+self.time_format()+".png")

    def sav_creenshot(self):
        '''
        截图
        '''
        now=time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time())) # 截图保存的文件名格式
        pic_path = "./"+now+'_screen.png' # 截图保存的路径
        # print(pic_path)
        self.driver.save_screenshot(pic_path) # 调用Driver的截图保存功能



    def element_screen_zong(self,loca):
        '''
        区域截图
        :return:
        '''
        element = self.wait_until_ele(loca)
        self.driver.save_screenshot("截图\\full.png")
        x_piont = element.location['x']
        y_piont = element.location['y']
        element_width = x_piont + element.size['width']
        element_height = x_piont + element.size['height']
        picture = Image.OPEN("截图\\full.png")

        '''
        crop()--  一个显式的参数：一个4元组
          Image.crop(box=None):图像返回一个矩形区域,box是一个四元组 限定所述左，上，右，和下像素坐标
          参数：box--裁剪矩形，作为（左，上，右，下）-tuple;返回类型：Image；返回：一个Image对象
          所以你应该重写它：
          img.crop((414,122,650,338))
          #        ^    4-tuple    ^
        '''
        picture = picture.crop((x_piont, y_piont, element_width, element_height))
        picture.save("截图\\"+self.time_format()+".png")

    def file_up(self,address):
        '''
        文件图片上传
        '''
        self.app = Desktop()
        dig = self.app["打开"]
        time.sleep(2)
        dig["文件名(&N):Edit1"].type_keys(address)
        time.sleep(1)
        dig["打开(&O)"].click()

    def time_format(self):
        '''
        时间格式进行格式化
        :return:
        '''
        current_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        return current_time
