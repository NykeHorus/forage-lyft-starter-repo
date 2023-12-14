import unittest
from datetime import datetime

from engine.sternman_engine import SternmanEngine


class TestSternmanEngine(unittest.TestCase):
    def test_initialize_with_parameters(self):
        warning_light_is_on = True
        engine = SternmanEngine(warning_light_is_on)
        self.assertEqual(engine.warning_light_is_on, warning_light_is_on)
        
    def test_engine_should_be_serviced_false(self):
        warning_light_is_on = False
        engine = SternmanEngine(warning_light_is_on)
        self.assertFalse(engine.engine_should_be_serviced())
    
    def test_engine_should_be_serviced_true(self):
        warning_light_is_on = True
        engine = SternmanEngine(warning_light_is_on)
        self.assertTrue(engine.engine_should_be_serviced())