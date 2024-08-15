from django.shortcuts import render
from . models import Product
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    return render(request,'index.html')

def product_list(request):
    page=1
    if request.GET:
        page=request.GET.get('page',1)
    list=Product.objects.all()
    product_paginator=Paginator(list,2)
    list=product_paginator.get_page(page)
    context={'products':list}
    return render(request,'products.html',context)   

def product_details(request):
    return render(request,'product_details.html')