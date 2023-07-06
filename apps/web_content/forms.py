from django import forms
from .models import Lead


class LeadForm(forms.ModelForm):
    name = forms.CharField(label='Name')
    phone = forms.CharField(label='Phone')

    class Meta:
        model = Lead
        fields = ['name', 'phone']
