from django.db import models

# Create your models here.
class Menu(models.Model):
    image = models.ImageField() 
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name