from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Category(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=255, db_index=True)
    def __str__(self):
        return self.title


class Booking(models.Model):
       name = models.CharField(max_length=255)
       num_of_guests = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(999999)])
       booking_date = models.DateTimeField()

       def __str__(self) -> str:
           return f"{self.name} - {self.booking_date}"

class Menu(models.Model):
        title = models.CharField(max_length=255)
        price = models.DecimalField(max_digits=10, decimal_places=2)
        inventory = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(999999)])

        def __str__(self) -> str:
            return f"{self.title}"