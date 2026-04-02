from django.db import models
from django.conf import settings


class ComponentStatus(models.TextChoices):
    PENDING = 'pending', 'Pending Review'
    APPROVED = 'approved', 'Approved'
    REJECTED = 'rejected', 'Rejected'


class Manufacturer(models.Model):
    name = models.CharField(max_length=100, unique=True)
    website = models.URLField(blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class ArrowShaft(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    model_name = models.CharField(max_length=150)
    spine = models.IntegerField(help_text="Spine rating (e.g. 300, 340, 400)")
    gpi = models.FloatField(help_text="Grains per inch")
    inner_diameter = models.FloatField(help_text="Inner diameter in inches")
    outer_diameter = models.FloatField(blank=True, null=True, help_text="Outer diameter in inches")
    straightness = models.CharField(max_length=20, blank=True, help_text="e.g. .001, .003, .006")
    stock_length = models.FloatField(default=32.0, help_text="Stock length in inches")
    status = models.CharField(max_length=10, choices=ComponentStatus.choices, default=ComponentStatus.PENDING)
    submitted_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['manufacturer', 'model_name', 'spine']
        unique_together = ['manufacturer', 'model_name', 'spine']

    def __str__(self):
        return f"{self.manufacturer} {self.model_name} ({self.spine})"


class Vane(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    model_name = models.CharField(max_length=150)
    length_inches = models.FloatField(help_text="Vane length in inches")
    height_inches = models.FloatField(blank=True, null=True, help_text="Vane height in inches")
    weight_grains = models.FloatField(help_text="Weight per vane in grains")
    status = models.CharField(max_length=10, choices=ComponentStatus.choices, default=ComponentStatus.PENDING)
    submitted_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['manufacturer', 'model_name']
        unique_together = ['manufacturer', 'model_name']

    def __str__(self):
        return f"{self.manufacturer} {self.model_name}"


class Nock(models.Model):
    NOCK_TYPES = [
        ('press', 'Press-Fit'),
        ('pin', 'Pin'),
    ]
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    model_name = models.CharField(max_length=150)
    nock_type = models.CharField(max_length=10, choices=NOCK_TYPES)
    weight_grains = models.FloatField(help_text="Weight in grains")
    compatible_diameter = models.CharField(max_length=20, blank=True, help_text="e.g. .204, .246")
    status = models.CharField(max_length=10, choices=ComponentStatus.choices, default=ComponentStatus.PENDING)
    submitted_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['manufacturer', 'model_name']

    def __str__(self):
        return f"{self.manufacturer} {self.model_name}"


class Insert(models.Model):
    INSERT_TYPES = [
        ('insert', 'Insert'),
        ('outsert', 'Outsert'),
        ('halfout', 'Half-Out'),
    ]
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    model_name = models.CharField(max_length=150)
    insert_type = models.CharField(max_length=10, choices=INSERT_TYPES)
    weight_grains = models.FloatField(help_text="Weight in grains")
    compatible_diameter = models.CharField(max_length=20, blank=True, help_text="e.g. .204, .246")
    material = models.CharField(max_length=50, blank=True, help_text="e.g. Aluminum, Brass, Stainless Steel")
    status = models.CharField(max_length=10, choices=ComponentStatus.choices, default=ComponentStatus.PENDING)
    submitted_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['manufacturer', 'model_name']

    def __str__(self):
        return f"{self.manufacturer} {self.model_name} ({self.weight_grains}gr)"


class Broadhead(models.Model):
    BROADHEAD_TYPES = [
        ('fixed', 'Fixed Blade'),
        ('mechanical', 'Mechanical'),
        ('hybrid', 'Hybrid'),
    ]
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    model_name = models.CharField(max_length=150)
    broadhead_type = models.CharField(max_length=12, choices=BROADHEAD_TYPES)
    weight_grains = models.FloatField(help_text="Weight in grains")
    cutting_diameter = models.FloatField(blank=True, null=True, help_text="Cutting diameter in inches")
    num_blades = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=ComponentStatus.choices, default=ComponentStatus.PENDING)
    submitted_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['manufacturer', 'model_name']
        unique_together = ['manufacturer', 'model_name', 'weight_grains']

    def __str__(self):
        return f"{self.manufacturer} {self.model_name} ({self.weight_grains}gr)"