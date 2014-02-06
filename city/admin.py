from django.contrib import admin

from models import City, CityPicture, Timezone

class CityAdmin(admin.ModelAdmin):
    class Meta:
        model = City
admin.site.register(City, CityAdmin)

class CityPictureAdmin(admin.ModelAdmin):
    class Meta:
        model = CityPicture
admin.site.register(CityPicture, CityPictureAdmin)

class TimezoneAdmin(admin.ModelAdmin):
    class Meta:
        model = Timezone
admin.site.register(Timezone, TimezoneAdmin)

# Register your models here.
