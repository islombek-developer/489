from django.shortcuts import render, redirect,get_object_or_404
from django.views import View
from .models import Student,Hobby
from .forms import LoginForm, RegisterForm,StudentForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Student

class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'users/login.html', context={"form": form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/') 
        return render(request, 'users/login.html', context={"form": form})

class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'users/register.html', context={"form": form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']

            if password == confirm_password:
                user = User(
                    username=username,
                    first_name=first_name,
                    last_name=last_name,
                    email=email
                )
                user.set_password(password)
                user.save()
                return redirect('/login-page')  
        return render(request, 'users/register.html', context={"form": form})


def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = StudentForm()
    return render(request, 'users/form.html', context={'form': form})

def student_update(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('/profil')
    else:
        form = StudentForm(instance=student)
    return render(request, 'users/form.html', context={'form': form})


def prfil(request):
    student=Student.objects.all()
    return render(request, 'users/profil.html',context={"student":student})

def read(request,id):
    student=Student.objects.get(id=id)
    return render(request, 'users/table.html',context={"student":student})



def delete(request, id):
    data = get_object_or_404(Student, id=id)
    data.delete()
    return redirect("/profil")
