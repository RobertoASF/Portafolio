from django.db.models import Max
from django.views.decorators.csrf import csrf_exempt
from audioop import reverse
import datetime
import uuid
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Historical, Product, User, Admin, UserFavoriteProduct, Comment, UserScore
from .forms import AdminForm, LoginForm, RegistrationForm, CommentForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user_email = form.cleaned_data['user_email']
            user_password = form.cleaned_data['user_password']
            try:
                user = User.objects.get(
                    user_email=user_email, user_password=user_password)
                if user.user_active:   # Comprobar si el usuario está activo
                    request.session['user_id'] = user.user_id
                    # Redirige al usuario a la vista 'home' después del inicio de sesión
                    return redirect('home')
                else:  # Si el usuario no está activo
                    return redirect('inactive')   # Redirigir a la página de usuario inactivo
            except User.DoesNotExist:
                messages.error(request, 'Email o contraseña incorrecta')
    else:
        form = LoginForm()
    # Añade la variable 'hide_footer' a tu contexto
    context = {'form': form, 'hide_footer': True}
    return render(request, 'login.html', context)



def admin_login(request):
    form = AdminForm(request.POST or None)
    if form.is_valid():
        admin_email = form.cleaned_data['admin_email']
        admin_name1 = form.cleaned_data['admin_name1']
        try:
            admin = Admin.objects.get(admin_email=admin_email, admin_name1=admin_name1)

            # Get historical data
            historical_data = Historical.objects.all()
            # Get product data
            product_data = Product.objects.all()
            # Get user data
            user_data = User.objects.all()

            # Get user score data
            user_score_data = UserScore.objects.all()

            context = {
                'admin': admin, 
                'hide_footer': True, 
                'historical_data': historical_data, 
                'product_data': product_data, 
                'user_data': user_data,
                'user_score_data': user_score_data
            }
            return render(request, 'home-admin.html', context)
        except Admin.DoesNotExist:
            messages.error(request, 'Las credenciales ingresadas son incorrectas.')
    context = {'form': form, 'hide_footer': True}
    return render(request, 'admin_login.html', context)



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
        # Filtra productos que coinciden con los intereses del usuario y están activos
        products_interest1 = Product.objects.filter(
            prod_affinitie1=user.user_inetrest1, prod_active=True)
        products_interest2 = Product.objects.filter(
            prod_affinitie2=user.user_interest2, prod_active=True)
        # Combina los dos QuerySets
        products = products_interest1 | products_interest2
    else:
        # Filtra productos que están activos
        products = Product.objects.filter(prod_active=True)

    context['products'] = products
    return render(request, 'home.html', context)


# traer el cometario y guarlo en la base de datos
def product_detail(request, prod_id):
    product = Product.objects.get(prod_id=prod_id)
    comments = Comment.objects.filter(product=product)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product_id = product.prod_id
            comment.user_id = request.session.get('user_id', None)
            comment.save()

            # Devolver la respuesta en formato JSON con el HTML del nuevo comentario
            return JsonResponse({'success': True, 'html': comment.text})

        else:
            # Devolver una respuesta de error en formato JSON
            return JsonResponse({'success': False})

    else:
        form = CommentForm()

    return render(request, 'product_detail.html', {'product': product, 'comments': comments, 'form': form})


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

    return render(request, 'all_products.html', {'products': products, 'context': context})


def logout(request):
    if 'user_id' in request.session:
        del request.session['user_id']
    return redirect('home')

def register(request):
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        user = User(
            user_id=form.cleaned_data['user_id'],
            user_name1=form.cleaned_data['user_name1'],
            user_name2=form.cleaned_data['user_name2'],
            user_surname1=form.cleaned_data['user_surname1'],
            user_surname2=form.cleaned_data['user_surname2'],
            user_email=form.cleaned_data['user_email'],
            user_password=form.cleaned_data['user_password'],
            user_last_loc_lat=1,
            user_last_loc_long=1,
            user_date_lastloc=datetime.date.today(),
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
        user.save()  
        request.session['user_id'] = user.user_id
        messages.success(request, 'Registro exitoso')
        return redirect('home')
    context = {'form': form, 'hide_footer': True}
    return render(request, 'register.html', context)



def enviar_correo(request):
    if request.method == 'POST':
        subject = 'Asunto de Prueba'
        mail_html_path = os.path.join('login', 'templates', 'mail.html')
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
    return render(request, 'home.html', {'hide_footer': True})


def weather(request):
    return render(request, 'weather.html', {'hide_footer': True})


def error_404_view(request, exception):
    return render(request, '404.html', status=404)

# ver megusta


def favorites(request):
    user = get_object_or_404(User, user_id=request.session.get('user_id'))

    favorites = UserFavoriteProduct.objects.filter(user=user)

    context = {'favorites': favorites}
    return render(request, 'favorites.html', context)


@csrf_exempt
def like_product(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, prod_id=product_id)
        user = get_object_or_404(User, user_id=request.session.get('user_id'))

        UserFavoriteProduct.objects.get_or_create(user=user, product=product)

        return JsonResponse({"message": "Producto añadido a favoritos"})
    else:
        return JsonResponse({"error": "Invalid method"})


def comprar_producto(request, prod_id):
    producto = get_object_or_404(Product, prod_id=prod_id)

    producto.prod_active = False
    producto.save()

    # Get the maximum hist_id currently in the model
    max_id = Historical.objects.all().aggregate(
        max_id=Max('hist_id'))['max_id']

    # If no instances exist yet, start from 1, otherwise increment the maximum by 1
    hist_id = 1 if max_id is None else max_id + 1

    historical_entry = Historical(
        hist_id=hist_id,
        date=datetime.date.today(),
        buyer_id=request.session.get('user_id', None),
        prod=producto
    )
    historical_entry.save()

    return redirect('pagina_de_confirmacion')



def pagina_de_confirmacion(request):
    return render(request, 'confirmacion.html', {'hide_footer': True})

@csrf_exempt
def toggle_user_active(request):
    if request.method == "POST":
        user_id = request.POST.get('user_id')
        try:
            user = User.objects.get(user_id=user_id)
            user.user_active = not user.user_active
            user.save()
            return JsonResponse({"success": True})
        except User.DoesNotExist:
            return JsonResponse({"success": False, "error": "User does not exist"})
    else:
        return JsonResponse({"success": False, "error": "Invalid request"})
    
def inactive(request):
    return render(request, 'inactive.html')
