import unittest
from tyre.octoprime_tyre import OctoprimeTyre

class TestOctoprimeTyre(unittest.TestCase):
    
    def test_create_instance_with_tire_wear_array(self):
        tire_wear_array = [0.1, 0.2, 0.3, 0.4]
        tyre = OctoprimeTyre(tire_wear_array)
        self.assertEqual(tyre.tire_wear_array, tire_wear_array)
        
        
    def test_needs_service_false(self):
        tire_wear_array = [0.1, 0.1, 0.1, 0.1]
        tyre = OctoprimeTyre(tire_wear_array)
        self.assertFalse(tyre.needs_service())
        
        
    def test_needs_service_true(self):
        tire_wear_array = [1, 1, 1, 1]
        tyre = OctoprimeTyre(tire_wear_array)
        self.assertTrue(tyre.needs_service())