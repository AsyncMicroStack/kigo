# -*- coding: utf_8 -*-
import logging
import os
import sys
import coloredlogs


def setup(path=None, logging_file='logging.log', logging_level=logging.INFO, append_console = True, colour = False):
    if isinstance(logging_level, str):
        logging_level = logging.getLevelName(logging_level)
    if not path:
        path = os.path.dirname(sys.argv[0])
    logging_file = os.path.join(path, logging_file)
    logging.root.handlers = []

    logging_handlers = {logging.FileHandler(logging_file)}
    if append_console:
        logging_handlers.add(logging.StreamHandler())
    if colour:
        coloredlogs.install()
    logging.basicConfig(handlers=logging_handlers,
                        level=logging_level,
                        format='%(asctime)s\t%(levelname)s\t%(message)s',
                        datefmt='%d %b %Y %H:%M:%S')

