import unittest
from client3 import getDataPoint

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    # Calculating the expected result manually
    expected_result = ('ABC', 120.48, 121.2, (120.48 + 121.2) / 2)

    # Calling the function to get the actual result
    actual_result = getDataPoint(quotes[0])

    # Added the assertion
    self.assertEqual(actual_result, expected_result)

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    # Calculating the expected result manually
    expected_result = ('ABC', 120.48, 119.2, (120.48 + 119.2) / 2)

    # Calling the function to get the actual result
    actual_result = getDataPoint(quotes[0])

    # Added the assertion
    self.assertEqual(actual_result, expected_result)

  """ ------------ Add more unit tests ------------ """



if __name__ == '__main__':
    unittest.main()
