import os
import sys

import yaml
from Base.Base import Base

# from Base.Read_data import get_yml_data
# data_list = []
# data = get_yml_data("add_user.yml")
# print(data)

curPath = os.path.abspath(os.path.dirname(__file__))
print(curPath)
rootPath = os.path.split(curPath)[0]
print(rootPath)
sys.path.append(rootPath)
print(os.getcwd())
# class Test_allure:
#     def setup(self):
#         pass
#
#     def teardown(self):
#         pass
#
#     def test_al(self):
#         assert 0