from django.db import models
import datetime
# Create your models here.

class Breakfast(models.Model):
    Item = models.CharField(max_length=250)
    quantity = models.FloatField()
    date = models.DateField(default=datetime.datetime.today())


    def __str__(self):
        return self.Item


class Nutrients(models.Model):
    item_name = models.CharField(max_length=200)
    protien = models.FloatField(blank=True,null=True)
    carbohydrates = models.FloatField(blank=True,null=True)
    fat = models.FloatField(blank=True,null=True)
    vitamin = models.FloatField(blank=True,null=True)
    mineral = models.FloatField(blank=True,null=True)
    calorie = models.FloatField()
    def __str__(self):
        return self.item_name

