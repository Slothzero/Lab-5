# Лабораторная работа №5, вариант 5
# Первая часть задания

import requests
import datetime

# API ключ и адрес с которого будут браться данные
api_key = 'f1d8f9c0ba5dd9df65b93203f34a0e33'
base_url = 'http://api.openweathermap.org/data/2.5/weather?'

# Функция переводит градусы по Кельвину в градусы Цельсия, т.к сайт отдает температуру в кельвинах
def kelv_to_cels(kelvin):
    celsius = kelvin - 273.15
    round(celsius)
    return celsius

# Перевод давления из паскалей в мм ртутного столба
def hPa_to_mm(press_hpa):
    press_mm = press_hpa * 100 / 133.3
    round(press_mm)
    return press_mm

while True:

    # Здесь создается запрос
    city_name = input('City name? ')
    url = f'{base_url}appid={api_key}&q={city_name}'

    # Это ответ с сайта
    response = requests.get(url).json()

    # Ошибка при неправильном вводе
    if response['cod'] == '404':
        print('City not found, try again')

    else:
        # Здесь достаем из response нужную информацию
        general_weather = f"{response['weather'][0]['main']}"
        temp = round(kelv_to_cels(response['main']['temp']))
        pressure = round(hPa_to_mm(response['main']['pressure']))
        humidity = response['main']['humidity']
        time = str(datetime.datetime.fromtimestamp(response['dt']))
        current_time = f'{time[11:16]}, {time[8:10]}/{time[5:7]}/{time[0:4]}'

        # Ну и вывод
        print(f"""Weather in {city_name} on {current_time}:
        General weather: {general_weather}
        Temperature: {temp}°C
        Pressure: {pressure} mmHg
        Humidity: {humidity}%
        """)
        break