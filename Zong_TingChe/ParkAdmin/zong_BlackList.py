from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Zong_TingChe.Zongoperationpage import OperaPage_Login
from time import sleep



class BlackList(OperaPage_Login):

    parkadmin = (By.XPATH,'//div/ul/div[4]/li/div/span')
    blacklist = (By.XPATH,'//div/ul/div[4]/li/ul/div[6]/a/li/span')
    #新增黑名单
    blackadd = (By.XPATH,'//section/div/div[2]/div[1]/div[1]/button/span/span')
    add_park = (By.XPATH,'//form/div[1]/div[1]/div/div/div/div[2]/input')
    add_plate_number = (By.XPATH,'//form/div[1]/div[2]/div/div/div/input')
    add_remarks = (By.XPATH,'//form/div[2]/div/div/div/div/input')
    add_confirm = (By.XPATH,'//div/div[3]/div/button[1]/span')
    #导入
    blackimport = (By.XPATH,'//section/div/div[2]/div[1]/div[2]/button/span/span')
    import_park = (By.XPATH,'//div/div[2]/form/div[1]/div/div/div[1]/input')
    import_file = (By.XPATH,'//form/div[2]/div/div/div/button/span')
    import_address = r'E:\xjwjj\2020-云停车\plateImportTemplat\blacklistTemplate.xlsx'
    import_confirm = (By.XPATH,'//div/div[3]/div/button[1]/span')
    #查询
    find_park = (By.XPATH,'//form/div[1]/div/div/div/input')
    find_palte_number = (By.XPATH,'//section/div/div[1]/form/div[2]/div/div/input')
    find_search = (By.XPATH,'//section/div/div[1]/form/div[3]/div/button[1]/span')
    find_reset = (By.XPATH,'//section/div/div[1]/form/div[3]/div/button[2]/span')
    #删除
    blackdel = (By.XPATH,'//section/div/div[2]/div[1]/div[5]/button/span/span')
    del_confirm = (By.XPATH,'//div/div[3]/button[2]/span')



    def park_blacklist(self):
        try:
            self.click_script_zong(OperaPage_Login.shrink)
        except:
            self.click_script_zong(OperaPage_Login.open_shrink)
            self.sav_creenshot()
        self.click_script_zong(BlackList.parkadmin)
        self.click_script_zong(BlackList.blacklist)
        sleep(2)

    def login_blacklisr(self,head,username,password):
        self.log_zong(head)
        self.login_zonglogin(username,password)
        self.park_blacklist()

    def blacklist_add(self,choose,path,plate,remarks):
        self.click_zong(BlackList.blackadd)
        if choose == 'one':
            self.click_zong(BlackList.add_park)
            add_park_choose = (By.XPATH,path)
            self.click_eles_presence_zong(add_park_choose,-1)
        elif choose == 'two':
            pass
        self.send_key_zong(BlackList.add_plate_number,plate)
        self.send_key_zong(BlackList.add_remarks,remarks)
        self.click_zong(BlackList.add_confirm)

    def blacklist_import(self,choose,path):
        self.click_zong(BlackList.blackimport)
        if choose == 'one':
            self.click_zong(BlackList.import_park)
            import_park_choose = (By.XPATH,path)
            self.click_eles_presence_zong(import_park_choose,-1)
        elif choose == 'two':
            pass
        self.click_zong(BlackList.import_file)
        self.file_up(BlackList.import_address)
        self.click_zong(BlackList.import_confirm)

    def blacklist_out(self):
        pass

    def blacklist_find_search(self,choose,path,plate):
        if choose == 'one':
            self.click_zong(BlackList.find_park)
            find_park_choose = (By.XPATH,path)
            self.click_zong(find_park_choose)
        elif choose == 'two':
            self.send_key_zong(BlackList.find_palte_number,plate)
        self.click_zong(BlackList.find_search)

    def blacklist_find_reset(self):
        sleep(2)
        self.click_zong(BlackList.find_reset)
        sleep(1)

    def blacklist_del(self,ele):
        del_plate = (By.XPATH,ele)
        del_list = [0,1,2,3,4]
        for i in del_list:
            self.click_eles_presence_zong(del_plate,i)
            sleep(1)
        self.click_zong(BlackList.blackdel)
        self.click_zong(BlackList.del_confirm)