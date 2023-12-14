from django.contrib import admin
from .models import WeatherInfo, DailyWeather, HourlyWeather

class WeatherInfoList(admin.ModelAdmin):
 list_display = ("city", "currentWeather", "instantTemperature", "dayTemperature", "nightTemperature", "feelsLike", "humidity")
 search_fields = ("city", "currentWeather")

class DailyWeatherInfoList(admin.ModelAdmin):
 list_display = ("city", "date", "dayWeather", "nightWeather", "dayTemperature", "nightTemperature", "humidity")
 search_fields = ("city", "date")

class HourlyWeatherInfoList(admin.ModelAdmin):
 list_display = (
 "city", "hour", "weatherType", "temperature")
 search_fields = ("city", "hour")

# Register models here.
admin.site.register(WeatherInfo, WeatherInfoList)
admin.site.register(DailyWeather, DailyWeatherInfoList)
admin.site.register(HourlyWeather, HourlyWeatherInfoList)
# Register your models here.
