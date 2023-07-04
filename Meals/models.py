from django.db import models

# Create your models here.

class Food(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=500)
    location = models.CharField(max_length=500)
    items = models.TextField()
    lat_long = models.CharField(max_length=500)
    full_details = models.TextField()

    def __str__(self):
        return self.name
