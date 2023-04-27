from django.shortcuts import render
from app.models import Product


# Create your views here.
def homepage(request):
    product=Product.objects.all()[:4]
    return render(request, 'home.html', context={'product':product})