import datetime

from engine.types.Willoughby import WilloughbyEngine
from battery.types.Spindler import SpindlerBattery
from Car import Car


class Glissade(Car):
    def __init__(self, last_service_date, current_mileage, last_service_mileage, current_date=datetime.date.today()):
        self.engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.battery = SpindlerBattery(last_service_date, current_date)
        super().__init__(self.engine, self.battery)

    def needs_service(self):
        return self.battery.needs_service() or self.engine.needs_service()
