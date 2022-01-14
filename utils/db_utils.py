from models import Accelerometer, Gyro, Temp
from sensors.sensors_config import SensorsConfig


def get_acceleration_data():
    accelerometer_data = Accelerometer.query.all()

    data = {
        SensorsConfig.TIMESTAMP_NAME_KEY: [],
        SensorsConfig.ACCELEROMETER_X_VALUE_NAME : [],
        SensorsConfig.ACCELEROMETER_Y_VALUE_NAME: [],
        SensorsConfig.ACCELEROMETER_Z_VALUE_NAME: []
    }

    for data_row in accelerometer_data:
        data[SensorsConfig.TIMESTAMP_NAME_KEY].append(data_row.timestamp)
        data[SensorsConfig.ACCELEROMETER_X_VALUE_NAME].append(data_row.x_value)
        data[SensorsConfig.ACCELEROMETER_Y_VALUE_NAME].append(data_row.y_value)
        data[SensorsConfig.ACCELEROMETER_Z_VALUE_NAME].append(data_row.z_value)

    return data


def get_gyro_data():
    gyro_data = Gyro.query.all()

    data = {
        SensorsConfig.TIMESTAMP_NAME_KEY: [],
        SensorsConfig.ACCELEROMETER_X_VALUE_NAME : [],
        SensorsConfig.ACCELEROMETER_Y_VALUE_NAME: [],
        SensorsConfig.ACCELEROMETER_Z_VALUE_NAME: []
    }

    for data_row in gyro_data:
        data[SensorsConfig.TIMESTAMP_NAME_KEY].append(data_row.timestamp)
        data[SensorsConfig.GYRO_X_VALUE_NAME].append(data_row.x_value)
        data[SensorsConfig.GYRO_Y_VALUE_NAME].append(data_row.y_value)
        data[SensorsConfig.GYRO_Z_VALUE_NAME].append(data_row.z_value)

    return data


def get_temp_data():
    temp_data = Temp.query.all()

    data = {
        SensorsConfig.TIMESTAMP_NAME_KEY: [],
        SensorsConfig.TEMP_TEMPERATURE_VALUE_NAME : [],
        SensorsConfig.TEMP_HUMIDITY_VALUE_NAME: []
    }

    for data_row in temp_data:
        data[SensorsConfig.TIMESTAMP_NAME_KEY].append(data_row.timestamp)
        data[SensorsConfig.TEMP_TEMPERATURE_VALUE_NAME].append(data_row.temp_value)
        data[SensorsConfig.TEMP_HUMIDITY_VALUE_NAME].append(data_row.humi_value)

    return data


def filter_acceleration_data(begin_datetime, end_datetime, accelerometer_data):
    timestamps = []
    x_values = []
    y_values = []
    z_values = []

    for i, timestamp in enumerate(accelerometer_data[SensorsConfig.TIMESTAMP_NAME_KEY]):
        if begin_datetime <= timestamp <= end_datetime:

            timestamps.append(timestamp)
            x_values.append(accelerometer_data[SensorsConfig.ACCELEROMETER_X_VALUE_NAME][i])
            y_values.append(accelerometer_data[SensorsConfig.ACCELEROMETER_Y_VALUE_NAME][i])
            z_values.append(accelerometer_data[SensorsConfig.ACCELEROMETER_Z_VALUE_NAME][i])

    return timestamps, x_values, y_values, z_values


def filter_gyro_data(begin_datetime, end_datetime, gyro_data):
    timestamps = []
    x_values = []
    y_values = []
    z_values = []

    for i, timestamp in enumerate(gyro_data[SensorsConfig.TIMESTAMP_NAME_KEY]):
        if begin_datetime <= timestamp <= end_datetime:

            timestamps.append(timestamp)
            x_values.append(gyro_data[SensorsConfig.GYRO_X_VALUE_NAME][i])
            y_values.append(gyro_data[SensorsConfig.GYRO_Y_VALUE_NAME][i])
            z_values.append(gyro_data[SensorsConfig.GYRO_Z_VALUE_NAME][i])

    return timestamps, x_values, y_values, z_values


def filter_temp_data(begin_datetime, end_datetime, temp_data):
    timestamps = []
    temp_values = []
    humi_values = []

    for i, timestamp in enumerate(temp_data[SensorsConfig.TIMESTAMP_NAME_KEY]):
        if begin_datetime <= timestamp <= end_datetime:

            timestamps.append(timestamp)
            temp_values.append(temp_data[SensorsConfig.TEMP_TEMPERATURE_VALUE_NAME][i])
            humi_values.append(temp_data[SensorsConfig.TEMP_HUMIDITY_VALUE_NAME][i])

    return timestamps, temp_values, humi_values