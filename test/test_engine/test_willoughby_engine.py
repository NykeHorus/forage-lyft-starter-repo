import unittest
from datetime import datetime

from engine.willoughby_engine import WilloughbyEngine


class TestWilloughbyEngine(unittest.TestCase):
        # WilloughbyEngine can be instantiated with valid input parameters
    def test_instantiation_with_valid_input_parameters(self):
        current_mileage = 50000
        last_service_mileage = 40000
        engine = WilloughbyEngine(current_mileage, last_service_mileage)

        self.assertEqual(engine.current_mileage, current_mileage)
        self.assertEqual(engine.last_service_mileage, last_service_mileage)
        
        
    def test_engine_should_be_serviced_true(self):
        current_mileage = 100000
        last_service_mileage = 30000
        engine = WilloughbyEngine(current_mileage, last_service_mileage)

        self.assertTrue(engine.engine_should_be_serviced())
        
       
    def test_engine_should_be_serviced_returns_false(self):
        current_mileage = 50000
        last_service_mileage = 40000
        engine = WilloughbyEngine(current_mileage, last_service_mileage)

        self.assertFalse(engine.engine_should_be_serviced())