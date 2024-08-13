from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    
    sort = request.GET.get('sort', 'id')
    
    if sort == 'id':
        order_by = 'id'
    elif sort == 'name':
        order_by = 'name'
    elif sort == 'min_price':
        order_by = 'price'
    elif sort == 'max_price':
        order_by = '-price'
        
    phones = Phone.objects.all().order_by(order_by)
    
    context = {
        'phones': phones
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {
        'phone': Phone.objects.get(slug = slug)
    }
    return render(request, template, context)
