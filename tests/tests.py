import unittest
from core.methods import sound_missing 
class TestCancion(unittest.TestCase):

    def test_brr(self):
        self.assertEqual(sound_missing('brr'), 'fiu, cric-cric, brrah')

    def test_birip(self):
        self.assertEqual(sound_missing('birip'), 'trri-trri, croac')

    def test_plop(self):
        self.assertEqual(sound_missing('plop'), 'cric-cric, brrah')

    def test_croac(self):
        self.assertEqual(sound_missing('croac'), '')


if __name__ == '__main__':
    unittest.main()
