# Rocket Control System

A Python-based PID control system for automated rocket flight in Kerbal Space Program using the kRPC mod.

## Overview

This system provides automated altitude control for rockets in KSP through a PID controller that adjusts throttle to maintain a target altitude. The application collects telemetry data, processes it through the PID algorithm, and sends throttle commands back to the rocket.

## Prerequisites

- [Kerbal Space Program](https://store.steampowered.com/app/220200/Kerbal_Space_Program/)
- [kRPC Mod](https://spacedock.info/mod/69/kRPC) installed in KSP
- Python 3.8+

## Installation

1. Clone this repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

### Setup KSP and kRPC

1. Launch Kerbal Space Program
2. Start a campaign/mission with a rocket
3. When prompted by kRPC, start the server with default settings
4. Make sure your rocket is on the launchpad and is the active vessel

### Running the Control System

Start the main control application:

```
python main.py
```

The application will:
- Connect to KSP via kRPC
- Start a web server on port 5000 for control commands
- Begin monitoring telemetry and applying PID control

### Setting Target Altitude

You can change the target altitude by sending a POST request to the web server:

```
curl -X POST http://localhost:5000/set_altitude -H "Content-Type: application/json" -d '{"altitude": 500.0}'
```

Replace `500.0` with your desired altitude in meters.

## Configuration

The system uses two configuration files:

- `src/config/PARAMS.json` - Contains the target altitude
- `src/config/PID_SYSTEM.json` - Contains PID controller parameters

Adjust these files to fine-tune the control system's behavior.

## Project Structure

- `main.py` - Entry point for the application
- `src/system.py` - PID controller implementation
- `src/telemetry.py` - Collects flight data from the rocket
- `src/control.py` - Sends control commands to the rocket
- `src/tower.py` - Web server for command input
- `src/rocket.py` - Base communication with KSP/kRPC

## Troubleshooting

- If you encounter connection issues, ensure the kRPC server is running in KSP
- Check `debug.log` for detailed application logs
- Verify your rocket has engines and fuel before starting the control system
