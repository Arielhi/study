#-*- coding:utf-8 -*-
"""
pytest中pytest.warns()：
1、断言告警信息
2、捕获告警信息，并进行判断
3、记录告警信息

#测试 test_warns.py
"""

#抛出告警示例
import pytest
import warnings
def fxn():
    warnings.warn("deprecated", DeprecationWarning)

def not_warn():
    pass

def warn_message():
    warnings.warn("user", UserWarning)
    warnings.warn("runtime", RuntimeWarning)


