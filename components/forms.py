from django import forms
from .models import ArrowShaft, Vane, Nock, Insert, Broadhead, Manufacturer


class ManufacturerMixin(forms.ModelForm):
    """Lets user type a manufacturer name instead of picking from dropdown"""
    manufacturer_name = forms.CharField(max_length=100, help_text="e.g. Easton, Gold Tip, Black Eagle")

    def clean_manufacturer_name(self):
        name = self.cleaned_data['manufacturer_name'].strip()
        manufacturer, _ = Manufacturer.objects.get_or_create(name__iexact=name, defaults={'name': name})
        return manufacturer


class ArrowShaftForm(ManufacturerMixin):
    class Meta:
        model = ArrowShaft
        fields = ['model_name', 'spine', 'gpi', 'inner_diameter', 'outer_diameter', 'straightness']

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.manufacturer = self.cleaned_data['manufacturer_name']
        if commit:
            instance.save()
        return instance


class VaneForm(ManufacturerMixin):
    class Meta:
        model = Vane
        fields = ['model_name', 'length_inches', 'height_inches', 'weight_grains']

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.manufacturer = self.cleaned_data['manufacturer_name']
        if commit:
            instance.save()
        return instance


class NockForm(ManufacturerMixin):
    class Meta:
        model = Nock
        fields = ['model_name', 'nock_type', 'weight_grains', 'compatible_diameter']

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.manufacturer = self.cleaned_data['manufacturer_name']
        if commit:
            instance.save()
        return instance


class InsertForm(ManufacturerMixin):
    class Meta:
        model = Insert
        fields = ['model_name', 'insert_type', 'weight_grains', 'compatible_diameter', 'material']

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.manufacturer = self.cleaned_data['manufacturer_name']
        if commit:
            instance.save()
        return instance


class BroadheadForm(ManufacturerMixin):
    class Meta:
        model = Broadhead
        fields = ['model_name', 'broadhead_type', 'weight_grains', 'cutting_diameter', 'num_blades']

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.manufacturer = self.cleaned_data['manufacturer_name']
        if commit:
            instance.save()
        return instance