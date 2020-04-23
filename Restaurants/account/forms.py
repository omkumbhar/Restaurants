from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .models import Account

class AccountRegistrationForm(UserCreationForm):
    email = forms.EmailField( max_length=60,help_text="Enter email id")
    class Meta:
        model = Account
        fields =  [  "email", 'first_name', 'middle_name', 'last_name', 'phone' ,'password1', 'password2' ]



class AccountAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget= forms.PasswordInput)

    class Meta:
        model = Account
        fields =  ['email', 'password']

        def clean(self):
            if self.is_valid():
                email = self.cleaned_data['email']
                password = self.cleaned_data['password']
                if not authenticate( email = email, password =password):
                    raise forms.ValidationError("Invalid login")



class LoginForm(forms.Form):
    email = forms.EmailField(label= "Email")
    password = forms.CharField(widget=forms.PasswordInput)
