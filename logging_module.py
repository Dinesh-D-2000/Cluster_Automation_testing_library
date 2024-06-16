import logging
import os
import random
def enable_logger():
    logs="logs_"
    for i in range(10):
        logs=logs+str(random.randint(0,9))
    os.makedirs(f"D:\\Automation_testing\\Logs\\{logs}")
    logger=logging.getLogger()
    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler(filename=f"D:\\Automation_testing\\Logs\\{logs}\\debug.log", mode="w")
    console_handler = logging.StreamHandler()
    formatter = logging.Formatter(fmt="%(asctime)s: %(levelname)s: %(message)s", datefmt="%y-%m-%d %I:%M:%S %p")
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    if not logger.handlers:
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logs, logger
