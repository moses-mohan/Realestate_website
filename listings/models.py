from django.db import models

from django.db import models


class Property(models.Model):
    title = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    price = models.BigIntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='properties/')

    def __str__(self):
        return self.title


class Booking(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
class Inquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    message = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
