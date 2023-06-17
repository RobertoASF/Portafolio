from django.db.models import Q
from .forms import UserScoreForm  # Import your form at the top of the file
from django.http import HttpResponse
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
from django.db.models import Count

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
                    # Redirigir a la página de usuario inactivo
                    return redirect('inactive')
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
            admin = Admin.objects.get(
                admin_email=admin_email, admin_name1=admin_name1)

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
            messages.error(
                request, 'Las credenciales ingresadas son incorrectas.')
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


def product_detail(request, prod_id):
    product = Product.objects.get(prod_id=prod_id)
    # comments = Comment.objects.filter(product=product)
    comments = Comment.objects.filter(product=product).select_related('user')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product_id = product.prod_id
            comment.user_id = request.session.get('user_id', None)
            comment.save()

            # Devolver la respuesta en formato HTML con el nuevo comentario
            return HttpResponse('Success')

        else:
            # Devolver una respuesta de error en formato JSON
            return HttpResponse('Failure')

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

    # Ordena los productos activos por la fecha de creación de manera descendente
    products = Product.objects.filter(prod_active=True).order_by('-prod_date')

    return render(request, 'all_products.html', {'products': products, 'context': context})


def logout(request):
    if 'user_id' in request.session:
        del request.session['user_id']
    return redirect('home')


def register(request):
    form = RegistrationForm(request.POST, request.FILES or None)
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


from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string

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

    # Fetch buyer and seller users
    buyer = User.objects.get(user_id=request.session.get('user_id'))
    seller = producto.prod_seller

    # Prepare email
    message = render_to_string('email_template.html', {
        'buyer': buyer,
        'seller': seller,
        'producto': producto
    })

    send_mail(
        'Confirmación de compra',  # Subject
        '',  # Message (left empty)
        settings.EMAIL_HOST_USER,  # From Email
        [buyer.user_email],  # To Email
        html_message=message,  # HTML Message
        fail_silently=False,
    )

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


@csrf_exempt
def toggle_product_active(request):
    prod_id = request.GET.get('prod_id', None)

    if prod_id is not None:
        product = Product.objects.get(prod_id=prod_id)
        product.prod_active = not product.prod_active
        product.save()

        return JsonResponse({"success": True})

    return JsonResponse({"success": False})


def sold_products(request):
    user_id = request.session.get('user_id', None)
    if user_id is not None:
        # Obtenemos los productos vendidos por el usuario
        historical_records = Historical.objects.filter(buyer_id=user_id)
        # Filtramos los productos que fueron vendidos
        sold_products = [
            record.prod for record in historical_records if not record.prod.prod_active]
        user_reviwer = User.objects.get(user_id=request.session.get('user_id'))

        # Para cada producto vendido, verifica si el usuario ya lo ha calificado
        sold_products_rated = []
        for product in sold_products:
            user_reviwed = product.prod_seller
            previous_score = UserScore.objects.filter(
                user_reviwer=user_reviwer, user_reviwed=user_reviwed).first()
            # Agrega al producto la información de si ha sido calificado o no
            product.rated = previous_score is not None
            sold_products_rated.append(product)

        context = {'sold_products': sold_products_rated}
        return render(request, 'sold_products.html', context)
    else:
        return redirect('login')


@csrf_exempt
def rate_seller(request, seller_id):
    if request.method == "POST":
        score_value = request.POST.get('rating')
        user_reviwer = User.objects.get(user_id=request.session.get('user_id'))
        user_reviwed = str(seller_id)

        # Comprueba si el usuario ya ha calificado este producto
        previous_score = UserScore.objects.filter(
            user_reviwer=user_reviwer, user_reviwed=user_reviwed).first()

        # Si ya existe un voto, redirige al usuario y muestra un mensaje de error
        if previous_score is not None:
            messages.error(request, 'Ya has calificado este producto.')
            return redirect('sold_products')

        # Si no existe un voto, procede a crear uno
        last_score = UserScore.objects.all().order_by('-score_id').first()
        new_score_id = 1 if last_score is None else last_score.score_id + 1

        score = UserScore(score_id=new_score_id, user_reviwer=user_reviwer,
                          user_reviwed=user_reviwed, score_date=datetime.date.today(), score_value=score_value)
        score.save()

        messages.success(
            request, f'Muchas gracias por calificar a {score.user_reviwed}!')
        return redirect('sold_products')
    else:
        return JsonResponse({"success": False, "error": "Invalid request"})

def products_cards_view(request):
    # Obtén todos los productos, anota con el número de 'likes' y ordénalos en orden descendente
    products = Product.objects.annotate(likes=Count('userfavoriteproduct')).order_by('-likes')

    # Para cada producto, obtén el vendedor
    for product in products:
        product.seller = product.prod_seller

    return render(request, 'products_cards.html', {'products': products})

from django.core.mail import send_mail
from django.http import JsonResponse

def send_contact_info(request, buyer_id, seller_id):
    buyer = User.objects.get(user_id=buyer_id)
    seller = User.objects.get(user_id=seller_id)
    
    subject = "Gracias por confiar en TindPlace"
    message = f"Gracias por confiar en TindPlace. A continuación te facilitamos el contacto de tu vendedor:\nNombre: {seller.user_name1} {seller.user_surname1}\nEmail: {seller.user_email}\nTeléfono: {seller.user_phone}\nPor favor, recuerda mantener la cortesía y el respeto en tus comunicaciones."
    from_email = 'your-email@example.com'  # Replace with your email
    to_list = [buyer.user_email]
    
    try:
        send_mail(subject, message, from_email, to_list, fail_silently=False)
        return JsonResponse({"success": True, "message": "Correo enviado exitosamente."})
    except Exception as e:
        return JsonResponse({"success": False, "message": str(e)})

