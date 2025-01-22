from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm, SetPasswordForm, PasswordResetForm
from django.contrib.auth.models import User
from . models import DIVISION_CHOICES

class LoginForm(AuthenticationForm):
    username = UsernameField(widget = forms.TextInput(attrs = {'autofocus' : 'true', 'class':'form-control'}))
    password = forms.CharField(widget= forms.PasswordInput(attrs = {'autocomplete' : 'current-password', 'class':'form-control'}))

class CustomerRegistrationForm(UserCreationForm):
    username = forms.CharField(widget= forms.TextInput(attrs = {'autofocus' : 'true', 'class':'form-control'}))
    email = forms.EmailField(widget= forms.EmailInput(attrs = {'class':'form-control'}))
    password1 = forms.CharField(label='Password', widget= forms.PasswordInput(attrs = {'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget= forms.PasswordInput(attrs = {'class':'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2'] 


class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Old Password', widget= forms.PasswordInput(attrs = {'autofocus' : 'true','autocomplete' : 'current-password','class':'form-control'}))
    new_password1 = forms.CharField(label='New Password', widget= forms.PasswordInput(attrs = {'autocomplete' : 'current-password','class':'form-control'}))
    new_password2 = forms.CharField(label='Confirm New Password', widget= forms.PasswordInput(attrs = {'autocomplete' : 'current-password','class':'form-control'}))

class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(widget = forms.EmailInput(attrs = {'class' : 'form-control'}))

class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(attrs = {'autocomplete' : 'current-password','class':'form-control'}))
    new_password2 = forms.CharField(label='Confirm New Password', widget=forms.PasswordInput(attrs = {'autocomplete' : 'current-password','class':'form-control'}))


class CustomerProfileForm(forms.ModelForm):
    name = forms.CharField(label='Name', widget= forms.TextInput(attrs = {'autofocus' : 'true', 'class':'form-control'}))
    city = forms.CharField(label='City', widget= forms.TextInput(attrs = {'autofocus' : 'true', 'class':'form-control'}))
    address = forms.CharField(label='address', widget= forms.TextInput(attrs = {'autofocus' : 'true', 'class':'form-control'}))
    division = forms.ChoiceField(label='division', choices=DIVISION_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    zipcode = forms.IntegerField(label='Zipcode', widget= forms.NumberInput(attrs = {'class':'form-control'}))
    mobile = forms.IntegerField(label='Mobile', widget= forms.NumberInput(attrs = {'class':'form-control'}))

    class Meta:
        model = User  # Replace with the actual model name
        fields = ['name', 'city', 'address', 'division', 'zipcode', 'mobile']