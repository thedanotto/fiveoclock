from django.shortcuts import render, render_to_response, RequestContext
from django.utils.timezone import utc

from datetime import datetime, timedelta
import pytz
from pytz import timezone

from functions import current_5oclock_timezone, get_local_now, get_utc_now
from models import City, CityPicture, Timezone

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
    return render_to_response('home.html', locals(), context_instance=RequestContext(request))


# Create your views here.
