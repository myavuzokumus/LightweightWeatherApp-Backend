from django.db import models
class WeatherInfo(models.Model):
    city = models.CharField(max_length=255)
    currentWeather = models.CharField(max_length=30)

    instantTemperature = models.IntegerField(default=10)
    dayTemperature = models.IntegerField(default=10)
    nightTemperature = models.IntegerField(default=10)
    feelsLike = models.IntegerField(default=10)
    humidity = models.IntegerField(default=10)

    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (f""
                f"City: {self.city}")

class DailyWeather(models.Model):
    city = models.ForeignKey(WeatherInfo, on_delete=models.CASCADE, related_name="daily")
    date = models.DateField()
    dayWeather = models.CharField(max_length=30)
    nightWeather = models.CharField(max_length=30)

    dayTemperature = models.IntegerField(default=10)
    nightTemperature = models.IntegerField(default=10)
    humidity = models.IntegerField(default=10)

class HourlyWeather(models.Model):
    city = models.ForeignKey(WeatherInfo, on_delete=models.CASCADE, related_name="hourly")
    hour = models.CharField(max_length=4)
    weatherType = models.CharField(max_length=30)

    temperature = models.IntegerField(default=10)