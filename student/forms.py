from django import forms
from django.contrib.auth.models import User

from .models import UserProfile

# Creates a User with usermane, email address, and password
class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=50, help_text="Please enter a username.")
    email = forms.CharField(help_text="Please enter your email.")
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(), help_text="Please enter a password.")
    password2 = forms.CharField(max_length=50, widget=forms.PasswordInput(), help_text="Repeat your password")
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')
    
    def clean_password(self):
        if self.data['password'] != self.data['password2']:
            raise forms.ValidationError('Passwords are not the same')
        return self.data['password']


# Creates a profile for the User with first name, last name, and TUid.
# This profile information is used when generating a Word Document to
# submit for an official Lab Report which is turned in to the TA.
class UserProfileForm(forms.ModelForm):    
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'TUid' ]
    
    