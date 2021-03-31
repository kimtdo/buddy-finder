from django import forms

class DeleteForm(forms.Form):
    user=forms.CharField(max_length=100)