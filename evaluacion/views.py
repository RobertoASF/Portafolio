from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import AppScore
from datetime import date
from django.db import IntegrityError

def evaluation(request):

    user_id = request.session.get('user_id')
    print(user_id)
    if not user_id:
        return redirect('home')  # Si no hay un usuario conectado, redirige a la página de inicio de sesión

    if request.method == 'POST':
        user_id = request.session.get('user_id')
        as_date = date.today()
        as_q1 = int(request.POST['calificacion'])
        as_q2 = int(request.POST['recomendacion'])
        as_q3 = int(request.POST['facilidad'])
        as_q4 = int(request.POST['publicacion'])
        as_q5 = int(request.POST['encontraste'])

        try:
            app_score = AppScore(user_id=user_id, as_date=as_date, as_q1=as_q1, as_q2=as_q2, as_q3=as_q3, as_q4=as_q4, as_q5=as_q5)
            app_score.save()
        except IntegrityError:
            return HttpResponse('Error: no se pudo guardar la información en la base de datos')

        return redirect('evaluation_done')

    return render(request, 'evaluation.html')


def evaluation_done(request):
    return render(request, 'evaluation_done.html')
