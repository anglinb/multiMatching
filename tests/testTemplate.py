import random
import unittest

def listInt(points):
    for (i, point) in enumerate(points):
        points[i] = int(point)
    return points
def trunc(f, n):
    '''Truncates/pads a float f to n decimal places without rounding'''
    slen = len('%.*f' % (n, f))
    return float(str(f)[:slen])

class TestSequenceFunctions(unittest.TestCase):

    def test_example_test(self):
        self.assertEqual(2+2,4)
    
        
if __name__ == '__main__':
    unittest.main()
