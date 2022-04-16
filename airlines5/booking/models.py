from datetime import datetime
from django.db import models

from uuid import uuid4

def generation():
    generate = str(uuid4())
    new_id = Identification.objects.filter(saved_id=generate)
    try:
        while new_id[0]:
            generate = str(uuid4())
            new_id = Identification.objects.filter(saved_id=generate)    
        new_id.save()
        return generate
    except:
        new_id = Identification(saved_id=generate)
        new_id.save()
        return generate 

class Identification(models.Model):
    saved_id = models.CharField(max_length=36)

    def __str__(self) -> str:
        return self.saved_id



class Airport(models.Model):
    unique_id   = models.CharField(max_length=36, blank=True)
    name        = models.CharField(max_length=250)
    localcode   = models.IntegerField()
    country     = models.CharField(max_length=250)
    region      = models.CharField(max_length=250) 

    def save(self, *args, **kwargs):
        self.unique_id = generation()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name


class Aircraft(models.Model):
    unique_id   = models.CharField(max_length=36, blank=True)
    model       = models.CharField(max_length=100)
    seats       = models.IntegerField(default=60)
    km_tot      = models.IntegerField(default=0)
    pilots_num  = models.IntegerField(default=4)
    team_num    = models.IntegerField(default=4)

    def save(self, *args, **kwargs):
        self.unique_id = generation()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.model + ' ' + str(self.id)


class Fly(models.Model):
    unique_id   = models.CharField(max_length=36, blank=True)
    aircraft    = models.ForeignKey(Aircraft, on_delete=models.SET_NULL, null=True, related_name='aircraft')
    start       = models.ForeignKey(Airport, on_delete=models.SET_NULL, null=True, related_name='start')
    arrive      = models.ForeignKey(Airport, on_delete=models.SET_NULL, null=True, related_name='arrive')
    date        = models.DateField(default=datetime.now)
    hour        = models.TimeField(default=datetime.now)

    def save(self, *args, **kwargs):
        self.unique_id = generation()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return str(self.start) + ' - ' + str(self.arrive) + ' ' +str(self.date)


class Search(models.Model):
    start       = models.ForeignKey(Airport, on_delete=models.SET_NULL, null=True, related_name='S_start')
    arrive      = models.ForeignKey(Airport, on_delete=models.SET_NULL, null=True, related_name='S_arrive')
    date        = models.DateField(default=datetime.now)

    def __str__(self) -> str:
        return str(self.start) + ' ' + str(self.arrive) + ' ' + str(self.date)


class Booking(models.Model):
    unique_id       = models.CharField(max_length=36, blank=True)
    fly             = models.ForeignKey(Fly, on_delete=models.SET_NULL, null=True, related_name='fly_booking')
    airC_seat       = models.CharField(max_length=5)
    name            = models.CharField(max_length=200)
    surname         = models.CharField(max_length=200)
    email           = models.EmailField()
    address         = models.CharField(max_length=200)
    city            = models.CharField(max_length=200)
    state           = models.CharField(max_length=200)
    zip_code        = models.IntegerField()

    def save(self, *args, **kwargs):
        self.unique_id = generation()
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.fly) +  ' ' + str(self.id)




