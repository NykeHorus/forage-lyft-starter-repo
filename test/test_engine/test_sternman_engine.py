import unittest
from datetime import datetime

from engine.sternman_engine import SternmanEngine


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