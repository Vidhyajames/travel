

from django.db import models

class Place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    dese=models.TextField()
    def __str__(self):
        return self.name
class Team(models.Model):
    name_Team = models.CharField(max_length=250)
    img_Team = models.ImageField(upload_to='pics')
    dese_Team = models.TextField()
    def __str__(self):
        return self.name_Team

# Create your models here.
