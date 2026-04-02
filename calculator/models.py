from django.db import models

# Create your models here.
class AnimalThreshold(models.Model):
    name = models.CharField(max_length=100)
    min_kinetic_energy = models.FloatField(help_text="Minimum KE in ft-lbs")
    min_momentum = models.FloatField(help_text="Minimum momentum in slug-ft/s")
    icon = models.CharField(max_length=10, blank=True)
    sort_order = models.IntegerField(default=0)


    class Meta:
        ordering = ['sort_order']

    def __str__(self):
        return self.name
