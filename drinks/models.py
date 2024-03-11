# this is the model of our api
from django.db import models

class Drink(models.Model):
    name=models.CharField(max_length=200)
    description = models.CharField(max_length =500)
    
    # this line update the name of the drink object in the admin interface
    def __str__(self) -> str:
        return self.name + ' ' + self.description