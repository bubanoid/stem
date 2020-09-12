from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = ('name', 'email', 'event')
        widgets = {
            'name':forms.TextInput(attrs={'id':'id_name'}),
            'email':forms.TextInput(attrs={"id": "demo-email"})
        }
