from datetime import datetime
import pytz
from pytz import timezone

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