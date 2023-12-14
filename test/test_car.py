import unittest
from datetime import datetime

from battery.nubbinBattery import NubbenBattery
from battery.spindlerBattery import SpindlerBattery
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine


class TestNubbinBattery(unittest.TestCase):
    def test_init_with_dates(self):
        last_service_date = "2020-01-01"
        current_date = "2022-01-01"
        battery = NubbenBattery(last_service_date, current_date)
    
        self.assertEqual(battery.last_service_date, last_service_date)
        self.assertEqual(battery.current_date, current_date)

    def test_needs_service_false(self):
        last_service_date = "2020-01-01"
        current_date = "2022-01-01"
        battery = NubbenBattery(last_service_date, current_date)
    
        self.assertFalse(battery.needs_service())

    def test_needs_service_true(self):
        last_service_date = "2016-01-01"
        current_date = "2022-01-01"
        battery = NubbenBattery(last_service_date, current_date)
    
        self.assertTrue(battery.needs_service())


class TestSpindlerBattery(unittest.TestCase):
    def test_init_with_dates(self):
        last_service_date = "2020-01-01"
        current_date = "2022-01-01"
        battery = SpindlerBattery(last_service_date, current_date)
    
        self.assertEqual(battery.last_service_date, last_service_date)
        self.assertEqual(battery.current_date, current_date)

    def test_needs_service_false(self):
        last_service_date = "2020-01-01"
        current_date = "2021-01-01"
        battery = SpindlerBattery(last_service_date, current_date)
    
        self.assertFalse(battery.needs_service())

    def test_needs_service_true(self):
        last_service_date = "2020-01-01"
        current_date = "2022-01-01"
        battery = SpindlerBattery(last_service_date, current_date)
    
        self.assertTrue(battery.needs_service())


class TestCapulateEngine(unittest.TestCase):
    def test_initialization(self):
        last_service_date = "2020-01-01"
        current_mileage = 50000
        last_service_mileage = 20000

        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage)

        self.assertEqual(engine.last_service_date, last_service_date)
        self.assertEqual(engine.current_mileage, current_mileage)
        self.assertEqual(engine.last_service_mileage, last_service_mileage)
        
    def test_needs_service_true(self):
        last_service_date = "2020-01-01"
        current_mileage = 50000
        last_service_mileage = 20000
        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage)

        self.assertTrue(engine.engine_should_be_serviced())
        
    def test_needs_service_false(self):
        last_service_date = "2020-01-01"
        current_mileage = 50000
        last_service_mileage = 40000
        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage)

        self.assertFalse(engine.engine_should_be_serviced())


class TestSternmanEngine(unittest.TestCase):
    def test_initialize_with_parameters(self):
        last_service_date = "2021-01-01"
        warning_light_is_on = True
        engine = SternmanEngine(last_service_date, warning_light_is_on)
        self.assertEqual(engine.last_service_date, last_service_date)
        self.assertEqual(engine.warning_light_is_on, warning_light_is_on)
        
    def test_engine_should_be_serviced_false(self):
        last_service_date = "2021-01-01"
        warning_light_is_on = False
        engine = SternmanEngine(last_service_date, warning_light_is_on)
        self.assertFalse(engine.engine_should_be_serviced())
    
    def test_engine_should_be_serviced_true(self):
        last_service_date = "2021-01-01"
        warning_light_is_on = True
        engine = SternmanEngine(last_service_date, warning_light_is_on)
        self.assertTrue(engine.engine_should_be_serviced())


class TestWilloughbyEngine(unittest.TestCase):
        # WilloughbyEngine can be instantiated with valid input parameters
    def test_instantiation_with_valid_input_parameters(self):
        last_service_date = datetime.datetime(2020, 1, 1)
        current_mileage = 50000
        last_service_mileage = 40000
        engine = WilloughbyEngine(last_service_date, current_mileage, last_service_mileage)

        self.assertEqual(engine.last_service_date, last_service_date)
        self.assertEqual(engine.current_mileage, current_mileage)
        self.assertEqual(engine.last_service_mileage, last_service_mileage)
        
        # engine_should_be_serviced returns True if current mileage minus last service mileage is greater than 60000
    def test_engine_should_be_serviced_true(self):
        last_service_date = datetime.datetime(2020, 1, 1)
        current_mileage = 100000
        last_service_mileage = 30000
        engine = WilloughbyEngine(last_service_date, current_mileage, last_service_mileage)

        self.assertTrue(engine.engine_should_be_serviced())
        
        # engine_should_be_serviced returns False if current mileage minus last service mileage is less than or equal to 60000
    def test_engine_should_be_serviced_returns_false(self):
        last_service_date = datetime.datetime(2020, 1, 1)
        current_mileage = 50000
        last_service_mileage = 40000

        engine = WilloughbyEngine(last_service_date, current_mileage, last_service_mileage)

        self.assertFalse(engine.engine_should_be_serviced())


if __name__ == '__main__':
    unittest.main()
