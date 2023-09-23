from django.db import models


# Create your models here.
class employee(models.Model):
    ID = models.IntegerField(primary_key = True)
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    phoneNumber = models.IntegerField()
    email = models.EmailField()
    level = models.IntegerField()

class shift(models.Model):
    date = models.DateField()
    time = models.TimeField()
    duration = models.DurationField()
    employeeID = models.ForeignKey(employee, on_delete=models.CASCADE)
    shiftType = models.CharField(max_length = 255)