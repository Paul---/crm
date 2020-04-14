from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home_page(req):
    return HttpResponse('Home Page')

def customer_page(req):
    return HttpResponse('Customer Page')

def products_page(req):
    return HttpResponse('<h1>Products Page</h1>')
