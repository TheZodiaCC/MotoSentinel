import threading
import time
from sensors.gyro import Gyro
from sensors.accelerometer import Accelerometer
from sensors.temp import Temp
from sensors.current_sensor import CurrentSensor
from background_managers.managers_config import ManagersConfig


class SensorManager:
    def __init__(self):
        self.is_running = False
        self.process = threading.Thread(target=self.mainloop)

        self.gyro_sensor = Gyro()
        self.accelerometer_sensor = Accelerometer()
        self.temp_sensor = Temp()
        self.current_sensor = CurrentSensor()

        self.sensors = [self.gyro_sensor, self.accelerometer_sensor, self.temp_sensor, self.current_sensor]

    def start(self):
        if not self.is_running:
            self.is_running = True
            self.process.start()

    def mainloop(self):
        while self.is_running:
            for sensor in self.sensors:
                if sensor.sensor is not None:
                    sensor.update()

            time.sleep(ManagersConfig.SENSORS_MANAGER_UPDATE_RATE)

    def get_sensors(self):
        return self.sensors

    def get_sensor_data_by_sensor_name(self, sensor_name):
        sensor_data = []

        for sensor in self.sensors:
            if sensor.name == sensor_name:
                sensor_data = sensor.get_sensor_values()
                break

        return sensor_data

    def get_sensor_parsed_data_by_sensor_name(self, sensor_name):
        parsed_sensor_data = {}

        for sensor in self.sensors:
            if sensor.name == sensor_name:
                parsed_sensor_data = sensor.parse_sensors_data()
                break

        return parsed_sensor_data
