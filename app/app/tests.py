'''
Sample tests
'''
from django.test import SimpleTestCase
from app import calc

# test calculate module
class CalcTests(SimpleTestCase):
    ''' Test that two numbers are added together '''
    def test_add_number(self):

        self.assertEqual(calc.add(3, 8), 11)
    def test_subtract_numers(self):
        res = calc.subtract(10, 15)
        self.assert_(res, 5)