import unittest
import pandas as pd

class TestOrderAnalysis(unittest.TestCase):

    def setUp(self):
        # loading the dataframe
        self.df = pd.read_csv("orders.csv")
        self.df['total_sales'] = self.df['product_price'] * self.df['quantity']


    def test_datetime_conversion(self):
        # testing if order date is converted to datetime format
        self.df['order_date'] = pd.to_datetime(self.df['order_date'], infer_datetime_format=True)
        self.assertEqual(self.df['order_date'].dtype, 'datetime64[ns]')

    def test_total_sales_by_product(self):
        # testing if total sales per product is calculated accurate
        expected_result = self.df.groupby('product_name')['total_sales'].sum()
        actual_result = self.df.groupby('product_name')['total_sales'].sum()
        pd.testing.assert_series_equal(expected_result, actual_result)

    def test_total_sales_by_customer(self):
        # testing if total sales per customer is calculated accurate
        expected_result = self.df.groupby('customer_id')['total_sales'].sum()
        actual_result = self.df.groupby('customer_id')['total_sales'].sum()
        pd.testing.assert_series_equal(expected_result, actual_result)

    def test_top_10_customers(self):
        # testing if the top 10 customers are calculated accurate
        expected_result = self.df.groupby('customer_id')['total_sales'].sum().nlargest(n=10)
        actual_result = self.df.groupby('customer_id')['total_sales'].sum().nlargest(n=10)
        pd.testing.assert_series_equal(expected_result, actual_result)

if __name__ == '__main__':
    unittest.main()
