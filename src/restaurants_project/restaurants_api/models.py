from django.db import models

# Create your models here.

class RestaurantItem(models.Model):
    """This is the restaurant model."""

    name = models.CharField(max_length=255, unique=True)
    opens_at = models.DateTimeField(blank=True)
    closes_at = models.DateTimeField(blank=True)

    REQUIRED_FIELDS = ['name']

    def __str__(self):
        """Return the model as a string."""

        return self.name
