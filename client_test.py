import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    # Initialize values
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
     # use a tuple returning the expected values to assert the test instead of making more than one assertion statement
    for quote in quotes: 
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'],(quote['top_bid']['price'] + quote['top_ask']['price']) / 2))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    # use a tuple returning the expected values to assert the test instead of making more than one assertion statement
    for quote in quotes: 

      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask'] ['price'],(quote['top_bid']['price'] + quote['top_ask']['price']) / 2))


  """ ------------ Add more unit tests ------------ """
  # Check if ratio is zero when price b is 0
  def getRatio_test_priceBisZero(self):
    price_a = 119.2
    price_b = 0
    self.assertIsNone(getRatio(price_a,price_b))
  # Check if ratio is zero when price a is 0
  def getRatio_test_priceAisZero(self):
    price_a = 0
    price_b = 121.68
    self.assertEqual(getRatio(price_a, price_b), 0)
  
  # Check if the result of ratio it is greater than 1
  def getRatio_test_greaterThan1(self):
    price_a = 447.26
    price_b = 224.46
    self.assertGreater(getRatio(price_a, price_b), 1)
  
  # Check that the result of ratio is less than 1
  def getRatio_test_lessThan1(self):
    price_a = 224.46
    price_b = 447.26
    self.assertLess(getRatio(price_a, price_b), 1)

  # Check that the result of ratio is equal to 1
  def getRatio_test_Equalto1(self):
    price_a = 721.46
    price_b = 721.46
    self.assertEqual(getRatio(price_a, price_b), 1)


if __name__ == '__main__':
    unittest.main()
