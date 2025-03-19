import unittest
from app import is_valid_email, calculate_area, process_list, convert_date_format, is_palindrome

class TestAppFunctions(unittest.TestCase):
    
    def setUp(self):
        self.valid_email = "test@example.com"
        self.invalid_email = "invalid-email"
        self.edge_case_email = "test@.com"
        
        self.circle_radius = 5
        self.rectangle_dims = (4, 5)
        self.triangle_dims = (3, 6)
        
        self.num_list = [3, 1, 4, 1, 5, 6]
        
        self.valid_date = "2025-03-19"
        self.invalid_date = "19-03-25"
        
        self.palindrome_text = "Madam, in Eden, I'm Adam"
        self.non_palindrome_text = "hello"
    
    def test_is_valid_email(self):
        self.assertTrue(is_valid_email(self.valid_email))
        self.assertFalse(is_valid_email(self.invalid_email))
        self.assertFalse(is_valid_email(self.edge_case_email))
    
    def test_calculate_area(self):
        self.assertAlmostEqual(calculate_area("circle", self.circle_radius), 78.53975)
        self.assertEqual(calculate_area("rectangle", *self.rectangle_dims), 20)
        self.assertEqual(calculate_area("triangle", *self.triangle_dims), 9)
        with self.assertRaises(ValueError):
            calculate_area("hexagon", 4)
    
    def test_process_list(self):
        self.assertEqual(process_list(self.num_list, "sort"), sorted(self.num_list))
        self.assertEqual(process_list(self.num_list, "filter_even"), [4, 6])
        with self.assertRaises(ValueError):
            process_list(self.num_list, "invalid_op")
    
    def test_convert_date_format(self):
        self.assertEqual(convert_date_format(self.valid_date, "%Y-%m-%d", "%d/%m/%Y"), "19/03/2025")
        self.assertEqual(convert_date_format("19-03-2025", "%d-%m-%Y", "%Y/%m/%d"), "2025/03/19")
        with self.assertRaises(ValueError):
            convert_date_format(self.invalid_date, "%d-%m-%Y", "%Y/%m/%d")
    
    def test_is_palindrome(self):
        self.assertTrue(is_palindrome(self.palindrome_text))
        self.assertTrue(is_palindrome("racecar"))
        self.assertFalse(is_palindrome(self.non_palindrome_text))

if __name__ == "__main__":
    unittest.main()
