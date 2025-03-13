import logging

from src.rocket import RocketCommunication


class RocketControl(RocketCommunication):
    def __init__(self, name):
        super().__init__(name)
        pass

    def set_throttle(self, throttle_percent: float = 0):
        logging.debug(f"Throttle Percent: {throttle_percent}")
        self.vessel.control.throttle = throttle_percent