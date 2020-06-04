from selenium.webdriver.common.by import By
from Base.Base import Base


class SearchPage(object):
    def __init__(self, driver):
        self.s_search = (By.ID, 'com.android.settings:id/search')
        self.s_text = (By.ID, 'android:id/search_src_text')
        self.s_back = (By.CLASS_NAME, 'android.widget.ImageButton')
        self.base_obj = Base(driver)

    def click_search(self):
        self.base_obj.click_element(self.s_search)

    def search_input(self, input_text):
        self.base_obj.input_element(self.s_text, input_text)

    def click_return(self):
        self.base_obj.click_element(self.s_back)