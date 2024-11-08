from django import forms

class SignupForm(forms.Form):
    email = forms.EmailField(label='Enter your email', max_length=100)
