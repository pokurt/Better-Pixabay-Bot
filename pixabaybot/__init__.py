import logging
from configparser import ConfigParser
from datetime import datetime

from pixabaybot.pixabaybot import pixabaybot

# Logging at the start to catch everything
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.WARNING,
    handlers=[
        logging.StreamHandler()
    ]
)
LOGS = logging.getLogger(__name__)

name = 'pixabaybot'

# Read from config file
config_file = f"{name}.ini"
config = ConfigParser()
config.read(config_file)

# Extra details
__version__ = '0.2.0'
__author__ = 'pokurt'

# Global Variables
CMD_HELP = {}
client = None
START_TIME = datetime.now()

pixabaybot = pixabaybot(name)
