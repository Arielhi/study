#-*- coding:utf-8 -*-
"""
存储参数化数据和函数
"""
import pytest

# 测试数据
is_leap = [4, 40, 400, 800, 1996, 2996]
is_not_leap = [1, 100, 500, 1000, 1999, 3000]
is_valueerror = [0, -4, -100, -400, -1996, -2000]
is_type_error = ['-4', '4', '100', 'ins', '**', '中文']

"""
@pytest.fixture():
由fixture装饰的函数可以作为参数传入其他函数
"""
# params需传入list
@pytest.fixture(params=is_leap)
def is_leap(request):
    return request.param
@pytest.fixture(params=is_type_error)
def is_type_error(request):
    return request.param

