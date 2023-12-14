# Lightweight WeatherApp - Django Backend with RESTAPI

## Installation

> [!NOTE]
> Python version: 3.11

1. Clone the repository:
```
git clone https://github.com/myavuzokumus/LightweightWeatherApp-Backend.git
```

2. Get the dependencies
```
python -m pip install --upgrade pip
pip install -r requirements.txt
```

3. Run server!
```
python manage.py runserver
```

> [!IMPORTANT]
> You need to create `.env` file in root directory. And add that following things:
> - GOOGLEAPI_KEY = ""
> - WEATHERAPI_KEY = ""
> - SECRET_KEY=""

## Packages

- [virtualenv](https://virtualenv.pypa.io/en/latest/) - To run project safely in environment.
- [DateTime](https://docs.python.org/3/library/datetime.html) - Parse for datetimes.
- [Django](https://www.djangoproject.com/) - For backend framework
- [djangorestframework](https://www.django-rest-framework.org/) - To create own API.

## APIs

- [visualcrossing](https://www.visualcrossing.com/weather/weather-data-services) - Weather Data
- [Google Maps AutoComplete Places]- City Data

## License

This project is licensed under the [MIT License](/LICENSE).

## How to use API?

Data refreshing every 15 minute when user try to send pull request.

**GET**
- ..api/weather-info  > Will display you all weather info of cities in database
- ..api/weather-info?city=name > Will display the city you typed in the city section of the URL.

**POST**
- ..api/weather-info | City key > If city doesn't exists, then it will be create and return that data.
- ..api/places | City key > Returns the cities in the word you send via POST.
