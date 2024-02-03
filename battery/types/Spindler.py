import datetime

from battery.Battery import Battery


class SpindlerBattery(Battery):
    def __init__(self, last_service_date, current_date=datetime.date.today()):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        return self.last_service_date + datetime.timedelta(days=730) <= self.current_date
