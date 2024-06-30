from django.db import models
from django.contrib.auth.models import User


# Create your models here.
#Member(Users), Rides, Articles

class Users(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)  #stored as hash
    #profile_info=models.JSONField(default=dict)
    registration_date = models.DateTimeField(auto_now_add=True)
    last_login_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name


class Rides(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    vehicle_type = models.CharField(max_length=50)
    distance = models.DecimalField(max_digits=10, decimal_places=2)
    co2_emissions = models.DecimalField(max_digits=10, decimal_places=2)
    date_logged = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Ride {self.id} by {self.user.name}"

    def calculate_co2_emissions(self):
        # Implementation to calculate CO2 emissions based on distance and vehicle type
        pass

    def get_vehicle_type_display(self):
        # Example method to get human-readable vehicle type
        return self.vehicle_type


class Articles(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_published = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_summary(self):
        # Example method to return a summary of the article
        return self.content[:200] + '...'
