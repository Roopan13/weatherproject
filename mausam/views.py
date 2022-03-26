from django.shortcuts import render
import requests
import datetime

# Create your views here.

def home(request):
   if 'city' in request.POST:
       city = request.POST['city']
   else:
       city = 'Khanna'

   apikey = '5fdeab6b9bbffcc30253c280b4aeb009'
   url = f'https://api.openweathermap.org/data/2.5/weather'
   params = {'q':city,'appid':apikey,'units': 'metric'}
   data = requests.get(url=url , params=params)
   res=data.json()

   payload = {
        'desc' : res['weather'][0]['description'],
        'icon' : res['weather'][0]['icon'],
        'temp' : res['main']['temp'],
        'day' : datetime.date.today(),
        'city' : city
    }
   return render(request,'mausam/home.html' , {'context':payload})

