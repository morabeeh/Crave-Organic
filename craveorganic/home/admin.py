from django.contrib import admin
from .models.category import Category
from .models.customer import Customer
from .models.product import Products
from .models.orders import Order



# Register your models here.
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Products)
admin.site.register(Order)

