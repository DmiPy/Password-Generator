from django import forms

class PasswordEntryForm(forms.Form):
    login = forms.CharField(max_length=100, required=True)
    password = forms.CharField(max_length=16, required=True, widget=forms.PasswordInput)
    website = forms.URLField(required=True)