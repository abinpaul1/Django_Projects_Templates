from django import forms
from ProApp.models import User

class SignUp(forms.ModelForm):
    class Meta:
        model  = User
        fields = "__all__"
