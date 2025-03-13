from dataclasses import dataclass
from src.rocket import RocketCommunication

@dataclass
class Metrics:
    ALTITUDE: float = None
    VELOCITY: float = None
    PRESSURE: float = None
    TEMPERATURE: float = None
    MASS: float = None
    THRUST: float = None
    MAX_THRUST: float = None


class Telemetry(RocketCommunication):
    def __init__(self, name):
        super().__init__(name)
        self.metrics = Metrics()
        pass


    def update(self):
        self.metrics.ALTITUDE = self.vessel.flight().mean_altitude
        self.metrics.VELOCITY = self.vessel.velocity(self.reference)
        self.metrics.PRESSURE = self.vessel.flight().static_pressure_at_msl
        self.metrics.TEMPERATURE = self.vessel.flight().static_air_temperature
        self.metrics.MASS = self.vessel.mass
        self.metrics.THRUST = self.vessel.thrust
        self.metrics.MAX_THRUST = self.vessel.max_thrust