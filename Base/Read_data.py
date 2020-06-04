from Base.Base import Base
import os,yaml,sys

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

def get_yml_data(filename):
    file_path = Base.get_root_path() + os.sep + "Data" + os.sep + filename
    with open(file_path, "r", encoding="utf-8") as f:
        data = yaml.load(f, yaml.FullLoader)
        return data
        # test_data = data.get("test_data")
        # for i in test_data.keys():
        #     print("编号：%s \nname:%s,age:%s" % (i, test_data.get(i).get("name"), test_data.get(i).get("age")))