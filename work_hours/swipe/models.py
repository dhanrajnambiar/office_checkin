from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# Create your models here.
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)

    def create_employee_profile(sender, instance, created, **kwargs):
        if created:#created == True if the User instance is save()'d.
            Employee.objects.create(user=instance)

    post_save.connect(create_employee_profile, sender=User)# when a User is created
    #post_save signal is triggered and it initiates create_employee_profile Function
    #defined above

    def __str__(self):
        return self.user.username

class checkin(models.Model):
    creator = models.ForeignKey('Employee', on_delete = models.CASCADE)
    time = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.time)

class checkout(models.Model):
    creator = models.ForeignKey('Employee', on_delete = models.CASCADE)
    time = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.time)
