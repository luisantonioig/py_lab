from math import factorial as fact
import math
import unittest
import hypothesis.strategies as st
from hypothesis import given
from python_lab_2 import *

class TestPyLab2(unittest.TestCase):

    @given(st.lists(st.integers()))
    def test_may_20(self, l):
        assert len(list(may_20(l))) + 1 == len(list(may_20(l + [21])))
        assert len(list(may_20(l))) == len(list(may_20(l + [3])))

    @given(st.lists(st.text()), st.integers())
    def test_word_filter(self, ls, n):
        assert word_filter(ls, n) == word_filter(list(word_filter(ls, n)), n)

    @given(st.text())
    def test_string_length(self, s):
        assert len(s) == string_length(s)

    @given(st.text(min_size=1,max_size=1))
    def test_is_vocal(self,char):
        assert len(char) == 1
        if is_vocal(char):
        	assert is_vocal(char) != is_vocal(chr(ord(char) + 1))

    @given(st.integers(min_value=1))
    def test_is_leap_year(self, year):
        assert (is_leap_year(year) == True) or (is_leap_year(year) == False)

    @given(st.text())
    def test_has_uppercase(self, text):
        assert has_uppercase(text) != has_uppercase(text + "A")

    @given(st.text())
    def test_vocales_consonantes(self, s):
        assert contar_consonantes(s) + contar_vocales(s) == len(s)

    @given(st.lists(st.integers(min_value = 0, max_value = 10000)))
    def test_sqare(self, lis):
        assert lis == list(map(lambda x: math.sqrt(x), square(lis)))

    @given(st.integers(min_value=1), st.integers(min_value=1))
    def test_is_prime(self, n, div):
        if is_prime(n):
            if div != 1 and div != n:
                assert n % div != 0
            else:
                assert n % div == 0

    @given(st.integers(max_value = 100, min_value = 0))
    def test_factorial(self, n):
        assert factorial(n) == fact(n)

if __name__ == '__main__':
    unittest.main()
