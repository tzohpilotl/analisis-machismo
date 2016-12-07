from configparser import ConfigParser
from pydoc

class KeyReader():
""" Keyreader to load keys.ini file """

    def __init__(self):
        self.parser = ConfigParser()
        self.keys = {}
    
    def read(self, filename='keys.ini', section='keys'):
    """ Import the configparser, tell it to read the file, and get a listing of the sections. Sections are listed in square brackets [] """	
	self.keys.clear()
        self.parser.read(filename)

        if self.parser.has_section(section):
            items = self.parser.items(section)
            for item in items:
                self.keys[item[0]] = item[1]
        else:
            raise LookupError('{} not found in {} file'.format(section, filename))
        return self.keys
