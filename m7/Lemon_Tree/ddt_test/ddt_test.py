import unittest
from ddt import ddt,data,unpack


name_list = [{'name':'alex','sex':'male'},{'name':'mary','sex':'female'}]

@ddt
class TestDDT(unittest.TestCase):

    @data(*name_list)
    @unpack
    def test_data(self,name,sex):
        print('%s'%name)
        print('%s\n'%sex)

if __name__ == '__main__':
    unittest.main()
