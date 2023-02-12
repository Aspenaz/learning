from unittest import TestCase 
from unittest.mock import patch, call 
from nose.tools import assert_equal
from Ch7.filter_funcs3 import filter_ints

class FilterIntsTestCase(TestCase): 
    
    @path('Ch7.filter_funcs3.is_positive')
    def test_filter_ints(self, is_positive_mock):
        # preparation
        v = [3, -4, 0, 5, 8] 
        # execution                       
        filter_ints(v)      
        # verification                       
        assert_equal([call(3), call(-4), call(0), call(5), call(8)], is_positive_mock.call_args_list)
        