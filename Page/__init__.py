from selenium.webdriver.common.by import By

"""
通讯录添加
"""
#点击通讯录
tongxunlu_btn = (By.XPATH,'//*[contains(@content-desc,"通讯录")]')
#点击新建按钮
newuser_btn = (By.ID,'com.android.dialer:id/floating_action_button')
#输入姓名
input_name = (By.XPATH,'//*[contains(@text,"姓名")]')
#输入电话
input_phone = (By.XPATH,'//*[contains(@text,"电话")]')
#提交保存
save = (By.ID,'com.android.contacts:id/menu_save')
#判断是否存在编辑按钮，用于区别是否成功录入
exit_edit = (By.ID,'com.android.contacts:id/menu_edit')
#用户列表中的保存名
list_username = (By.ID,'com.android.dialer:id/cliv_name_textview')