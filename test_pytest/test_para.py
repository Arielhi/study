#-*- coding:utf-8 -*-

import pytest
from test_pytest import is_leap_year

class TestPara():
    def test_is_leap(self,is_leap):
        assert is_leap_year.is_leap_year(is_leap)==True
    def test_is_typeerror(self, is_type_error):
        with pytest.raises(TypeError):
            is_leap_year.is_leap_year(is_type_error)

    """
    pytest.mark.parametrize():
    采用标记函数参数化
    """
    # 测试用例参数传入year中
    @pytest.mark.parametrize('year, expected',
        [(1,False), (4,True), (100,False), (400,True), (500,True)])
    def test_is_leap(self,year,expected):
        assert is_leap_year.is_leap_year(year) == expected

    @pytest.mark.parametrize('year, expected',
        [(0, ValueError), ('-4', TypeError),
         (-4, ValueError), ('ss', TypeError), (100, ValueError)])
    def test_is_typeerror(self, year, expected):
        if expected == ValueError:
            with pytest.raises(ValueError) as excinfo:
                is_leap_year.is_leap_year(year)
            assert excinfo.type == expected
        else:
            with pytest.raises(TypeError) as excinfo:
                is_leap_year.is_leap_year(year)
            assert excinfo.type == expected