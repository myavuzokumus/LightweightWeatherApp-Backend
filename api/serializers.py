from rest_framework import serializers

from .models import WeatherInfo, DailyWeather, HourlyWeather

class DailyWeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyWeather
        fields = [
            "date",
            "dayWeather",
            "nightWeather",
            "dayTemperature",
            "nightTemperature",
            "humidity",
        ]

class HourlyWeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = HourlyWeather
        fields = [
            "hour",
            "weatherType",
            "temperature",
        ]

class WeatherInfoSerializer(serializers.ModelSerializer):

    daily = DailyWeatherSerializer(many=True, read_only=True)
    hourly = HourlyWeatherSerializer(many=True, read_only=True)

    class Meta:
        model = WeatherInfo
        fields = [
            "city",
            "currentWeather",
            "instantTemperature",
            "dayTemperature",
            "nightTemperature",
            "feelsLike",
            "humidity",
            "daily",
            "hourly"
        ]