from django import forms

from .models import Member


class InscriptionForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ('civility', 'name', 'surname', 'address', 'locality', 'npa', 'mail', 'phone_number')
