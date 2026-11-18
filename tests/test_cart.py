import unittest
from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class TestCart(unittest.TestCase):
    def test_add_dvd_until_full(self):
        cart = Cart()
        for i in range(20):
            dvd = DigitalVideoDisc(f"DVD {i + 1}", "Action", "Director", 90, 10.0)
            self.assertTrue(cart.add_dvd(dvd))
        extra_dvd = DigitalVideoDisc("DVD 21", "Action", "Director", 90, 10.0)
        self.assertFalse(cart.add_dvd(extra_dvd))

    def test_total_cost_with_discount(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("DVD 1", "Action", "Director", 90, 100.0))
        self.assertAlmostEqual(cart.total_cost_with_discount(20), 80.0)
        with self.assertRaises(ValueError):
            cart.total_cost_with_discount(150)


if __name__ == "__main__":
    unittest.main()
