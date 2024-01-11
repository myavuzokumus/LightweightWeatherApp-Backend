import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from decouple import config
from django.http import HttpResponseRedirect

# Create your views here.
@csrf_exempt
def GooglePlacesAPI(request):

    PLACES_API_KEY = config('GOOGLEAPI_KEY')

    uuid = request.POST.get('uuid', 'uuid')
    suggestionWord = request.POST.get('suggestionWord', 'suggestionWord')

    api_url = f"https://maps.googleapis.com/maps/api/place/autocomplete/json?input={suggestionWord}&key={PLACES_API_KEY}&sessionToken={uuid}&types=country|administrative_area_level_1"

    # GET isteği yap ve yanıtı al
    response = requests.get(api_url)

    if response.status_code == 200:

        data = response.json()
        # Veriyi JSON olarak döndürün
        return JsonResponse(data)

    else:
        # istek başarısız olduysa, hata mesajı yazdır
        print("Request failed with status: {}".format(response.status_code))