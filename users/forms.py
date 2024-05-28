from django import forms
from .models import Student

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        min_length=4,
        widget=forms.TextInput({"class": "form-control"})
    )
    password = forms.CharField(widget=forms.PasswordInput({"class": "form-control"}))

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100,min_length=4,
        widget=forms.TextInput({"class": "form-control"}))
    
    first_name = forms.CharField(max_length=100,min_length=4,
        widget=forms.TextInput({"class": "form-control"}))

    last_name = forms.CharField(max_length=100,min_length=4,
        widget=forms.TextInput({"class": "form-control"}))
    
    email = forms.CharField(max_length=100,min_length=4,
        widget=forms.EmailInput({"class": "form-control"}))


    password = forms.CharField(widget=forms.PasswordInput({"class": "form-control"}))

    confirm_password = forms.CharField(widget=forms.PasswordInput({"class": "form-control"}))

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'last_name', 'email', 'location', 'phone', 'hobby', 'image']