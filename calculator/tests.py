from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import AnimalThreshold


class AnimalThresholdModelTest(TestCase):
    def setUp(self):
        self.animal = AnimalThreshold.objects.create(
            name='Whitetail Deer',
            min_kinetic_energy=40.0,
            min_momentum=0.4,
            icon='🦌',
            sort_order=1
        )

    def test_animal_created(self):
        self.assertEqual(self.animal.name, 'Whitetail Deer')

    def test_animal_thresholds(self):
        self.assertEqual(self.animal.min_kinetic_energy, 40.0)
        self.assertEqual(self.animal.min_momentum, 0.4)

    def test_animal_str(self):
        self.assertEqual(str(self.animal), 'Whitetail Deer')

    def test_animal_ordering(self):
        AnimalThreshold.objects.create(
            name='Elk',
            min_kinetic_energy=65.0,
            min_momentum=0.6,
            sort_order=2
        )
        animals = AnimalThreshold.objects.all()
        self.assertEqual(animals[0].name, 'Whitetail Deer')
        self.assertEqual(animals[1].name, 'Elk')