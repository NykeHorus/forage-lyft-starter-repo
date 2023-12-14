import unittest
from datetime import datetime

from engine.willoughby_engine import WilloughbyEngine


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