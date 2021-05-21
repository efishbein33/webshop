from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse, JsonResponse
import requests
from django.db.models import Q



def products(request):
    ''' display all products on products page '''
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products.html', context)


def product_detail(request, id):
    ''' detailed product page  '''
    products = Product.objects.filter(id=id)
    context = {'data': products}
    return render(request, 'detail/product-detail.html', context)


def add_to_cart(request):
    ''' Using django session's to add items to shopping cart '''
    product_id = request.GET['product_id']
    cart = [product_id]

    if 'cartdata' in request.session:
        cart_data=request.session['cartdata']
        cart_data.append(cart)
        request.session['cartdata']=cart_data
    else:
        request.session['cartdata']=cart
    return JsonResponse({'data':request.session['cartdata'],'totalitems':len(request.session['cartdata'])})



def search(request):
    ''' handle the search bar for both name and product code '''
    q=request.GET['q']
    data=Product.objects.filter(Q(name__icontains=q) | Q(code__icontains=q))
    return render(request, 'search.html', {'data': data})
