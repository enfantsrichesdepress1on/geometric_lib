import unittest
from rectangle.py import area, perimeter

class TestRectangleFunctions(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(10, 4), 40)
        self.assertEqual(area(5, 5), 25)
        self.assertEqual(area(0, 10), 0)
        self.assertEqual(area(7, 3), 21)

    def test_perimeter(self):
        self.assertEqual(perimeter(10, 4), 28)
        self.assertEqual(perimeter(5, 5), 20)
        self.assertEqual(perimeter(0, 10), 20)
        self.assertEqual(perimeter(7, 3), 20)

if __name__ == "__main__":
    unittest.main()
