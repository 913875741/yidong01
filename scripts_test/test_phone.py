import os
import sys

from Base.Init_driver import init_driver
from Page.PageObj import PageObj
from Base.Read_data import get_yml_data
import pytest,allure

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

def get_test_data():
    list_data = []
    test_data = get_yml_data("add_user.yml").get("test_data")
    for i in test_data.keys():
        list_data.append((i,test_data.get(i).get("name"),test_data.get(i).get("phonenum"),test_data.get(i).get("exp")))
    return list_data


class Test_phone(object):
    def setup_class(self):
        self.driver = init_driver()
        # self.user = Add_user(self.driver)
        self.user = PageObj(self.driver).reAddUser()
    def teardown_class(self):
        self.driver.quit()

    @pytest.fixture(scope="class")
    @allure.step("步骤一：点击切换到通讯录列表界面，准备新增联系人，该方法只执行一次")
    def tongxunlu(self):
        self.user.click_tongxunlu()

    @pytest.fixture()
    @allure.step("步骤二：点击新建按钮")
    def newuser(self):
        self.user.click_newuser()

    @pytest.mark.usefixtures("tongxunlu","newuser")
    @pytest.mark.parametrize("testnum,name,phone,exp",get_test_data())
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.step("步骤三：新增联系人，并返回到联系人列表")
    def test_new_user(self,testnum,name,phone,exp):

        self.user.shuru_user(name,phone)
        assert exp in self.user.ret_username_list()
