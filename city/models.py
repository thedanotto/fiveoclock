from django.db import models

class Timezone(models.Model):
    name = models.CharField(max_length=50)
    tz_code = models.CharField(max_length=10)
    def __unicode__(self, ):
        return '%s, %s' %(self.name, self.tz_code)

class City(models.Model):
    city_name = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)    
    timezone = models.ForeignKey(Timezone)
    
    def __unicode__(self, ):
        return self.city_name
    

class CityPicture(models.Model):
    city = models.ForeignKey(City)
    image = models.ImageField(upload_to='cities/')
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']
    
    def __unicode__(self, ):
        return str(self.image)


# Create your models here.
