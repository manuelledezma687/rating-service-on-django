from django.db import models
from django.utils import timezone
import datetime

class Rating(models.Model):
    first_name = models.CharField(max_length=20)
    last_name= models.CharField(max_length=20)
    comments = models.CharField(max_length=50)
    stars = models.IntegerField(default=5)
    pub_date = models.DateTimeField("date published")
    
    
    def __str__(self):
        return self.comments
    
    def was_published_recently(self):
        return timezone.now() >= self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
class Booking(models.Model):
    pick_up = models.CharField(max_length=50)
    destiny = models.CharField(max_length=50)
    full_name = models.CharField(max_length=50)
    email= models.EmailField(max_length=20)
    flight = models.CharField(max_length=20)
    date = models.CharField(max_length=50)  ##
    date_time = models.CharField(max_length=50)  ##
    payment_method = models.CharField(max_length=50)
    type_of_travel = models.CharField(max_length=12)                  
    observations = models.CharField(max_length=100)
    passengers = models.IntegerField(default=1)

    
