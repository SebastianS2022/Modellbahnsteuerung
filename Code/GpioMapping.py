import xml.etree.ElementTree as ET
class GPIOMapper:
    gpioOutputDictionary = {
        #train switch name and left/right, GPIO number
        "ts1r": 14,
        "ts1l": 15
    }

    def __init__(self, config):
        xmlConfig = ET.parse(config)
        xmlRoot = xmlConfig.getroot()

