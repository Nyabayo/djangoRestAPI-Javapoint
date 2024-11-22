from django.db import models

# Create your models here.

class Students(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    roll_number = models.CharField(max_length=200)
    mobile_number = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name +" "+ self.last_name