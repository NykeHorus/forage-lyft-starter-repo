import unittest
from datetime import datetime
from engine.capulet_engine import CapuletEngine



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