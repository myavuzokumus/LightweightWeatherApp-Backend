import requests
import datetime
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from api.models import WeatherInfo, DailyWeather, HourlyWeather
from .serializers import WeatherInfoSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from datetime import timedelta
from decouple import config

# Create your views here.
class WeatherInfoAPI(viewsets.ModelViewSet):

    queryset = WeatherInfo.objects.all()
    serializer_class = WeatherInfoSerializer

    def list(self, request):

        oldCity=self.request.query_params.get("city", None)

        if not oldCity:
            queryset = WeatherInfo.objects.all()
            serializer = WeatherInfoSerializer(queryset, many=True)
            return Response(serializer.data)

        updateCity = WeatherInfo.objects.filter(city=oldCity).first()

        if not updateCity:
            return Response({"message": "Please provide a valid id."})

        else:
            if updateCity.timestamp < timezone.now() - timedelta(minutes=15):

                todayDate = (datetime.date.today() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
                AfterSevenDayDate = (datetime.date.today() + datetime.timedelta(days=7)).strftime("%Y-%m-%d")

                WEATHERAPI_TOKEN = config('WEATHERAPI_KEY')

                api_url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{oldCity}/{todayDate}/{AfterSevenDayDate}?unitGroup=metric&key={WEATHERAPI_TOKEN}"

                response = requests.get(api_url)

                if response.status_code == 200:
                    # yanıtın içeriğini JSON olarak oku
                    data = response.json()

                    updateCity.delete()
                    # JSON verilerini WeatherInfo modeline uygun bir şekilde kaydet
                    weather = WeatherInfo(
                        city=oldCity,
                        currentWeather=data["days"][1]["icon"],
                        instantTemperature=data["days"][1]["temp"],
                        dayTemperature=data["days"][1]["tempmax"],
                        nightTemperature=data["days"][1]["tempmin"],
                        feelsLike=data["days"][1]["feelslike"],
                        humidity=data["days"][1]["humidity"]
                    )
                    weather.save()

                    # JSON verilerini DailyWeather modeline uygun bir şekilde kaydet
                    for day in data["days"]:
                        daily = DailyWeather(
                            city=weather,
                            date=datetime.datetime.strptime(day["datetime"], "%Y-%m-%d").date(),
                            dayWeather=day["icon"],
                            nightWeather=day["hours"][20]["icon"],
                            dayTemperature=day["tempmax"],
                            nightTemperature=day["tempmin"],
                            humidity=day["humidity"]
                        )
                        daily.save()
                    for hour in data["days"][0]["hours"]:
                        hourly = HourlyWeather(
                            city=weather,
                            hour=datetime.datetime.strptime(hour["datetime"], "%H:%M:%S").time().strftime(
                                "%H:%M"),
                            weatherType=hour["icon"],
                            temperature=hour["temp"]
                        )
                        hourly.save()
                    # veriyi JSON formatında döndür
                    serializer = WeatherInfoSerializer(weather)
                    return Response(serializer.data)
                else:
                    # istek başarısız olduysa, hata mesajı yazdır
                    print("Request failed with status: {}".format(response.status_code))
                    serializer = WeatherInfoSerializer(updateCity)
                    return Response(serializer.data)
            else:
                serializer = WeatherInfoSerializer(updateCity)
                return Response(serializer.data)

    def create(self, request):

        todayDate = (datetime.date.today() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
        AfterSevenDayDate = (datetime.date.today() + datetime.timedelta(days=7)).strftime("%Y-%m-%d")

        WEATHERAPI_TOKEN = config('WEATHERAPI_KEY')

        api_url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{request.data['city']}/{todayDate}/{AfterSevenDayDate}?unitGroup=metric&key={WEATHERAPI_TOKEN}"

        # GET isteği yap ve yanıtı al
        response = requests.get(api_url)

        # yanıtın durum kodunu kontrol et
        if response.status_code == 200:
            # yanıtın içeriğini JSON olarak oku
            data = response.json()

            # JSON verilerini WeatherInfo modeline uygun bir şekilde kaydet
            weather = WeatherInfo(
                city=request.data["city"],
                currentWeather=data["days"][1]["icon"],
                instantTemperature=data["days"][1]["temp"],
                dayTemperature=data["days"][1]["tempmax"],
                nightTemperature=data["days"][1]["tempmin"],
                feelsLike=data["days"][1]["feelslike"],
                humidity=data["days"][1]["humidity"]
            )
            weather.save()

            # JSON verilerini DailyWeather modeline uygun bir şekilde kaydet
            for day in data["days"]:
                daily = DailyWeather(
                    city=weather,
                    date=datetime.datetime.strptime(day["datetime"], "%Y-%m-%d").date(),
                    dayWeather=day["icon"],
                    nightWeather=day["hours"][20]["icon"],
                    dayTemperature=day["tempmax"],
                    nightTemperature=day["tempmin"],
                    humidity=day["humidity"]
                )
                daily.save()
            for hour in data["days"][0]["hours"]:
                hourly = HourlyWeather(
                    city=weather,
                    hour=datetime.datetime.strptime(hour["datetime"], "%H:%M:%S").time().strftime(
                        "%H:%M"),
                    weatherType=hour["icon"],
                    temperature=hour["temp"]
                )
                hourly.save()
            # veriyi JSON formatında döndür
            serializer = WeatherInfoSerializer(weather)
            return Response(serializer.data)
        else:
            # istek başarısız olduysa, hata mesajı yazdır
            print("Request failed with status: {}".format(response.status_code))