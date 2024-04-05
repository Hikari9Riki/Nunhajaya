from django.shortcuts import render,redirect
from .models import Product
from django_mobileesp import mdetect

# Create your views here.


def catalog(request):
   
    user_agent = request.META.get('HTTP_USER_AGENT', '')
    http_accept = request.META.get('HTTP_ACCEPT', '')

    agent = mdetect.UAgentInfo(user_agent, http_accept)

    if agent.detectMobileQuick():
        request.session['extend'] = 'base mobile.html'
    else:
        # User is accessing from a computer
        request.session['extend'] = 'base pc.html'
    
    template = request.session.get('extend')
    one_products = Product.objects.filter(category=0)
    second_products = Product.objects.filter(category=1)
    third_products = Product.objects.filter(category=2)
    forth_products = Product.objects.filter(category=3)
    fifth_products = Product.objects.filter(category=4)
    context = {
        'one_products': one_products,
        'second_products': second_products,
        'third_products': third_products,
        'forth_products': forth_products,
        'fifth_products': fifth_products,
        'template': template
    }
    return render(request, "catalog.html", context)

'''
def category(request, category_id):
    try:
        products = Product.objects.filter(category=category_id)
    except Product.DoesNotExist:
        products = None
    
    template = request.session.get('extend')
    context = {
        'products': products,
        'template': template
    }
    return render(request, "catalog.html", context)
'''

def category(request, category_id):


    request.session['product'] = category_id
    return redirect('catalog')

def Cuba(request):
    return render(request,"try.html")

def gpt(request):
    return render(request,"gpt.html")

def eco(request):
    return render(request,"eco.html")
