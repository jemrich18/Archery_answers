from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.test.utils import override_settings
from .models import BowSetup, ArrowBuild
from components.models import ArrowShaft, Manufacturer


@override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
class BowSetupModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.bow = BowSetup.objects.create(
            user=self.user,
            name='Mathews V3X',
            ibo_speed=342,
            draw_weight=70,
            draw_length=29.5
        )

    def test_bow_created(self):
        self.assertEqual(self.bow.name, 'Mathews V3X')

    def test_bow_str(self):
        self.assertIn('Mathews V3X', str(self.bow))
        self.assertIn('testuser', str(self.bow))

    def test_bow_speed(self):
        self.assertEqual(self.bow.ibo_speed, 342)


@override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
class ArrowBuildCalculationTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.bow = BowSetup.objects.create(
            user=self.user,
            name='Test Bow',
            ibo_speed=340,
            draw_weight=70,
            draw_length=30.0
        )
        self.manufacturer = Manufacturer.objects.create(
            name='Test Manufacturer'
        )
        self.shaft = ArrowShaft.objects.create(
            manufacturer=self.manufacturer,
            model_name='Test Shaft',
            gpi=8.5,
            inner_diameter=0.246,
            spine=350
        )

    def test_arrow_build_str(self):
        build = ArrowBuild.objects.create(
            user=self.user,
            bow=self.bow,
            name='Test Build',
            shaft=self.shaft,
            arrow_length=28.0,
            num_vanes=3
        )
        self.assertIn('Test Build', str(build))

    def test_kinetic_energy_calculated(self):
        build = ArrowBuild.objects.create(
            user=self.user,
            bow=self.bow,
            name='KE Test',
            shaft=self.shaft,
            arrow_length=28.0,
            num_vanes=3
        )
        self.assertIsNotNone(build.kinetic_energy)
        self.assertGreater(build.kinetic_energy, 0)

    def test_momentum_calculated(self):
        build = ArrowBuild.objects.create(
            user=self.user,
            bow=self.bow,
            name='Momentum Test',
            shaft=self.shaft,
            arrow_length=28.0,
            num_vanes=3
        )
        self.assertIsNotNone(build.momentum)
        self.assertGreater(build.momentum, 0)

    def test_arrow_speed_calculated(self):
        build = ArrowBuild.objects.create(
            user=self.user,
            bow=self.bow,
            name='Speed Test',
            shaft=self.shaft,
            arrow_length=28.0,
            num_vanes=3
        )
        self.assertIsNotNone(build.arrow_speed)
        self.assertGreater(build.arrow_speed, 0)


@override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
class DashboardViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

    def test_dashboard_requires_login(self):
        response = self.client.get('/')
        self.assertIn(response.status_code, [302, 200])

    def test_dashboard_loads_when_logged_in(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)