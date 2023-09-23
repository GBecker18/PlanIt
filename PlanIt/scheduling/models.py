from django.db import models


# Create your models here.
class shift(models.Model):
    date = models.DateField()
    time = models.TimeField()
    duration = models.DurationField()
    shiftType = models.CharField(max_length = 255)