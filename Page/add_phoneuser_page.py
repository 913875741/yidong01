import time,allure

import Page
from Base.Base import Base
class Add_user(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)

    # 点击切换到通讯录，只需要点一次
    def click_tongxunlu(self):
        self.click_element(Page.tongxunlu_btn)

    #点击新建
    def click_newuser(self):
        self.click_element(Page.newuser_btn)

    def shuru_user(self,name,phone):
        allure.attach('描述1', '输入联系人姓名')
        self.input_element(Page.input_name,name)
        allure.attach('描述2', '输入联系人电话号码')
        self.input_element(Page.input_phone,phone)
        allure.attach('描述3', '保存')
        self.click_element(Page.save)
        #判断用户是否成功录入,成功就返回
        if(self.exit_ele(Page.exit_edit)):
            allure.attach('描述4', '返回到联系人列表')
            self.driver.keyevent(4)

    def ret_username_list(self):
        users = self.find_elements_o(Page.list_username)
        return [i.text for i in users]