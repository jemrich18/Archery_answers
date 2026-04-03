from django.db import models
from django.conf import settings
from components.models import ArrowShaft, Vane, Nock, Insert, Broadhead


class BowSetup(models.Model):
    """A user's bow configuration - one user might have multiple bows"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, help_text="e.g. Mathews V3X 33")
    ibo_speed = models.IntegerField(help_text="IBO rated speed in FPS")
    draw_weight = models.IntegerField(help_text="Actual draw weight in lbs")
    draw_length = models.FloatField(help_text="Draw length in inches")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} ({self.user.username})"


class ArrowBuild(models.Model):
    """A complete arrow build tied to a bow setup"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bow = models.ForeignKey(BowSetup, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, help_text="e.g. Elk Setup Heavy")
    
    # Components
    shaft = models.ForeignKey(ArrowShaft, on_delete=models.SET_NULL, null=True)
    vane = models.ForeignKey(Vane, on_delete=models.SET_NULL, null=True, blank=True)
    nock = models.ForeignKey(Nock, on_delete=models.SET_NULL, null=True, blank=True)
    insert = models.ForeignKey(Insert, on_delete=models.SET_NULL, null=True, blank=True)
    broadhead = models.ForeignKey(Broadhead, on_delete=models.SET_NULL, null=True, blank=True)
    
    # Build specs
    arrow_length = models.FloatField(help_text="Cut length in inches")
    num_vanes = models.IntegerField(default=3)
    
    # Calculated fields (stored so we don't recalculate every page load)
    total_arrow_weight = models.FloatField(blank=True, null=True)
    arrow_speed = models.FloatField(blank=True, null=True)
    kinetic_energy = models.FloatField(blank=True, null=True)
    momentum = models.FloatField(blank=True, null=True)
    foc = models.FloatField(blank=True, null=True, help_text="Front of Center %")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at']

    def __str__(self):
        return f"{self.name} - {self.bow.name} ({self.user.username})"

    def calculate(self):
        """Calculate all ballistics from components and bow setup"""
        # Total arrow weight
        shaft_weight = (self.shaft.gpi * self.arrow_length) if self.shaft else 0
        vane_weight = (self.vane.weight_grains * self.num_vanes) if self.vane else 0
        nock_weight = self.nock.weight_grains if self.nock else 0
        insert_weight = self.insert.weight_grains if self.insert else 0
        broadhead_weight = self.broadhead.weight_grains if self.broadhead else 0

        self.total_arrow_weight = shaft_weight + vane_weight + nock_weight + insert_weight + broadhead_weight

        # Arrow speed from IBO
        speed = self.bow.ibo_speed
        speed -= (30 - self.bow.draw_length) * 10  # 10 FPS per inch under 30
        speed -= (70 - self.bow.draw_weight) * 1.75  # ~17.5 FPS per 10 lbs under 70
        speed -= (self.total_arrow_weight - 350) * (1.5 / 5)  # 1.5 FPS per 5gr over 350
        self.arrow_speed = max(speed, 0)

        # Kinetic energy: KE = (mv^2) / 450240
        self.kinetic_energy = (self.total_arrow_weight * self.arrow_speed ** 2) / 450240

        # Momentum: p = (mv) / 225120
        self.momentum = (self.total_arrow_weight * self.arrow_speed) / 225120

        # FOC estimation
        if self.total_arrow_weight > 0 and self.arrow_length > 0:
            front_weight = insert_weight + broadhead_weight
            vane_position = 1.5  # inches from nock end
            
            # Center of mass calculation (measured from nock end)
            balance_point = (
                (front_weight * self.arrow_length) +
                (shaft_weight * (self.arrow_length / 2)) +
                (vane_weight * vane_position) +
                (nock_weight * 0)
            ) / self.total_arrow_weight

            midpoint = self.arrow_length / 2
            self.foc = ((balance_point - midpoint) / self.arrow_length) * 100
        else:
            self.foc = 0

    def save(self, *args, **kwargs):
        if self.shaft and self.bow:
            self.calculate()
        super().save(*args, **kwargs)