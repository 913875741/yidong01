import os

from selenium.webdriver.support.wait import WebDriverWait


class Base(object):
    def __init__(self, driver):
        self.driver = driver

    def find_elements_o(self, loc, timeout=10, poll=0.5):
        # 定位一组元素
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(*loc))

    def find_element_o(self, loc, timeout=10, poll=0.5):
        # 定位单个元素
        """

        :param loc: 元祖类型 定位方式+属性值，类似(By.XPATH,"xpath语句") (By.ID,"id属性值")
        :param timeout:
        :param poll:
        :return:
        """
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(*loc))

    def click_element(self, loc):
        # loc ：元祖类型 (By.XPATH,"xpath语句") (By.ID,"id属性值")
        # 点击元素函数
        self.find_element_o(loc).click()

    def input_element(self, loc, text):
        """
        :param loc ：元祖类型 (By.XPATH,"xpath语句") (By.ID,"id属性值")
        :param text: 输入内容
        :return:
        """
        ele = self.find_element_o(loc)
        ele.clear()
        ele.send_keys(text)

    def input_element_noclear(self, loc, text):
        """
        :param loc ：元祖类型 (By.XPATH,"xpath语句") (By.ID,"id属性值")
        :param text: 输入内容
        :return:
        """
        ele = self.find_element_o(loc)
        ele.send_keys(text)

    def exit_ele(self,loc):
        try:
            self.find_element_o(loc)
            return True
        except Exception as e:
            return False
    @classmethod
    def get_root_path(cls):
        cur_path = os.getcwd()
        root_path = cur_path[:cur_path.find("yidong01") + len("yidong01")]
        return root_path
