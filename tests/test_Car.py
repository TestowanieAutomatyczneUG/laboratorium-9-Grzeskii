import unittest
from unittest.mock import *
from src.sample.CarClass import Car


class TestCar(unittest.TestCase):

    def test_needs_fuel(self):
        car = Car()
        car.needsFuel = Mock(name = "needsFuel")
        car.needsFuel.return_value = True

        self.assertEqual(car.needsFuel(), True)
    
    def test_get_engine_temperature(self):
        car = Car()
        car.getEngineTemperature = Mock(name = "getEngineTemperature")
        car.getEngineTemperature.return_value = 115

        self.assertEqual(car.getEngineTemperature(), 115)

    def test_drive_to(self):
        car = Car()
        destination = "Gdansk"
        car.driveTo = Mock(name = "driveTo")
        car.driveTo.return_value = f"Our destination is {destination}"

        self.assertEqual(car.driveTo("Gdansk"), "Our destination is Gdansk")


if __name__ == '__main__':
    unittest.main()
