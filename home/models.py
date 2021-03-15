# from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

# Create your models here.
NUMBER = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),)

class Region (models.Model):
    name = models.CharField(max_length=300,blank=True, null=True)

    def __str__(self):
        return self.name

class State (models.Model):


    region = models.ForeignKey('Region', null=True, blank=True, on_delete=models.CASCADE)
    number = models.CharField(max_length=255, choices=NUMBER, null=True, blank=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Lga(models.Model):
    state = models.ForeignKey('State', null=True, blank=True, on_delete=models.CASCADE)
    number = models.CharField(max_length=255, choices=NUMBER, null=True, blank=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('home:ads_list_by_category',
    #                    args=[self.slug])

class Center(models.Model):
    lga = models.ForeignKey('Lga',null=True, blank=True,on_delete=models.CASCADE)
    number = models.CharField(max_length=255, choices=NUMBER, null=True, blank=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name




