from tyre.tyre import Tyre

class CarriganTyre(Tyre):
    def __init__(self,tire_wear_array):
        self.tire_wear_array = tire_wear_array
        
    def needs_service(self):
        if any(wear >= 0.9 for wear in self.tire_wear_array):
            return True
        else:
            return False