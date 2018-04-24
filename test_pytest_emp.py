#-*- coding:utf-8 -*-
import pytest

class TestDemo:
    # 加法
    @pytest.mark.parametrize("a, b, expected",[(1,2,3),(2,3,5),(3,4,8)])
    def test_add(self, a, b, expected):
        # 求和
        sum = a + b
        # 断言
        assert sum == expected

        # 减法
    @pytest.mark.parametrize("a, b, excepted",[(1,2,-1),(8,3,5),(3,4,8)])
    def test_sub(self, a, b, excepted):
        sub = a-b
        # 断言
        assert sub == excepted