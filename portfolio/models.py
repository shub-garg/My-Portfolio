from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    phone = models.IntegerField(
        validators=[
            MinValueValidator(1000000000),
            MaxValueValidator(9999999999), 
        ]
    )
    ext = models.CharField(max_length=5)
    subject = models.TextField(null=True)
    description = models.TextField()


    def __str__(self):
        return self.name
