import datetime
from abc import ABC
from battery.Battery import Battery


class NubbinBattery(Battery, ABC):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        return self.last_service_date + datetime.timedelta(days=1460) <= self.current_date
