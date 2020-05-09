# -*- coding: utf_8 -*-
from .configuration import config
from .logging import logger

logger.setup()
config.load()



