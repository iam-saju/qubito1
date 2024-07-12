from django.db import models

# Create your models here.
class users(models.Model):
    username=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    phno=models.CharField(max_length=15)

    def __str__(self):
        return self.username
    


    