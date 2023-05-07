from audioop import reverse
import datetime
import uuid
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Product, User ,Admin
from .forms import AdminForm, LoginForm, RegistrationForm

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

def admin_login(request):
    if request.method == 'POST':
        form = AdminForm(request.POST)
        if form.is_valid():
            admin_email = form.cleaned_data['admin_email']
            admin_name1 = form.cleaned_data['admin_name1']
            try:
                admin = Admin.objects.get(admin_email=admin_email, admin_name1=admin_name1)
                # Si el inicio de sesión es exitoso, redirige al usuario a la vista 'dashboard'
                context = {'admin': admin}
                return render(request, 'home.html', context)
            except Admin.DoesNotExist:
                messages.error(request, 'Las credenciales ingresadas son incorrectas.')
    else:
        form = AdminForm()
    return render(request, 'admin_login.html', {'form': form})

def home(request):
    user_id = request.session.get('user_id', None)
    if user_id:
        try:
            user = User.objects.get(user_id=user_id)
            context = {'user': user}
        except User.DoesNotExist:
            context = {'message': 'No se pudo encontrar al usuario'}
    else:
        context = {'message': '¿Aún no te registras?, prueba ahora TindPlace'}

    products = Product.objects.all()
    context['products'] = products
    return render(request, 'home.html', context)



def logout(request):
    if 'user_id' in request.session:
        del request.session['user_id']
    return redirect('home')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Cree una instancia de User con los datos del formulario
            user = User(
                user_id=uuid.uuid4().hex,
                user_name1=form.cleaned_data['user_name1'],
                user_name2=form.cleaned_data['user_name2'],
                user_surname1=form.cleaned_data['user_surname1'],
                user_surname2=form.cleaned_data['user_surname2'],
                user_email=form.cleaned_data['user_email'],
                user_password=form.cleaned_data['user_password'],
                user_last_loc_lat=form.cleaned_data['user_last_loc_lat'],
                user_last_loc_long=form.cleaned_data['user_last_loc_long'],
                user_date_lastloc=form.cleaned_data['user_date_lastloc'],
                date_registred=datetime.date.today(),
                date_last_login=datetime.date.today(),
                user_score=0,
                user_phone=form.cleaned_data['user_phone'],
                user_active=True,
                user_inetrest1=form.cleaned_data['user_inetrest1'],
                user_interest2=form.cleaned_data['user_interest2'],
                user_photo=form.cleaned_data['user_photo'],
                user_sells=0,
                user_is_premium=False,
            )
            user.save()  # Guarde el usuario en la base de datos
            request.session['user_id'] = user.user_id  # Inicie la sesión del usuario
            messages.success(request, 'Registro exitoso')  # Muestre un mensaje de éxito al usuario
            return redirect('home')  # Redirigir al usuario a la vista 'home'
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})
