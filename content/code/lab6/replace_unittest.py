import unittest

def replace(s):
    return s.replace('h', 'H', s.count('h')-1).replace('H', 'h', 1)

class ReplaceTest(unittest.TestCase):

    def test_1(self):
        self.assertEqual(replace('aaa'), 'aaa')
        self.assertEqual(replace('aaha'), 'aaha')
        self.assertEqual(replace('aahha'), 'aahha')
        self.assertEqual(replace('aahhha'), 'aahhha')
        self.assertEqual(replace('Haahhha'), 'Haahhha')

unittest.main(verbosity=2)
