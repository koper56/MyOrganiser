# TODO: print weather for all day, hour by hour

import pyowm

# API key and type of subscription from http://openweathermap.org/
api_data = pyowm.OWM(API_key='3680a47900fb30de7d81ef3cb1a7d9fb',
                     subscription_type='free')

# Check API
is_api_online = api_data.is_API_online()


def print_weather():
    if is_api_online == True:
        print('API is online...')

        # Choose city
        city_input = input("Type your City and country symbol"
                           "\nf.ex. Warsaw, pl"
                           "\n-->:")

        # Set city for weather search in ('City, country symbol')
        observation = api_data.weather_at_place(city_input)
        weather = observation.get_weather()

        # Weather details
        clouds = weather.get_clouds()
        rain = weather.get_rain()
        wind = weather.get_wind()
        humidity = weather.get_humidity()
        temperature = weather.get_temperature('celsius')
        status = weather.get_detailed_status()

        # Print weather data from details
        print(f'Weather now in {city_input} \n'
              '\n'
              f'Clouds\t\t\t:\t{clouds} %\n'
              f'Rain\t\t\t:\t{rain} %\n'
              'Wind speed\t\t:\t', wind['speed'], ' \n'
              # 'Wind degree\t\t:\t', wind['deg'], ' \n'
              f'Humidity\t\t:\t{humidity} %\n'
              'Temperature\t\t:\t', temperature['temp'],
              ' celsius\n'
              'Max temperature\t:\t', temperature['temp_max'], ' celsius\n'
              'Min temperature\t:\t', temperature['temp_min'], ' celsius\n'
              f'Weather status\t:\t{status}')

    else:
        print('API is offline...')
# print_weather()

def print_weather_warsaw():
    if is_api_online == True:

        city_input = 'Warsaw, pl'

        # Set city for weather search
        observation = api_data.weather_at_place(city_input)
        weather = observation.get_weather()

        # Weather details
        clouds = weather.get_clouds()
        rain = weather.get_rain()
        wind = weather.get_wind()
        humidity = weather.get_humidity()
        temperature = weather.get_temperature('celsius')
        status = weather.get_detailed_status()

        # Print weather data from details
        print(f'Weather now in {city_input} \n'
              '\n'
              f'Clouds\t\t\t:\t{clouds} %\n'
              f'Rain\t\t\t:\t{rain} %\n'
              'Wind speed\t\t:\t', wind['speed'], ' \n'
              # 'Wind degree\t\t:\t', wind['deg'], ' \n'
              f'Humidity\t\t:\t{humidity} %\n'
              'Temperature\t\t:\t', temperature['temp'],
              ' celsius\n'
              'Max temperature\t:\t', temperature['temp_max'], ' celsius\n'
              'Min temperature\t:\t', temperature['temp_min'], ' celsius\n'
              f'Weather status\t:\t{status}')

    else:
        print('API is offline...')
print_weather_warsaw()
