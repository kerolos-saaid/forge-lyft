from battery.Battery import Battery
from engine.Engine import Engine


class Car( Battery, Engine):
    def __init__(self, engine, battery):
        super().__init__()
        self.engine = engine
        self.battery = battery

    def needs_service(self):
        pass
