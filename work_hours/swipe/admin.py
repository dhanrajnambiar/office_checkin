from django.contrib import admin

from swipe.models import Employee, checkin, checkout
# Register your models here.

class EmpAdmin(admin.ModelAdmin):
    class Meta:
        model = Employee
    list_display = ['user',]

class checkinAdmin(admin.ModelAdmin):
    class Meta:
        model = checkin
    list_display = ['creator','time']

class checkoutAdmin(admin.ModelAdmin):
    class Meta:
        model = checkout
    list_display = ['creator','time']

admin.site.register(Employee,EmpAdmin)
admin.site.register(checkin,checkinAdmin)
admin.site.register(checkout,checkoutAdmin)
