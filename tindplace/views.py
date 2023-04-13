from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect

def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            if user.user_active:
                login(request, user)
                return HttpResponseRedirect('/home/')
            else:
                return render(request, 'login.html', {'error_message': 'Tu cuenta esta desactivada.'})
        else:
            return render(request, 'login.html', {'error_message': 'Correo o contraseña incorrecta.'})
    else:
        return render(request, 'login.html')

