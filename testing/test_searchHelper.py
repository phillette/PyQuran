"""unittest module for searchHelper.py
"""
import unittest

# Adding another searching path
from sys import path
path.append('../tools/')
path.append('../core/')

from searchHelper import *

class Testing_searchHelper(unittest.TestCase):

    def test_count_spaces_before_index(self):
        self.assertEqual(count_spaces_before_index('', 0), 0)
        self.assertEqual(count_spaces_before_index('01 34 6 8', 8), 3)
        self.assertEqual(count_spaces_before_index(' ', 1), 1)


    def test_get_string_taskeel(self):
        x = 'ﺐِﺴﻣ ﺎﻠﻠﻫِ ﺎﻟﺮّﺤﻤﻧ ﺎﻟﺮَﺤﻴﻣ'
        self.assertEqual(len(get_string_taskeel(x)), 7)


if __name__ == '__main__':
    unittest.main()