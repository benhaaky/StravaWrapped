from django.db import models
from django.core import serializers
from django.db.models.signals import post_save
from django.dispatch import receiver
import json
import requests

class Token(models.Model):
    token_type = models.CharField(max_length=60)
    expires_at = models.BigIntegerField()
    expires_in = models.PositiveIntegerField()
    refresh_token = models.CharField(primary_key=True, max_length=100)
    access_token = models.CharField(max_length=100)
    def __str__(self):
        return self.refresh_token

class Map(models.Model):
    id  = models.CharField(primary_key=True, max_length=200, default='error')
    polyline = models.CharField(max_length=1000000, blank=True, default='error')
    resource_state = models.IntegerField(default=3)
    summary_polyline = models.CharField(max_length=1000000, blank=True, default="error")
    def __int__(self):
        return self.id

class Athlete(models.Model):
    id = models.IntegerField(primary_key=True, default='error')
    refresh_token = models.ForeignKey(Token, max_length=200, on_delete=models.CASCADE)
    def __int__(self):
        return self.id

class AuthCode(models.Model):
    code = models.CharField(max_length=200, default='error')
    def __str__(self):
        return self.code

class Activity(models.Model):
    id = models.IntegerField(primary_key=True, default=0)
    type = models.CharField(max_length=200, default='error')
    name = models.CharField(max_length=200, blank=True, default='error')
    map = models.ForeignKey(Map, blank=True, max_length=200, on_delete=models.CASCADE)
    athlete_id = models.ForeignKey(Athlete, on_delete=models.CASCADE)
    moving_time = models.IntegerField()
    elapsed_time = models.IntegerField()
    distance = models.IntegerField()
    total_elevation_gain = models.IntegerField()
    kudos_count = models.IntegerField()
    max_speed = models.IntegerField()
    average_speed = models.IntegerField()
    # different name so that dict mapper doesnt pick it up
    start_date = models.CharField(max_length=200, default='error')

    def __int__(self):
        return self.id
