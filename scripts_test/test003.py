import pytest


def re_list():
    my_datas = []
    # my_datas.append((1,2,3))
    with open("D:\\Dev\\PythonProject\\yidong01\\scripts_test\\data.txt", "r", encoding="utf-8") as f:
        for i in f.readlines():
            print(i)
            data = i.split("=")[-1]
            print(data)
            # e = eval(data)
            my_datas.append(eval(data))
    # print(my_datas)
    return my_datas
    # return [(1,2,3)]

class Test_param(object):
    @pytest.mark.parametrize("a,b,c", re_list())
    def test_param(self, a,b,c):
        # print("haha")
        assert a+b==c


#
if __name__ == "__main__":
    a = re_list()
    print(a)
    print(type(a))
    # for i in a:
    #     print(type(i))
    #     print(i)