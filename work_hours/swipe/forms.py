from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class signupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class loginForm(forms.Form):
    username = forms.CharField(max_length = 200)
    password = forms.CharField(widget = forms.PasswordInput)

    def clean_username(self):
        inst_username = self.cleaned_data.get("username")
        return inst_username

    def clean_password(self):
        inst_password = self.cleaned_data.get("password")
        return inst_password

class checkinoutForm(forms.Form):
    Choices = (('in','CheckIn'),('out','CheckOut'))
    Check_Select = forms.ChoiceField(widget = forms.RadioSelect, choices = Choices)
