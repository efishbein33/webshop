from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse, JsonResponse
import requests
from django.db.models import Q
from django.template.loader import render_to_string



def products(request):
    ''' display all products on products page '''
    if request.GET.get('name'):
        pass
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products.html', context)


def product_detail(request, id):
    ''' detailed description of product '''
    products = Product.objects.filter(id=id)
    context = {'data': products}
    return render(request, 'detail/product-detail.html', context)


def add_to_cart(request):
    print(request.GET.get('id'))
    cart={}
    cart[str(request.GET['id'])]={
        'price': request.GET['price'],
        'qty': request.GET['qty'],
    }
    if 'cart' in request.session:
        if str(request.GET['id']) in request.session['cart']:
            cart_data=request.session['cart']
            cart_data[str(request.GET['id'])]['qty']=int(cart[str(request.GET['id'])]['qty'])
            cart_data.update(cart_data)
            request.session['cart']=cart_data
        else:
            cart_data=request.session['cart']
            cart_data.update(cart)
            request.session['cart']=cart_data
    else:
        request.session['cart']=cart
    return JsonResponse({'data':request.session['cart'],'totalitems':len(request.session['cart'])})



def search(request):
    q=request.GET['q']
    data=Product.objects.filter(Q(name__icontains=q) | Q(code__icontains=q))
    return render(request, 'search.html', {'data': data})

