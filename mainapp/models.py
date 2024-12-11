from django.db import models

# Create your models here.
class Food(models.Model):
    name = models.CharField( max_length = 100)
    carbs = models.FloatField() 
    protien = models.FloatField() 
    fats = models.FloatField() 
    calories = models.IntegerField()

    def __str__(self):
        return f' {self.name, self.calories}'


