from django import forms
from django.core import validators

def check_for_a(value):
    if value[0].lower() != 'a':
        raise forms.ValidationError("Make sure name starts with A")

class First_form(forms.Form):
    name = forms.CharField(validators=[check_for_a])
    email = forms.EmailField()
    verify_email = forms.EmailField()
    text = forms.CharField(widget = forms.Textarea)

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data.get('email')
        vmail = all_clean_data.get('verify_email')

        if email != vmail:
            raise forms.ValidationError("Make sure Emails match")
