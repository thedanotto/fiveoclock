from django.shortcuts import render, render_to_response, RequestContext
from django.utils.timezone import utc

from datetime import datetime, timedelta
import pytz
from pytz import timezone

from functions import current_5oclock_timezone, get_local_now, get_utc_now
from models import City, CityPicture, Timezone
from yelp import yelp_request_url, yelp_values

def home(request):
    five_oclock_tz = current_5oclock_timezone()
    timezone = Timezone.objects.get(name=five_oclock_tz)
    city = City.objects.get(timezone=timezone)
    local_now = get_local_now(timezone)
    str_local_now = local_now.strftime('%I:%M:%S %p')
    '''
    #WHAT TIME ZONIZZLES AM I MISSING??
    timezones = Timezone.objects.all()
    for timezone in timezones:
        a_time = get_local_now(timezone)
        timezone.hour = a_time.hour
    '''
    if request.method == 'POST':
        zip_code = request.POST.get('zip_code')
        full_url = yelp_request_url(zip_code)
        locations = yelp_values(full_url)
        if len(locations) == 0:
            no_results = True
        else:
            no_results = False
#        what_you_get = locations[0][1].split(".")

    
    default_background_image_url = 'http://upload.wikimedia.org/wikipedia/commons/thumb/8/8b/Tango_-_Bastille_Day_2008_-_Juneau_Town_-_Milwaukee%2C_Wisconsin_-_USA.jpg/800px-Tango_-_Bastille_Day_2008_-_Juneau_Town_-_Milwaukee%2C_Wisconsin_-_USA.jpg'
    return render_to_response('home.html', locals(), context_instance=RequestContext(request))


# Create your views here.
