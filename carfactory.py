from car import Car
from battery.nubbenBattery import NubbenBattery
from battery.spindlerBattery import SpindlerBattery
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from tyre.carrigan_tyre import CarriganTyre
from tyre.octoprime_tyre import OctoprimeTyre


class carfactory:
    def create_calliope(current_date,last_service_date,current_mileage,last_service_mileage,tire_wear_array):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tyre = OctoprimeTyre(tire_wear_array)
        car= Car(engine,battery,tyre)
        return car
    
    def create_glissade(current_date,last_service_date,current_mileage,last_service_mileage,tire_wear_array):
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tyre = CarriganTyre(tire_wear_array)
        car= Car(engine,battery,tyre)
        return car
    
    def create_rorschach(current_date,last_service_date,current_mileage,last_service_mileage,tire_wear_array):
        engine = WilloughbyEngine(last_service_date, current_mileage)
        battery = NubbenBattery(last_service_date, current_date)
        tyre = OctoprimeTyre(tire_wear_array)
        car= Car(engine,battery,tyre)
        return car
    
    def create_thovex(current_date,last_service_date,current_mileage,last_service_mileage,tire_wear_array):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = NubbenBattery(last_service_date,current_date)
        tyre = OctoprimeTyre(tire_wear_array)
        car= Car(engine,battery,tyre)
        return car
    
    def create_glissade(current_date,last_service_date,warning_light_is_on,tire_wear_array):
        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(last_service_date, current_date)
        tyre = CarriganTyre(tire_wear_array)
        car= Car(engine,battery,tyre)
        return car
    