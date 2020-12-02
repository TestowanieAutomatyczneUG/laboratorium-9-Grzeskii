import unittest
from unittest.mock import *
from src.sample.CarClass import Car


class TestCar(unittest.TestCase):

    def test_needsFuel(self):
        car = Car()
        car.needsFuel = Mock(name = "needsFuel")
        car.needsFuel.return_value = True

        self.assertEqual(car.needsFuel(), True)


if __name__ == '__main__':
    unittest.main()
