from django import forms
from .models import BowSetup, ArrowBuild
from components.models import ArrowShaft, Vane, Nock, Insert, Broadhead


class BowSetupForm(forms.ModelForm):
    class Meta:
        model = BowSetup
        fields = ['name', 'ibo_speed', 'draw_weight', 'draw_length']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'e.g. Mathews V3X 33'}),
            'ibo_speed': forms.NumberInput(attrs={'placeholder': 'e.g. 330', 'min': 200, 'max': 400}),
            'draw_weight': forms.NumberInput(attrs={'placeholder': 'e.g. 70', 'min': 20, 'max': 100}),
            'draw_length': forms.NumberInput(attrs={'placeholder': 'e.g. 28.5', 'min': 20, 'max': 35, 'step': 0.5}),
        }


class ArrowBuildForm(forms.ModelForm):
    class Meta:
        model = ArrowBuild
        fields = ['name', 'shaft', 'arrow_length', 'vane', 'num_vanes', 'nock', 'insert', 'broadhead']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'e.g. Elk Setup Heavy'}),
            'arrow_length': forms.NumberInput(attrs={'placeholder': 'e.g. 28', 'min': 20, 'max': 35, 'step': 0.25}),
            'num_vanes': forms.NumberInput(attrs={'min': 3, 'max': 4}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        # Show approved components + anything this user submitted
        for field_name, model in [('shaft', ArrowShaft), ('vane', Vane), ('nock', Nock), ('insert', Insert), ('broadhead', Broadhead)]:
            if field_name in self.fields:
                qs = model.objects.filter(status='approved')
                if user:
                    qs = qs | model.objects.filter(submitted_by=user)
                self.fields[field_name].queryset = qs.distinct()
                self.fields[field_name].required = field_name == 'shaft'