from django import forms

# Create your models here.
class LoginForm(forms.Form):
  username = forms.CharField(max_length=65)
  password = forms.CharField(max_length=65, widget=forms.PasswordInput)

  