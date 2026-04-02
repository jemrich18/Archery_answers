from django.core.management.base import BaseCommand
from calculator.models import AnimalThreshold


class Command(BaseCommand):
    help = 'Seed animal threshold data'

    def handle(self, *args, **kwargs):
        thresholds = [
            {'name': 'Turkey / Small Game', 'min_kinetic_energy': 25, 'min_momentum': 0.25, 'icon': '🦃', 'sort_order': 1},
            {'name': 'Whitetail Deer', 'min_kinetic_energy': 42, 'min_momentum': 0.40, 'icon': '🦌', 'sort_order': 2},
            {'name': 'Black Bear', 'min_kinetic_energy': 52, 'min_momentum': 0.50, 'icon': '🐻', 'sort_order': 3},
            {'name': 'Elk / Moose', 'min_kinetic_energy': 60, 'min_momentum': 0.55, 'icon': '🫎', 'sort_order': 4},
            {'name': 'African Plains Game', 'min_kinetic_energy': 70, 'min_momentum': 0.65, 'icon': '🦬', 'sort_order': 5},
        ]

        for t in thresholds:
            obj, created = AnimalThreshold.objects.get_or_create(
                name=t['name'],
                defaults=t
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created: {obj.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Already exists: {obj.name}'))

        self.stdout.write(self.style.SUCCESS('Done!'))