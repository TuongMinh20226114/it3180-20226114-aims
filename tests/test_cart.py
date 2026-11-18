import unittest
from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class TestCart(unittest.TestCase):
    def test_add_dvd_until_full(self):
        cart = Cart()
        for i in range(20):
            dvd = DigitalVideoDisc(f"DVD {i + 1}", "Action", "Director", 90, 10.0)
            self.assertTrue(cart.add_dvd(dvd))
        # Đĩa thứ 21 phải bị từ chối (trả về False)
        extra_dvd = DigitalVideoDisc("DVD 21", "Action", "Director", 90, 10.0)
        self.assertFalse(cart.add_dvd(extra_dvd))


if __name__ == "__main__":
    unittest.main()
