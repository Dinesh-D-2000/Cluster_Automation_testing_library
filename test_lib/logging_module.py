import logging
import os
import random
def enable_logger():
    logs="logs_"
    curr_dir = os.path.dirname(os.path.abspath(__file__))
    for i in range(10):
        logs=logs+str(random.randint(0,9))
    os.makedirs(curr_dir + rf"\cluster_hmi_tests\hmi_tests\Logs\{logs}")
    logger=logging.getLogger()
    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler(filename=curr_dir + rf"\cluster_hmi_tests\hmi_tests\Logs\{logs}\\debug.log", mode="w")
    console_handler = logging.StreamHandler()
    formatter = logging.Formatter(fmt="%(asctime)s: %(levelname)s: %(message)s", datefmt="%y-%m-%d %I:%M:%S %p")
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    if not logger.handlers:
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logs, logger
