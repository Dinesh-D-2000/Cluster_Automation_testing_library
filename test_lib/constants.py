from enum import Enum

class TelltaleStatus(Enum):
    ON="ON"
    OFF="OFF"

class WarningStatus(Enum):
    ON="ON"
    OFF="OFF"

class Buttons(Enum):
    Home = "home"
    DRIVER_MODE = "drive_mode"
    REVERSE_MODE = "reverse_mode"
    TIRE_PRESSURE = "tpms"
    OIL_TEMP = "oil_temp"
    FUEL_ECONOMY = "fuel_economy"
    MESSAGES = "messages"
