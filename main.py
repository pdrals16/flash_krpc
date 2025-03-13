import asyncio
import aiofiles
import time
import json
import logging
import numpy as np

from threading import Thread
from src.telemetry import Telemetry
from src.system import SimplePIDController
from src.control import RocketControl
from src.tower import tower

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

with open("src/config/PID_SYSTEM.json", "r") as f:
    configuration = json.loads(f.read())

pid = SimplePIDController(
        kp=configuration["kp"],
        ki=configuration.get("ki", 0), 
        kd=configuration.get("kd", 0)
    )

async def read_file(filename):
    async with aiofiles.open(filename, mode='r') as f:
        contents = await f.read()
        return contents
    
def run_web_server():
    tower.run(host='0.0.0.0', port=5000)


async def main():
    NAME = "SYSTEM"
    telemetry = Telemetry(name=f"{NAME}_1")
    control = RocketControl(name=f"{NAME}_2")

    while True:
        start = int(time.time() * 1000)
        file = await read_file("src/config/PARAMS.json")
        params = json.loads(file)
        await asyncio.sleep(0.1)
        telemetry.update()
        logger.debug(telemetry.metrics)
        alt = telemetry.metrics.ALTITUDE
        max_thrust = telemetry.metrics.MAX_THRUST
        
        end =  int(time.time() * 1000)
        dt = (end - start) / 1000
        
        control_output = pid.update(params["altitude"], alt, dt)
        logger.debug(f"{control_output, dt}")
        control.set_throttle(np.sum(control_output) / max_thrust)


if __name__=="__main__":
    logger.info("Starting...")
    
    web_thread = Thread(target=run_web_server, daemon=True)
    web_thread.start()

    asyncio.run(main())
