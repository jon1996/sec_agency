from django import forms
from .models import addReport
from django.forms import ModelForm

class PostForms(forms.ModelForm):
    class Meta:
        model = addReport
        fields = ('mouve','nom_Visiteur','fonction','service','motif','phoneNumber')


        widgets = {
            'mouve': forms.Select(attrs={'class': 'form-control'}),
            'nom_Visiteur': forms.TextInput(attrs={'class': 'form-control'}),
            'fonction': forms.TextInput(attrs={'class': 'form-control'}),
            'service': forms.TextInput(attrs={'class': 'form-control'}),
            'motif': forms.Textarea(attrs={'class': 'form-control'}),
            'phoneNumber': forms.TextInput(attrs={'class': 'form-control'}),
        }

        def __init__(self, data=None, *args, **kwargs):

            super().__init__(data, *args, **kwargs)

        # If 'later' is chosen, mark send_dt as required.
            if data and data.get('mouve', None) == self.OUT:
                self.fields['fonction'] = forms.HiddenInput(),
                self.fields['service'] = forms.HiddenInput(),
                
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)