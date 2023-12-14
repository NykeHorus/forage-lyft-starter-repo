import unittest
from datetime import date

from battery.spindlerBattery import SpindlerBattery

class TestSpindlerBattery(unittest.TestCase):
    def test_init_with_dates(self):
        last_service_date = date.fromisoformat("2020-01-01")
        current_date = date.fromisoformat("2022-01-01")
        battery = SpindlerBattery(last_service_date, current_date)
    
        self.assertEqual(battery.last_service_date, last_service_date)
        self.assertEqual(battery.current_date, current_date)

    def test_needs_service_false(self):
        last_service_date = date.fromisoformat("2020-01-01")
        current_date = date.fromisoformat("2021-01-01")
        battery = SpindlerBattery(last_service_date, current_date)
    
        self.assertFalse(battery.needs_service())

    def test_needs_service_true(self):
        last_service_date = date.fromisoformat("2020-01-01")
        current_date = date.fromisoformat("2023-05-01")
        battery = SpindlerBattery(last_service_date, current_date)
    
        self.assertTrue(battery.needs_service())
