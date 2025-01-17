from django.shortcuts import render

from store.models import Product


# Create your views here.
def index(request):
    products = Product.objects.filter(is_active=True).order_by('-id')
    context = {'products': products}
    return render(request, 'index.html', context)