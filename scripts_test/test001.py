import time

import pytest
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture(params=["刘备","设置日期","设置"])
def init_data(request):
    return request.param
class Test_1(object):

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

    def teardown_class(self):
        self.driver.quit()

    def wait_el(self,type,data):
        if type == "id":
            return WebDriverWait(self.driver,5,0.5).until(lambda x: x.find_element_by_id(data))
        if type == "xpath":
            return WebDriverWait(self.driver,5,0.5).until(lambda x: x.find_element_by_xpath(data))
        if type == "calss_name":
            return WebDriverWait(self.driver, 5, 0.5).until(lambda x: x.find_element_by_class_name(data))

    def test_search(self,init_data):
        self.wait_el("id","com.android.settings:id/search").click()
        el = self.wait_el("id","android:id/search_src_text")
        el.clear()
        el.send_keys(init_data)

        if "设置" == init_data:
            self.wait_el("xpath","//*[contains(@text,'设置时间')]").click()
            time.sleep(2)

    # @pytest.fixture()
    # def in_dex(self):
    #     el1 = self.wait_el("xpath","//*[contains(@text,'设置屏幕锁定')]")
    #     el2 = self.wait_el("xpath","//*[contains(@text,'通知')]")
    #     self.driver.drag_and_drop(el2,el1)
    #     el3 = self.wait_el("xpath","//*[contains(@text,'电池')]")
    #     self.driver.drag_and_drop(el3,el2)
    #     self.wait_el("xpath","//*[contains(@text,'位置信息')]").click()
    #
    # @pytest.mark.usefixtures("in_dex")
    # def test_change_mod(self):
    #     self.wait_el("xpath","//*[contains(@text,'模式')]").click()
    #     self.wait_el("xpath","//*[contains(@text,'仅限设备')]").click()
    #     self.wait_el("calss_name","android.widget.ImageButton").click()
    #     # el = self.driver.find_element_by_id("android:id/summary")
    #     #断言
    #     assert el.get_attribute("text") == "高精确度"
