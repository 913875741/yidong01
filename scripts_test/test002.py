import pytest
def aaa(a,b):
    if (a>b):
        return True
    else:
        return False
def bbb():
    return True
class Test_a(object):
    # @pytest.mark.skipif(aaa(1,2),reason="hahaha")
    # def test_a(self):
    #     assert False
    def test_b(self):
        assert True
    @pytest.mark.xfail(bbb(),reason="hehe")
    def test_c(self):
        assert True