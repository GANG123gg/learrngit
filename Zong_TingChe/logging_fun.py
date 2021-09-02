# coding = utf-8
# Author: Muzi
# Date: 2020/10/16 15:19


''''''
'''
1:创建日志器
    设置日志级别
2:创建处理器
    控制台、文件
    设置日志级别
3：创建格式器
    f1,f2,f3,f4
4:日志器添加处理器
5：处理器添加格式
6：日志器日志输出
    log.warning()
    log.error()
    log.inro()
'''
import logging

class log_object():
    def __init__(self):
        '''
        初始化日志器，设置日志级别为debug
        '''
        self.log=logging.getLogger() #创建日志器
        self.log.setLevel(level=logging.INFO) #设置日志级别
        self.log.handlers.clear()

    def set_Formatter(self):
        '''
        格式器，设置2中格式
        :return: 返还设置的2种格式
        '''
        self.f1 = logging.Formatter(fmt='[%(filename)s]: [%(levelname)s] %(asctime)s:>>> %(message)s ')
        self.f2 = logging.Formatter(fmt='%(asctime)s >> %(levelname)s >> 行号：%(lineno)d >>> %(message)s')
        return self.f1,self.f2

    def add_StreamHandler(self):
        '''
        设置控制台处理器
        :return: 无
        '''
        self.h = logging.StreamHandler()#控制台处理器
        self.h.setLevel(level=logging.INFO)
        self.log.addHandler(self.h) #日志器添加处理器
        self.h.setFormatter(self.set_Formatter()[0])#处理器添加格式器


    def add_FileHandler(self,file):#文件处理器
        '''
        设置文件处理器
        :param file: file就是要保存的日志文件名称
        :return:
        '''
        self.h=logging.FileHandler(file,mode='a',encoding='utf-8')
        self.h.setLevel(level=logging.INFO)
        self.log.addHandler(self.h) #日志器添加处理器
        self.h.setFormatter(self.set_Formatter()[1])#处理器添加格式器

    def get_log(self,file):
        '''
        执行了日志处理格式后，再返回日志器的方法
        :return: 日志器
        '''
        self.add_StreamHandler()
        self.add_FileHandler(file)
        return self.log





