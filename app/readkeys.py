import os
from configparser import ConfigParser

def readKeys(filename='keys.ini', section='keys'):
    """ Read Twitter API keys """

    parser = ConfigParser()
    parser.read(filename)

    keys = {}
    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            keys[item[0]] = item[1]
    else:
        raise LookupError('{} not found in the {} file'.format(section, filename))

    return keys
