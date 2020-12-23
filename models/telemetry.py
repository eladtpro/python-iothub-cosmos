
from datetime import datetime


class Telemetry:
    deviceid = '',
    temperature = 0
    humidity = 0
    timestamp = 0

    def __init__(self, config, temperature, humidity):
            now = datetime.now()
            timestamp = datetime.timestamp(now)
            self.deviceid = config.deviceid
            self.timestamp = timestamp
            self.temperature = temperature
            self.humidity = humidity
