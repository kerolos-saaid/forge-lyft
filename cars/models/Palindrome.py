import datetime

from engine.types.Sternman import SternmanEngine
from battery.types.Spindler import SpindlerBattery
from Car import Car


class Palindrome(Car):
    def __init__(self, last_service_date, warning_indicator, current_date=datetime.date.today()):
        self.engine = SternmanEngine(warning_indicator)
        self.battery = SpindlerBattery(last_service_date, current_date)
        super().__init__(self.engine, self.battery)

    def needs_service(self):
        return self.battery.needs_service() or self.engine.needs_service()
