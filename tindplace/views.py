from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def product_detail(request):
    prod_id = request.GET.get('prod_id')
    product = Product.objects.get(prod_id=prod_id)
    return render(request, 'product_detail.html', {'product': product})
