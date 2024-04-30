from django import forms


class SignupForm(forms.Form):
    username = forms.CharField(max_length=5)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    c_password = forms.CharField(widget=forms.PasswordInput, label="Confirm password")


class LoginForm(forms.Form):
    username = forms.CharField(max_length=5)
    password = forms.CharField(widget=forms.PasswordInput)
