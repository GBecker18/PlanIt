from django.db import models

#Table containing employee information
class employee(models.Model):
    ID = models.IntegerField(primary_key = True)
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    phoneNumber = models.IntegerField()
    email = models.EmailField()
    level = models.IntegerField()

#Table containing information about shifts
class shift(models.Model):
    date = models.DateField()
    startTime = models.TimeField(null = True)
    endTime = models.TimeField(null = True)
    shiftType = models.CharField(max_length = 255)
    employeeID = models.ForeignKey(employee, null = True, blank = True, on_delete=models.SET_NULL)
    
