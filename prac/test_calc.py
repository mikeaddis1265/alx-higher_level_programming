import unittest
import example

class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(example.add(10, 5), 15)
        self.assertEqual(example.add(-1, -1), -2)
        self.assertEqual(example.add(10, -2), 8)
    
    def test_sub(self):
        self.assertEqual(example.sub(10, 5), 5)
        self.assertEqual(example.sub(-1, -1), 0)
        self.assertEqual(example.sub(10, -2), 12)

    def test_div(self):
        self.assertEqual(example.div(10, 5), 2)
        self.assertEqual(example.div(-1, -1), 1)
        self.assertEqual(example.div(10, -2), -5)
        self.assertEqual(example.div(5, 2), 2 )
        self.assertRaises(ValueError, example.div, 10 , 0)
    
     




if __name__ =="__main__":
    unittest.main()
