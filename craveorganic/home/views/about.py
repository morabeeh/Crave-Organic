from django.shortcuts import render
from home.models.product import Products
from home.models.category import Category





def shop(request):
    products=Products.objects.all()
    return render(request,'shop.html',{'products':products})



#about
def about(request):
    return render(request,'about.html')

#contact
def contact(request):
    return render(request,'contact.html')

#products
def products(request):
    products = Products.objects.all()
    return render(request, 'product.html', {'products':products})
