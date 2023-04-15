from audioop import reverse
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
                    return redirect('home')  # Redirige al usuario a la vista 'home' después del inicio de sesión
            except User.DoesNotExist:
                messages.error(request, 'Email o contraseña incorrecta')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def home(request):
    user_id = request.session.get('user_id', None)
    if user_id:
        user = User.objects.get(user_id=user_id)
        context = {'user': user}
        return render(request, 'home.html', context)
    else:
        # redirige al usuario a la página de inicio de sesión si no ha iniciado sesión
        return redirect('login')  

