
from datetime import datetime
from string import Template

template = Template('''{
    "id": "$timestamp",
    "batchid": "$batchid",
    "device": {
        "deviceid": "$deviceid"
    },
    "data": {
        "timestamp": $timestamp,
        "temperature": $temperature,
        "humidity": $humidity
    }
}''')


def flatten(multiline):
    lst = multiline.split('\n')
    flat = ''
    for line in lst:
        flat += line.replace(' ', '')+' '
    return flat


def format(data):
    message = template.substitute(deviceid=data.deviceid, batchid=data.batchid, timestamp=data.timestamp,
                                  temperature=data.temperature, humidity=data.humidity)
    flattend = flatten(message)
    return flattend


class Telemetry:
    deviceid = ''
    batchid = 0
    temperature = 0
    humidity = 0
    timestamp = 0

    def __init__(self, config, batchid, temperature, humidity):
        now = datetime.now()
        timestamp = datetime.timestamp(now)
        self.deviceid = config.iot.deviceid
        self.timestamp = timestamp
        self.temperature = temperature
        self.humidity = humidity
