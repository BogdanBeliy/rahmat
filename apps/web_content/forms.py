from django import forms
from .models import Lead


class LeadForm(forms.ModelForm):
    name = forms.CharField(label='Name', widget=forms.TextInput(
        attrs={'class': "form-control"}))
    phone = forms.CharField(label='Phone', widget=forms.TextInput(
                              attrs={'class': "form-control"}))

    class Meta:
        model = Lead
        fields = ['name', 'phone']
