import unittest
from tyre.carrigan_tyre import CarriganTyre

class TestCarrigenTyre(unittest.TestCase):
    
    def test_init_with_tyre_wear_array(self):
        tire_wear_array = [0.8, 0.7, 0.6]
        tyre = CarriganTyre(tire_wear_array)
        
        self.assertEqual(tyre.tire_wear_array, tire_wear_array)
        
    def test_needs_service_false(self):
        tire_wear_array = [0.8, 0.7, 0.6]
        tyre = CarriganTyre(tire_wear_array)
        
        self.assertFalse(tyre.needs_service())
        
        
    def test_needs_service_true(self):
        tire_wear_array = [0.8, 0.9, 0.7]
        tyre = CarriganTyre(tire_wear_array)
        
        self.assertTrue(tyre.needs_service())