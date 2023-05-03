from pyexpat.errors import messages
from django.shortcuts import redirect, render
from login.models import User

from .forms import ProductForm
from login.models import Product


def create_product(request):
    user_id = request.session.get('user_id')
    print(user_id)
    if not user_id:
        return redirect('login')  # Si no hay un usuario conectado, redirige a la página de inicio de sesión
    user = User.objects.get(user_id=user_id)
    print(user)
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.prod_id = 1;
            product.prod_seller = user
            product.save()
            return redirect('home')
    else:
        form = ProductForm()

    return render(request, 'create_product.html', {'form': form})


