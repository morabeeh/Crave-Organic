from django.shortcuts import render
from home.models import Products

from home.models import Customer

#from home.models import Products

# Create your views here.

#index page
def index(request):
    products = Products.objects.all()
    return render(request,'index.html', {'products':products})

#shop page
def shop(request):
    return render(request,'shop.html')

#about page
def about(request):
    return render(request,'about.html')

#contact page
def contact(request):
    return render(request,'contact.html')

#wishlist page
def wishlist(request):
    return render(request,'wishlist.html')

#cart page
def cart(request):
    return render(request,'cart.html')
    
#single product page
def product(request):
    return render(request,'product.html')

def customer(request):
    customer = Customer.objects.all()
    return render(request,'customer.html',{'customer':customer})

#products
def products(request):
    products = Products.objects.all()
    return render(request, 'products.html', {'products':products})
