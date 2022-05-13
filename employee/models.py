from django.db import models


# Create your models here.

class Employee(models.Model):
    UPLOAD_SKIN_IMAGES = (models.ImageField(upload_to='images/'))
    First_Name = models.CharField(max_length=200,default='First_Name')
    Last_Name = models.CharField(max_length=200,default='Last_Name')
    Patient_Id = models.IntegerField(
        help_text="Enter 6 digit Id",default=1
    )

    def __str__(self):
        return str(self.UPLOAD_SKIN_IMAGES)
