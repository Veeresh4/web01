from django.shortcuts import render, redirect
from app.models import Product
from django.core.paginator import Paginator
from app.forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.
def homepage(request):
    product=Product.objects.all()
    return render(request, 'home.html', context={'product':product})


def Products(request):
    products = Product.objects.all()
    paginator = Paginator(products, 18)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render (request, "products.html")


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("main:homepage")
        messages.error(request, "Unsuccessful registration. Invalid information.")  
    form = NewUserForm
    return render(request, 'register.html', context={"form":form})


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("main:homepage")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request, "login.html", context={"form":form})


def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("app:homepage")