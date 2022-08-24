from django import forms
from .models import Positions


class PositionForm(forms.ModelForm):
    class Meta:
        model   = Positions
        fields  = ('title', 'description', 'amount')
