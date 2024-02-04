import datetime

from Car import Car
from battery.types.Nubbin import NubbinBattery
from battery.types.Spindler import SpindlerBattery
from engine.types.Capulet import CapuletEngine
from engine.types.Sternman import SternmanEngine
from engine.types.Willoughby import WilloughbyEngine


class CarFactory:
    current_date = datetime.date.today()

    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        return Car(engine, battery)

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        return Car(engine, battery)

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        return Car(engine, battery)

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        return Car(engine, battery)

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_indicator):
        engine = SternmanEngine(warning_indicator)
        battery = SpindlerBattery(last_service_date, current_date)
        return Car(engine, battery)
