from appium import webdriver
from Page.sdmessg import SearchPage
import pytest,time,os,sys
sys.path.append(os.getcwd())
class Test_search:
    def setup_class(self):
        desired_caps = {}
        # 设备信息
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.1'
        desired_caps['deviceName'] = '192.168.68.103:5555'
        # app的信息
        desired_caps['appPackage'] = 'com.android.messaging'
        desired_caps['appActivity'] = '.ui.conversationlist.ConversationListActivity'
        # 中文输入允许
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        # 声明我们的driver对象
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.sdmsg_obj = SearchPage(self.driver)
    # def teardown_class(self):
    #     self.driver.quit()

    @pytest.mark.run(order=1)
    def test_01(self):
        self.sdmsg_obj.click_new()
        self.sdmsg_obj.search_input("11122223333")
        self.driver.keyevent(66)

    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("text",["ha","ll","o"])
    def test_02(self,text):
        # self.sdmsg_obj.search_input(text)
        # self.driver.keyevent(66)
        self.sdmsg_obj.msg_input(text)
        self.driver.get_screenshot_as_file("./screen/set_%s.png" % text)
        # self.sdmsg_obj.click_send()

    # @pytest.mark.run(order=3)
    # def test_03(self):
    #     self.sdmsg_obj.msg_input("haha")
    #     self.sdmsg_obj.click_send()

# if __name__ == '__main__':
#     pytest.main(["-s","./test-02.py"])