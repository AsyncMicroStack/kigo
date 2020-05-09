import platform
import logging
import yaml
import os
import sys


def load(path_location = "setup", config_file = "config.yaml"):
    if platform.system() == "Linux" or os.name == "posix":
        config_path = os.path.join("/", path_location, config_file)
    else:
        disk = os.getcwd()[0:3]
        config_path = os.path.join(disk, path_location, config_file)

    if not os.path.exists(config_path):
        logging.info(f"Not found config: {config_path}")
        base_path = os.path.dirname(sys.argv[0])
        config_path = os.path.join(base_path, path_location, config_file)

    if os.path.exists(config_path):
        with open(config_path) as f:
            conf = yaml.load(f, Loader=yaml.FullLoader)
        logging.info(f"Load config: {config_path}")
        return conf

    if not os.path.exists(config_path):
        logging.info(f"Not found config: {config_path}")
        logging.error("Not found any configuration")
        raise Exception("Not found any configuration")