from audioop import reverse
import datetime
import uuid
from django.shortcuts import render, redirect , get_object_or_404
from django.contrib import messages
from .models import Product, User ,Admin, UserFavoriteProduct
from .forms import AdminForm, LoginForm, RegistrationForm
from django.http import JsonResponse


#aca agregamos el product details
def product_detail(request):
    prod_id = request.GET.get('prod_id')
    product = Product.objects.get(prod_id=prod_id)
    return render(request, 'product_detail.html', {'product': product})


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
    user = None
    if user_id:
        try:
            # todos los datos del usuario
            user = User.objects.get(user_id=user_id)
            context = {'user': user}
        except User.DoesNotExist:
            context = {'message': 'No se pudo encontrar al usuario'}
    else:
        context = {'message': '¿Aún no te registras?, prueba ahora TindPlace'}

    if user:
        # Filtra productos que coinciden con los intereses del usuario
        products_interest1 = Product.objects.filter(prod_affinitie1=user.user_inetrest1)
        products_interest2 = Product.objects.filter(prod_affinitie2=user.user_interest2)

        # Combina los dos QuerySets
        products = products_interest1 | products_interest2
    else:
        products = Product.objects.all()

    context['products'] = products
    return render(request, 'home.html', context)


def all_products(request):
    user_id = request.session.get('user_id', None)
    user = None
    if user_id:
        try:
            # todos los datos del usuario
            user = User.objects.get(user_id=user_id)
            context = {'user': user}
        except User.DoesNotExist:
            context = {'message': 'No se pudo encontrar al usuario'}
    else:
        context = {'message': '¿Aún no te registras?, prueba ahora TindPlace'}

    # Ordena los productos por la fecha de creación de manera descendente
    products = Product.objects.all().order_by('-prod_date')
    return render(request, 'all_products.html', {'products': products})


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
                user_id= form.cleaned_data['user_id'],
                user_name1=form.cleaned_data['user_name1'],
                user_name2=form.cleaned_data['user_name2'],
                user_surname1=form.cleaned_data['user_surname1'],
                user_surname2=form.cleaned_data['user_surname2'],
                user_email=form.cleaned_data['user_email'],
                user_password=form.cleaned_data['user_password'],
                user_last_loc_lat= 1,
                user_last_loc_long=1,
                user_date_lastloc=  datetime.date.today(),
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


def enviar_correo(request):
    if request.method == 'POST':
        subject = 'Asunto de Prueba'
        mail_html_path = os.path.join('login','templates', 'mail.html')
        with open(mail_html_path, 'r') as f:
            mail_html_content = f.read()
        message = render_to_string('mail.html', {'content': mail_html_content})
        # Sustituir la variable "{{ mensaje }}" en el contenido del correo
        mensaje = request.POST.get('message1', '')
        mail_html_content = mail_html_content.replace("{{ mensaje }}", mensaje)
        sender_email = 'rob.sanchez@duocuc.cl'
        recipient_list = ['rob.sanchez@duocuc.cl', 'roberto.asf@gmail.com']
        
        sg = sendgrid.SendGridAPIClient(api_key=settings.EMAIL_HOST_PASSWORD)
        mail = Mail(
            from_email=sender_email,
            to_emails=recipient_list,
            subject=subject,
            html_content=message)
        response = sg.send(mail)
        print(response.status_code)
    return render(request, 'home.html') 

def weather(request):
    return render(request, 'weather.html')


def error_404_view(request, exception):
    return render(request, '404.html', status=404)

#me gusta 
def like_product(request, product_id):
    product = get_object_or_404(Product, prod_id=product_id)
    user = get_object_or_404(User, user_id=request.session.get('user_id'))
    
    UserFavoriteProduct.objects.get_or_create(user=user, product=product)
    
    # Añade un mensaje a la cola de mensajes
    messages.success(request, "Producto añadido a favoritos")

    # Redirige al usuario a la página de inicio
    return redirect('home')

#ver megusta
def favorites(request):
    user = get_object_or_404(User, user_id=request.session.get('user_id'))
    
    favorites = UserFavoriteProduct.objects.filter(user=user)

    context = {'favorites': favorites}
    return render(request, 'favorites.html', context)
