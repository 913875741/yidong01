import os
import sys

from appium import webdriver
from Page.search import SearchPage
import pytest
sys.path.append(os.getcwd())

class Test_Searchx(object):
    def setup_class(self):
        desired_caps = {}
        # 设备信息
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.1'
        desired_caps['deviceName'] = '192.168.68.103:5555'
        # app的信息
        desired_caps['appPackage'] = 'com.android.settings'
        desired_caps['appActivity'] = '.Settings'
        # 中文输入允许
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        # 声明我们的driver对象
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.search_obj = SearchPage(self.driver)

    def teardown_class(self):
        self.driver.quit()

    @pytest.mark.run(order=1)
    def test_search01(self):
        self.search_obj.click_search()

    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("text", [1, 2, 3])
    def test_search02(self, text):
        self.search_obj.search_input(text)

    @pytest.mark.run(order=3)
    def test_search03(self):
        self.search_obj.click_return()
