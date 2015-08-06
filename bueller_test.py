import sys
import unittest
from bueller import *

class TestBueller(unittest.TestCase):

    def setUp(self):
        self.names = ['Araceli Tews', 'Astrid Maxson', 'Bessie Myrie', 'Chaya Berryman', 'Cliff Okeefe', 'Deetta Gillian', 'Edmundo Vitolo', 'Gilberte Ragin', 'Gustavo Wethington', 'Howard Luby', 'Lasonya Strong', 'Loreta Gilliard', 'Matt Couchman', 'Merissa Ferro', 'Mickey Turnbough', 'Minnie Curl', 'Raye Cadet', 'Stan Jawad', 'Thao Hinton', 'Werner Paek']
        self.lasts = ['Berryman, Chaya', 'Cadet, Raye', 'Couchman, Matt', 'Curl, Minnie', 'Ferro, Merissa', 'Gillian, Deetta', 'Gilliard, Loreta', 'Hinton, Thao', 'Jawad, Stan', 'Luby, Howard', 'Maxson, Astrid', 'Myrie, Bessie', 'Okeefe, Cliff', 'Paek, Werner', 'Ragin, Gilberte', 'Strong, Lasonya', 'Tews, Araceli', 'Turnbough, Mickey', 'Vitolo, Edmundo', 'Wethington, Gustavo']
        self.function_defined()

    def function_defined(self):
        try:
            self.assert_(sort_by_last_name is not None)
        except NameError as e:
            self.fail("Define a function called sort_by_last_name")
            self.skipTest(TestBueller)

    def test_return(self):
        result = sort_by_last_name(["test", "test2"])
        self.assertIsInstance(result,list,"sort_by_last_name should return an array")

    def test_sorting(self):
        result = sort_by_last_name(self.names)
        self.assertEqual(result, self.lasts)

if __name__ == '__main__':
    unittest.main()
