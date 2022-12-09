from django.db import models


# Create your models here.
class Contact(models.Model):
    def __str__(self):
        return self.fname
    fname = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    message = models.CharField(max_length=200)
