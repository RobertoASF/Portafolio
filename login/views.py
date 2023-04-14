from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from .forms import LoginForm

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user_email = form.cleaned_data['user_email']
            user_password = form.cleaned_data['user_password']
            try:
                user = User.objects.get(user_email=user_email, user_password=user_password)
                if user:
                    request.session['user_id'] = user.user_id
                    messages.success(request, 'Inicio de sesión exitoso')
                    return render(request, 'home.html', {'form': form})  # Cambiar 'home' por la vista de destino después del inicio de sesión
            except User.DoesNotExist:
                messages.error(request, 'Email o contraseña incorrecta')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
