# UNI436 - Stage 2 SIC Assignment

This repository contains a solution for the Stage 2 SIC (Samsung Innovation Campus) assignment. The project integrates an ESP32 microcontroller with various sensors and provides a REST API for data collection.

## Project Overview

### Hardware Components

- **ESP32 DevKit Board**
- **Sensors:**
  - DHT11 (Temperature & Humidity)
  - HC-SR501 (Motion Sensor)

### Software Components

1. **ESP32 MicroPython Application**
   - Collects sensor data
   - Connects to WiFi
   - Transmits data
2. **Flask REST API**
   - Integrates with MongoDB
   - Provides RESTful endpoints
   - Runs in a Docker container

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.13 or higher
- Docker & Docker Compose
- MicroPython tools (from `requirements-dev.txt`)

### Installation & Setup

#### 1. Clone the repository

```sh
git clone https://www.github.com/fwwz-id/uni436-s2as2
cd uni436-s2as2
```

#### 2. Start the API services

```sh
docker compose up -d
```

#### 3. Flash ESP32 (Development)

```sh
pip install -r requirements-dev.txt
```

For more details, refer to the official [MicroPython documentation](https://micropython.org/download/ESP32_GENERIC/).

## API Endpoints

- `GET /ping` - Health check
- `GET /dht22` - Retrieve DHT22 sensor data

## Development & Simulation

The project can be simulated using Wokwi for ESP32 development. See [diagram.json](diagram.json) for the hardware configuration.

### Wokwi Setup

#### 1. Install Wokwi Extension

- Download the [Wokwi VS Code extension](https://marketplace.visualstudio.com/items?itemName=Wokwi.wokwi-vscode).

#### 2. Start the Simulator

- Press `Ctrl + Shift + P` to open the command palette.
- Search for `Wokwi: Start Simulation` and select `wokwi.toml` when prompted.

#### 3. Connect to ESP32

Use the following command to connect to the ESP32 board:

```sh
mpremote connect port:rfc2217://localhost:4000 run esp32/main.py
```

For advanced usage, refer to the [official Wokwi documentation](https://github.com/wokwi/wokwi-vscode-micropython/blob/main/README.md).

#### Troubleshooting

If you encounter the error `mpremote.transport.TransportError: could not enter raw repl`, try running the command again. If the issue persists, restart the simulator.

To check if port 4000 is active:

```sh
# Linux/macOS
netstat -an | grep 4000  

# Windows
netstat -ano | findstr 4000  
```

Expected output:

```sh
tcp    0    0 127.0.0.1:4000   0.0.0.0:*   LISTEN
```

For further assistance, consult the Wokwi Discord community or official support.

## Production Deployment

To deploy to a physical ESP32 board, use:

```sh
mpremote connect port:rfc2217://<esp32-ip>:4000 run esp32/main.py
```

## License

This project is part of an event assignment.

## Developer

| Mantainer                 | Email                     |
| ------------------------- | ------------------------- |
| Fawwaz Abdurrahim         | fwwz.id@gmail.com         |
| Mohammad Luqman Hakim     | moh.luqman.nore@gmail.com |
| Muhammad Rafly Adryansyah | muhr0417@gmail.com        |
| Wildan Wigenta            | wildanwigenta52@gmail.com |
