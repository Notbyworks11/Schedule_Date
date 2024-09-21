from django.db import models

# Create your models here.
class Activity(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    created_at = models.DateField( auto_now_add=True)

    def __str__(self):
        return self.name