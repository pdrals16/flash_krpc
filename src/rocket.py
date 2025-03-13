import krpc
import logging

class RocketCommunication():
    def __init__(self, name):
        self.name = f"{__name__}_{name}"
        self.conn = self.connect()
        self.vessel = self.conn.space_center.active_vessel
        self.reference = self.vessel.orbit.body.reference_frame
        pass

    def connect(self):
        logging.info(f"Connection to {self.name}...")
        return krpc.connect(name=self.name)