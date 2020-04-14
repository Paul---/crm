from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home_page(req):
    return render(req, 'accounts/dashboard.html')

def customer_page(req):
    return render(req, 'accounts/customer.html')

def products_page(req):
    return render(req, 'accounts/products.html')
