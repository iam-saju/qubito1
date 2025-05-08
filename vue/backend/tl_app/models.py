from django.db import models

class Chat(models.Model):
    phno=models.IntegerField(unique=True)
    username=models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.phno

    
