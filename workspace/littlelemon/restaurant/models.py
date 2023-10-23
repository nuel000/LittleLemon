from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    inventory = models.IntegerField(
        validators=[
            MaxValueValidator(99999),  
            MinValueValidator(0),  
        ]
        
    )
    def __str__(self) -> str:
        return self.title
    
class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField(
        validators=[
            MaxValueValidator(999999),  
            MinValueValidator(0),  
        ]
        )
    booking_date = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.name
    

