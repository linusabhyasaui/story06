from random import randint

from django.db import models
from django.forms import forms
from django.http import request
from django.shortcuts import get_object_or_404, redirect


class Event(models.Model):
    name = models.CharField(max_length=500)
    participants = {}
    participant_count = 0

    def delete(self):
        self.delete()

    def __str__(self):
        return self.name


class Participant(models.Model):
    name = models.CharField(max_length=500)
    event_key = models.ForeignKey(Event, on_delete=models.CASCADE)
    # event_choice = models.ManyToManyField(Event, null=True)

    def delete(self):
        self.delete()

    def __str__(self):
        return self.name
