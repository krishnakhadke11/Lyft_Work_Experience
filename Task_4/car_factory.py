from car import Car
from datetime import datetime
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine

from battery.spindlerBattery import spindlerBattery
from battery.nubbinBattery import nubbinBattery

from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoprimeTires
class car_factory:
    def create_calliope(self,last_service_date,current_mileage,last_service_mileage):
        engine = CapuletEngine(last_service_date,current_mileage,last_service_mileage)
        battery=spindlerBattery(last_service_date,datetime.today().date())
        car = Car(engine,battery)
        return car
    
    def create_glissade(self,last_service_date,current_mileage,last_service_mileage):
        engine=WilloughbyEngine(last_service_date, current_mileage, last_service_mileage)
        battery=spindlerBattery(last_service_date,datetime.today().date())
        car = Car(engine,battery)
        return car
    
    def create_palindrome(self,last_service_date, warning_light_is_on):
        engine=SternmanEngine(last_service_date, warning_light_is_on)
        battery=spindlerBattery(last_service_date,datetime.today().date())
        car = Car(engine,battery)
        return car
    
    def create_rorschach(self,last_service_date, current_mileage, last_service_mileage):
        engine=WilloughbyEngine(last_service_date, current_mileage, last_service_mileage)
        battery=nubbinBattery(last_service_date,datetime.today().date())
        car = Car(engine,battery)
        return car
    
    def create_thovex(self,last_service_date,current_mileage,last_service_mileage):
        engine = CapuletEngine(last_service_date,current_mileage,last_service_mileage)
        battery=nubbinBattery(last_service_date,datetime.today().date())
        car = Car(engine,battery)
        return car