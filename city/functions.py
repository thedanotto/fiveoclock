from datetime import datetime
import pytz
from pytz import timezone
from geopy import geocoders

from models import Timezone

def current_5oclock_timezone():
    timezones = Timezone.objects.all()
    for timezone in timezones:
        a_time = get_local_now(timezone)
        if a_time.hour == 17:
            fiveoclock_timezone = timezone.name

    #fiveoclock_timezone = 'America/Los_Angeles'
    
    return fiveoclock_timezone

def get_utc_now():
    utc = pytz.utc
    now = datetime.now()
    utc_now = utc.localize(now)
    return utc_now

def get_local_now(timezone):
    local_timezone = pytz.timezone(timezone.name)
    utc_now = get_utc_now()
    local_now = utc_now.astimezone(local_timezone)
    return local_now

def utc_to_local(utc_date_time, local_timezone):
    local_timezone = pytz.timezone(local_timezone)
    local_date_time = utc_date_time.astimezone(local_timezone)
    return local_date_time

def find_city_zip(zip_code):
    g = geocoders.GoogleV3()
    place, (lat, lng) = g.geocode(zip_code)
    full_address = place.split(', ')
    return lat, lng


def point_distance_calculator(biz_lat, biz_lng, zip_lat, zip_lng):
    zip_lat = float(zip_lat)
    zip_lng = float(zip_lng)
    biz_lat = float(biz_lat)
    biz_lng = float(biz_lng)

    
    R = 3963.1905919; # earth's mean radius in km
    dLat  = rad(zip_lat - biz_lat);
    dLong = rad(zip_lng - biz_lng);
    
    a = math.sin(dLat/2) * math.sin(dLat/2) + math.cos(rad(biz_lat)) * math.cos(rad(zip_lat)) * math.sin(dLong/2) * math.sin(dLong/2);
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a));
    d = R * c;
    
    return d;

    #6.47633299108
def rad(x):
    return x*math.pi/180;

