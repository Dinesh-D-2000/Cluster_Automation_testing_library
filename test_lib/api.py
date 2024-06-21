import cv2
from PIL import Image
from test_lib.logging_module import enable_logger
from test_lib.sql_operations import get_connection
import os
from test_lib.sql_operations import execute_sql_file
import logging
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time
import pytesseract
import json


class Error(Exception):
    def __init__(self, message):
        super().__init__(message)

curr_dir =  os.path.dirname(os.path.abspath(__file__))
curr_dir_1 = curr_dir.split("test_lib")[0]
curr_dir_2 = curr_dir.split("venv")[0]
class ValidationApi:
    def initialise_webdriver(self):
        browser_path = r"C:\Program Files\Mozilla Firefox\firefox.exe"
        driver_path = curr_dir_1 + r"drivers\geckodriver.exe"
        s = Service(executable_path=driver_path)
        o = Options()
        o.binary_location = browser_path
        driver = webdriver.Firefox(service=s, options=o)
        return driver

    def get_url(self):
        self.driver = self.initialise_webdriver()
        self.driver.get(url= curr_dir_1 + r"webpage\cluster_hmi.html")
        time.sleep(5)
        self.logger.info("URL SUCCESSFULLY LOADED")

    def press_btn(self, btn_id):
        if self.driver.title == "CLUSTER HMI DISPLAY":
            self.button = self.driver.find_element(by=By.ID, value=btn_id)
            self.button.click()
            self.logger.info(f"Button with ID:{btn_id} is pressed")

    def setup_logger(self):
        # Clear any previous handlers associated with the logger
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)
        # Enable logger
        self.logs, self.logger = enable_logger()

    def capture_screen(self):
        if self.driver.title == "CLUSTER HMI DISPLAY":
            path = curr_dir_2 + fr"\cluster_hmi_tests\hmi_tests\Logs\{self.logs}\screenshot.png"
            self.driver.save_screenshot(path)
            self.logger.info(f"Screenshot successfully captured and saved in path:{path}")
            return path

    def icon_db_load(self):

        try:
            execute_sql_file(curr_dir_1 + r"test_resources\icons.sql")
            self.logger.info("ICON DB sucessfully loaded")
        except:
            self.logger.error("ICON DB IS NOT SUCCESSFULLY LOADED")
            raise Error("ICON DB IS NOT SUCCESSFULLY LOADED")

    def read_database_icon_and_save(self, name):
        conn, cursor = get_connection()
        cursor.execute('''
            SELECT image FROM icons WHERE name = ?
        ''', (name,))
        blob_data = cursor.fetchone()[0]
        conn.commit()
        conn.close()
        with open(curr_dir_2 + rf"\cluster_hmi_tests\hmi_tests\Logs\{self.logs}\database_icon_" + name + ".png", 'wb') as file:
            file.write(blob_data)

    def verify_telltale_status(self, telltale_mode, icon_data, frame_data):
        """
        This method would verify the telltale is ON/OFF
        """

        icon = icon_data["telltale_icon"]
        self.read_database_icon_and_save(icon)
        self.logger.info(f"{icon} is sucessfully read from the database")
        icon = cv2.imread(curr_dir_2 + rf"\cluster_hmi_tests\hmi_tests\Logs\{self.logs}\database_icon_{icon}.png")

        full_screenshot = Image.open(frame_data)

        top_left = icon_data["top_left_coordinate"]
        bottom_right = icon_data["bottom_right_coordinate"]

        compare_icon = Image.open(frame_data)
        compare_icon = compare_icon.crop((top_left[0], top_left[1], bottom_right[0], bottom_right[1]))
        compare_icon.save(curr_dir_2 + rf"\cluster_hmi_tests\hmi_tests\Logs\{self.logs}\compare_icon.png")

        compare_icon = cv2.imread(curr_dir_2 + rf"\cluster_hmi_tests\hmi_tests\Logs\{self.logs}\compare_icon.png")
        icon = cv2.cvtColor(icon, cv2.COLOR_BGR2GRAY)

        compare_icon = cv2.cvtColor(compare_icon, cv2.COLOR_BGR2GRAY)
        result = cv2.matchTemplate(compare_icon, icon, cv2.TM_CCOEFF_NORMED)

        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        confidence = 0.7
        top_left = max_loc
        h, w = icon.shape
        bottom_right = (top_left[0] + w, top_left[1] + h)
        detected_roi = full_screenshot.crop((top_left[0], top_left[1], bottom_right[0], bottom_right[1]))
        detected_roi.save(curr_dir_2 + rf"\cluster_hmi_tests\hmi_tests\Logs\{self.logs}\detected_icon.png")
        self.logger.info(f"Detection result for {icon_data['telltale_icon']}")

        if max_val >= confidence and telltale_mode == "ON":
            self.logger.info("TELLTALE STATUS IS ON")
            self.logger.info(f"top left coordinates: {top_left}")
            self.logger.info(f"bottom right coordinates: {bottom_right}")
            self.logger.info(f"ICON saved as detected_icon_{icon_data['telltale_icon']}.png")
            self.logger.info(f"confidence_detected: {max_val}")
        elif max_val < confidence and telltale_mode == "ON":
            self.logger.error("TELLTALE STATUS IS NOT ON")
            self.logger.info(f"confidence_detected: {max_val}")
            raise Error("TELLTALE STATUS IS NOT ON")
        elif telltale_mode == "OFF" and max_val < confidence:
            self.logger.info("TELLTALE STATUS IS OFF")
            self.logger.info(f"confidence_detected: {max_val}")

        elif telltale_mode == "OFF" and max_val >= confidence:
            self.logger.error("TELLTALE STATUS IS NOT OFF")
            self.logger.info(f"confidence_detected: {max_val}")
            raise Error("TELLTALE STATUS IS NOT OFF")

    def verify_warning_status(self, warning_status, warning_id, frame_data):
        """
        This method will verify if the warning test is present in the HMI
        """
        with open(curr_dir_1 + r"test_resources\warning_data.json", 'r') as file:
            data = json.load(file)
            for i in range(len(data)):
                if data[i]["warning_id"] == warning_id:
                    top_left = data[i]["top_left_coordinate"]
                    bottom_right = data[i]["bottom_right_coordinate"]
                    warning_text = data[i]["warning_text"]
        pytesseract.pytesseract.tesseract_cmd = curr_dir_1 + r"drivers\tesseract\tesseract.exe"
        full_screenshot = Image.open(frame_data)
        roi = full_screenshot.crop((top_left[0], top_left[1], bottom_right[0], bottom_right[1]))
        roi.save(curr_dir_2 + rf"\cluster_hmi_tests\hmi_tests\Logs\{self.logs}\given_region.png")
        roi = Image.open(curr_dir_2 + rf"\cluster_hmi_tests\hmi_tests\Logs\{self.logs}\given_region.png")
        extracted_text = pytesseract.image_to_string(roi)
        if warning_text in extracted_text:
            self.logger.info(f"Warning {warning_id} with text {warning_text} is ON")
            self.logger.info(f"top_left_coordinates: {top_left}")
            self.logger.info(f"bottom_right_coordinates: {bottom_right}")
        else:
            self.logger.error(f"Warning {warning_id} is NOT ON")
            self.logger.info(f"Detected Text is \n{extracted_text}")
            raise Error(f"Warning {warning_id} is NOT ON")