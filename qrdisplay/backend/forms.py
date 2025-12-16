from django import forms

class Qrform(forms.Form):
    url = forms.CharField(max_length=255)
