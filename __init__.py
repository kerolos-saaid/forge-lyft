import datetime
from cars.CarFactory import CarFactory
from cars.models.Glissade import Glissade


x = Glissade(datetime.date.today()-datetime.timedelta(days=730), 100000, 40500)
y = CarFactory().create_glissade(datetime.date.today(), datetime.date.today(), 100000, 40500)

print(x.needs_service())
