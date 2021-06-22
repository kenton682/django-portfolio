from django.db import models


# Create your models here.

class Card(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=250)
    image = models.ImageField(upload_to = "static/images", height_field= None, width_field= None, max_length= None)
    pub_date = models.DateTimeField('date published')


    