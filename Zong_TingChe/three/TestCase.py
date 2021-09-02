import unittest
from selenium import webdriver
from HTMLTestRunner import HTMLTestRunner
from Zong_TingChe.three.page_Login import login
from Zong_TingChe.three.initBrowser import Browser
class TestCase(unittest.TestCase,login):
    @classmethod
    def setUpClass(cls):
        #global driver,broswer
        cls.options = webdriver.ChromeOptions()
        cls.options.add_argument('--ignore-certificate-errors')
        cls.driver=webdriver.Chrome(chrome_options=cls.options)
        cls.driver.get('https://10.30.33.23')
        cls.broswer=Browser(cls.driver)
    #@classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_login(self):
        self.tenant_input('czz')
        self.user_input('czz')
        self.tenant_input('czz')
        self.login_click()
if __name__=='__main__':
    # suite=unittest.TestSuite()
    # suite.addTest(TestCase('test_login'))
    # runner=HTMLTestRunner(
    #     stream=open('report.html','wb'),
    #     verbosity=2,
    #     title='自动化测试报告',
    #     description='登陆测试',
    #     tester='czz'
    # )
    # runner.run(suite)
    unittest.main()

