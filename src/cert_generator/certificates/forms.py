from django import forms
from .models import CertificateTemplate


class CertificateGenerationForm(forms.Form):
    participant_name = forms.CharField(max_length=200)
    template = forms.ModelChoiceField(queryset=CertificateTemplate.objects.all())
