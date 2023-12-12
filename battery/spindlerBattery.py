from datetime import datetime
from battery.battery import Battery

class SpindlerBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date= last_service_date
        self.current_date = current_date
        
    def needs_service(self):
        if self.last_service_date - self.current_date > 730:
            return True
        else: 
            return False