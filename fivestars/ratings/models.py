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
    

