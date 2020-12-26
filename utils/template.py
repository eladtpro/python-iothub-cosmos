from string import Template

template = Template('''{
    "id": "$timestamp",
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
    message = template.substitute(deviceid=data.deviceid, timestamp=data.timestamp, temperature=data.temperature, humidity=data.humidity)
    flattend = flatten(message)
    return flattend
