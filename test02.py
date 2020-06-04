import pytest
class Test1:
    def setup_class(self):
        print("-------开始----》")
    def teardown_class(self):
        print("-------结束----》")
    def test_b(self):
        assert True
    def test_a(self):
        assert False