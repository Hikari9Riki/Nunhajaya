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
    if 'product' in request.session:
        try:
            products = Product.objects.filter(category=request.session.get('product'))
        except Product.DoesNotExist:
            products = None
        template = request.session.get('extend')
        context = {
        'products': products,
        'template': template
        }
        return render(request, "catalog.html", context)
    else:
        template = request.session.get('extend')
        products = Product.objects.all()
        context = {
            'products': products,
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