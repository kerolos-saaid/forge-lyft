import datetime
from cars.models.Calliope import Calliope
from cars.models.Glissade import Glissade
from cars.models.Thovex import Thovex
from cars.models.Rorschach import Rorschach
from cars.models.Palindrome import Palindrome


class CarFactory:
    current_date = datetime.date.today()

    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        return Calliope(last_service_date, current_mileage, last_service_mileage, current_date)

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        return Glissade(last_service_date, current_mileage, last_service_mileage, current_date)

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        return Rorschach(last_service_date, current_mileage, last_service_mileage, current_date)

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        return Thovex(last_service_date, current_mileage, last_service_mileage, current_date)

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_indicator):
        return Palindrome(last_service_date, warning_indicator, current_date)
