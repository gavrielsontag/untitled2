import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        fracture1 = 5*6
        fracture2 = 3*10
        fracture3 = 60*.5
        self.assertEqual(fracture1, fracture2, fracture3)

if __name__ == '__main__':
    unittest.main()
