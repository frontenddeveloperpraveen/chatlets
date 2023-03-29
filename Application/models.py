from django.db import models
from datetime import datetime as dt
class Room(models.Model):
    name = models.CharField(max_length=100)
    creater = models.CharField(max_length=100)
    date = models.DateTimeField(default=dt.now(),blank=True)

class Message(models.Model):
    msg = models.CharField(max_length=10000)
    room = models.CharField(max_length=100)
    sender = models.CharField(max_length=100)
    date = models.DateTimeField(default=dt.now(),blank=True)

