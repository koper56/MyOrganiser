import requests
import logging
import time

from morg import LOG_FILE_PATH

# Take time and store in format day_month_year - 09_05_2017
time_format = time.strftime("%Y_%m_%d")

# Create specific logger different than Kivy logger
logger = logging.getLogger(__name__)

# Set level of logger
logger.setLevel(logging.INFO)

# Logging info format f.ex.
# "[2017-05-09 15:33:58,217]	data_base_test_log.py	message"
format_of_logger = logging.Formatter(
    '[%(asctime)s]\t%(pathname)s\t%(message)s')

# Create file with logging info f.ex. "morg_09_05_2017.log"
file_handler = logging.FileHandler(LOG_FILE_PATH)
file_handler.setFormatter(format_of_logger)
logger.addHandler(file_handler)

# Wunderground API
# Return weather for now and amount times weather for +time_segment time for
# selected city (refine country!) in metric or english measurement system.
# Select format: .json or .xml
# List of types of weather in docs
# Create your api token: https://www.wunderground.com

# Your own data, f.ex:
# type_of_weather = 'hourly'
# country = 'Poland'
# city_name = 'Warsaw'
# measurement_system = 'metric'
# data_format = 'json
# time_segment = 3
# amount = 4

# Static data
WUNDERGROUND_API_URL = 'http://api.wunderground.com/api/'
WUNDERGROUND_API_TOKEN = 'a25c676ff3b56dc0'


def print_weather(type_of_weather, country, city_name, data_format,
                  measurement_system, time_segment, amount):
    # Give basic info after initiation of functions
    logger.info('Taken from API {} weather for {}/{}:'.format(
        type_of_weather, country, city_name))

    # Put your data to request url
    request_url = WUNDERGROUND_API_URL + WUNDERGROUND_API_TOKEN + '/' + \
                  type_of_weather + '/q/' + country + '/' + city_name + '.' \
                  + data_format
    requests_result = requests.get(request_url)

    # Take all data in readable version
    json_wunderground_data = requests_result.json()

    # Take specific part od json data with weather
    hourly_forecast_json_wunderground_data = json_wunderground_data[
        'hourly_forecast']

    with open('weatherdata.txt', mode='w',
              encoding='utf-8') as weather_file:
        hour = -time_segment

        while hour < time_segment * amount:
            hour += time_segment

            all_data_hourly_forecast_json_wunderground_data = \
                hourly_forecast_json_wunderground_data[hour]
            # Take detail about hour H:MM format
            hour_detail = \
                all_data_hourly_forecast_json_wunderground_data['FCTTIME'][
                    'civil']
            air_temp = all_data_hourly_forecast_json_wunderground_data['temp'][
                measurement_system]
            dewpoint_temp = \
                all_data_hourly_forecast_json_wunderground_data['dewpoint'][
                    measurement_system]
            feelslike_temp = all_data_hourly_forecast_json_wunderground_data[
                'feelslike'][measurement_system]
            sky_condition = all_data_hourly_forecast_json_wunderground_data[
                'condition']
            rain = all_data_hourly_forecast_json_wunderground_data['qpf'][
                measurement_system]
            snow = all_data_hourly_forecast_json_wunderground_data[
                'snow'][measurement_system]
            pressure = all_data_hourly_forecast_json_wunderground_data[
                'mslp'][measurement_system]

            weather_file.write(
                '---- {} ------------------------------------\n'
                '    Temp (C):    {}({})    feelslike {}\n'
                '    Sky: {}       Rain: {}\n'
                '    Snow: {}      Pressure: {}\n'.format(hour_detail,
                                                          air_temp,
                                                          dewpoint_temp,
                                                          feelslike_temp,
                                                          sky_condition,
                                                          rain, snow,
                                                          pressure))
