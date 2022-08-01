from django.shortcuts import render

# Create your views here.

#index page
def index(request):
    return render(request,'index.html')

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
