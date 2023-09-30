from django.contrib import admin
from .models import employee
from .models import shift

#Make display of models more reader-friendly by creating classes: 'tableName'Admin()
class employeeAdmin(admin.ModelAdmin):
    list_display = ("firstName", "lastName", "ID",)

class shiftAdmin(admin.ModelAdmin):
    list_display = ("shiftType", "date", "startTime", "endTime",)

# Register your models here.
admin.site.register(employee, employeeAdmin)
admin.site.register(shift, shiftAdmin)


