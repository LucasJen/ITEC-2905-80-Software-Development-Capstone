import unittest
from unittest import TestCase
import area



class TestShapeAreas(TestCase):

    def test_triangle_area(self):
        self.assertEqual(10, area.triange_area(4, 5))

        #values can be directly input into the assertion.

    def test_triangle_area_floating_point(self): 
        self.assertAlmostEqual(17.79875, area.triange_area(7.25, 4.91))
        # assertAlmostEqual can be used for floats.

    def test_negative_base_height_raises_value_error(self):
        with self.assertRaises(ValueError):
            area.triange_area(-3, 0)

    def test_base_height_zero(self):
        # test to check that 0 
        self.assertEqual(0, area.triange_area(0, 4))
        self.assertEqual(0, area.triange_area(0, 0))
        self.assertEqual(0, area.triange_area(3, 0))
        

if __name__ == "__main__":
    unittest.main()
