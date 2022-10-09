from random import choices
from zoneinfo import available_timezones
from django.db import models


class Daste_Bandi_Ketab(models.Model):
    Name = models.CharField(max_length=150)

    def __str__(self):
        return self.Name


class Nevisandeh(models.Model):
    Name = models.CharField(max_length=150)
    Family = models.CharField(max_length=150)
    Age = models.IntegerField()

    def __str__(self):
        return ' نویسنده ' + self.Name + self.Family


class user(models.Model):
    Name = models.CharField(max_length=150)
    Family = models.CharField(max_length=150)

    def __str__(self):
        return self.Name


class Book(models.Model):
    Name = models.CharField(max_length=150)
    nevisandeh = models.ForeignKey(Nevisandeh, on_delete=models.CASCADE)
    daste_Bandi_Ketab = models.ForeignKey(
        Daste_Bandi_Ketab, on_delete=models.CASCADE)
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    available = {
        ('d', 'dastres'),
        ('a', 'amanat'),
        ('h', 'hazf'),
        ('s', 'sahafi'),
    }
    status = models.CharField(max_length=150, choices=available)

    def __str__(self):
        return self.Name
