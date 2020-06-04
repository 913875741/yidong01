from selenium.webdriver.common.by import By
from Base.Base import Base


class SearchPage(object):
    def __init__(self, driver):
        self.s_click_new = (By.ID, 'com.android.messaging:id/start_new_conversation_button')
        self.s_search_input = (By.ID, 'com.android.messaging:id/recipient_text_view')
        self.s_msg_input = (By.ID, 'com.android.messaging:id/compose_message_text')
        self.s_send = (By.ID, 'com.android.messaging:id/self_send_icon')
        self.base_obj = Base(driver)

    def click_new(self):
        self.base_obj.click_element(self.s_click_new)

    def search_input(self, input_text):
        self.base_obj.input_element_noclear(self.s_search_input, input_text)

    def msg_input(self, input_text):
        self.base_obj.input_element(self.s_msg_input, input_text)

    def click_send(self):
        self.base_obj.click_element(self.s_send)