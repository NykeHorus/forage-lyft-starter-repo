import unittest

from engine.capulet_engine import CapuletEngine



class TestCapulateEngine(unittest.TestCase):
    def test_initialization(self):
        current_mileage = 50000
        last_service_mileage = 20000
        engine = CapuletEngine(current_mileage, last_service_mileage)

        self.assertEqual(engine.current_mileage, current_mileage)
        self.assertEqual(engine.last_service_mileage, last_service_mileage)
        
    def test_needs_service_true(self):
        current_mileage = 50001
        last_service_mileage = 20000
        engine = CapuletEngine(current_mileage, last_service_mileage)

        self.assertTrue(engine.engine_should_be_serviced())
        
    def test_needs_service_false(self):
        current_mileage = 50000
        last_service_mileage = 40000
        engine = CapuletEngine(current_mileage, last_service_mileage)

        self.assertFalse(engine.engine_should_be_serviced())