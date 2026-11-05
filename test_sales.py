import unittest
from sales import calculate_total_sales 

class TestSales(unittest.TestCase): 
    def test_calculate_total_sales(self):
        sales_list = [15000, 12000, 9000, 11000, 6000]
        expected_total = 53000
        self.assertEqual(calculate_total_sales(sales_list), expected_total) 
        
                         
         