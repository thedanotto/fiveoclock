from django.shortcuts import render, render_to_response, RequestContext
from django.utils.timezone import utc

from datetime import datetime, timedelta
from random import randrange
import pytz
from pytz import timezone


from functions import current_5oclock_timezone, get_local_now, get_utc_now, find_city_zip, point_distance_calculator
from models import City, CityPicture, Timezone
from yelp import yelp_request_url, yelp_values

def home(request):
    five_oclock_tz = current_5oclock_timezone()
    timezone = Timezone.objects.get(name=five_oclock_tz)
    cities = City.objects.filter(timezone=timezone)
    if cities.count() == 1:
        city = City.objects.get(timezone=timezone)
    else:
        city_ids = []
        for city in cities:
            city_ids.append(city.id)
        total_cities = len(city_ids)
        city_id = city_ids[randrange(total_cities)]
    city = City.objects.get(id=city_id)
    # city = find a way to pick the city 
    local_now = get_local_now(timezone)
    str_local_now = local_now.strftime('%I:%M:%S %p')
    '''
    #WHAT TIME ZONIZZLES AM I MISSING??
    timezones = Timezone.objects.all()
    for timezone in timezones:
        a_time = get_local_now(timezone)
        timezone.hour = a_time.hour
    '''
    source_picture = True
    if request.method == 'POST':
        source_picture = False
        zip_code = request.POST.get('zip_code')

        full_url = yelp_request_url(zip_code)
        try:
            businesses = yelp_values(full_url)
            if len(businesses) == 0:
                no_results = True
            else:
                no_results = False
                
        except:
            no_results = True
        
        
        

    
    default_background_image_url = 'http://upload.wikimedia.org/wikipedia/commons/thumb/8/8b/Tango_-_Bastille_Day_2008_-_Juneau_Town_-_Milwaukee%2C_Wisconsin_-_USA.jpg/800px-Tango_-_Bastille_Day_2008_-_Juneau_Town_-_Milwaukee%2C_Wisconsin_-_USA.jpg'
    return render_to_response('home.html', locals(), context_instance=RequestContext(request))


# Create your views here.
