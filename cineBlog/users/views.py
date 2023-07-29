from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterUserForm
from django.contrib import messages

# Vista para el inicio de sesión
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'usted ah ingresado correctamente')
            return redirect('home') # Redirección a la página de inicio después del inicio de sesión
        else:
            messages.error(request, 'Usuario o contraseña inválido, intente de nuevo')
            return redirect('login')
    else:
        return render(request, 'user_layout/login.html', {})

# Vista para el cierre de sesión
def user_logout(request):
    logout(request)
    return redirect('login')

def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'El usuario ha sido creado correctamente')
            return redirect('home')
        else:
            messages.error(request, 'Registro inválido, intente otra vez')
    else:
        form = RegisterUserForm()  # Instantiate the form for GET requests

    return render(request, 'user_layout/register.html', {
        'form': form,
    })