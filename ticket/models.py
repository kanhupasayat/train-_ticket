import random
import string
from django.db import models

class Ticket(models.Model):
    train = models.CharField(max_length=50)
    passenger = models.CharField(max_length=100)
    state_depart = models.CharField(max_length=50)
    state_arrive = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    carriage = models.IntegerField()
    seat = models.CharField(max_length=50, blank=True, editable=False)
    platform=models.CharField(max_length=50,blank=True,editable=False)

    def __str__(self):
        return f"{self.train} - {self.passenger}"

    def save(self, *args, **kwargs):
        if not self.seat:
            self.seat = self.generate_seat()
        if not self.platform:
            self.platform=self.generate_platform()
        super().save(*args, **kwargs)



    def generate_seat(self):
        # Generate a random letter from A to Z
        x=['A','B','C']
        letter = random.choice(x)
        # Generate a random number from 1 to 99
        number = random.randint(1, 99)
        # Combine letter and number to form seat identifier
        return f"{letter}{number}"
    
    def generate_platform(self):
        # Generate a random number from 1 to 99
        number = random.randint(1,7)
        return f"{number}"




    
    



    






