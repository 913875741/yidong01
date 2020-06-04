from Page.add_phoneuser_page import Add_user
class PageObj(object):
    def __init__(self,driver):
        self.driver = driver
    def reAddUser(self):
        return Add_user(self.driver)