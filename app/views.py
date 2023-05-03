from django.shortcuts import render, redirect
from app.models import Product
from django.core.paginator import Paginator
from app.forms import NewUserForm, UserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.
def homepage(request):
    # if request.method == "POST":
	# 	product_id = request.POST.get('product_pk')
	# 	product = Product.objects.get(id = product_id)
	# 	request.user.profile.products.add(product)
	# 	messages.success(request,(f'{product} added to wishlist.'))
	# 	return redirect ('app:homepage')
    product=Product.objects.all()
    return render(request, 'home.html', context={'product':product})


def Products(request):
    # if request.method == "POST":
	# 	product_id = request.POST.get("product_pk")
	# 	product = Product.objects.get(id = product_id)
	# 	request.user.profile.products.add(product)
	# 	messages.success(request,(f'{product} added to wishlist.'))
	# 	return redirect ('app:products')
    products = Product.objects.all()
    paginator = Paginator(products, 18)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render (request, "products.html", context = { "page_obj":page_obj})


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("app:homepage")
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
				return redirect("app:homepage")
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


def userpage(request):
	if request.method == "POST":
		user_form = UserForm(request.POST, instance=request.user)
		if user_form.is_valid():
		    user_form.save()
		    messages.success(request,('Your profile was successfully updated!'))
		else:
		    messages.error(request,('Unable to complete request'))
		return redirect ("app:userpage")
	user_form = UserForm(instance=request.user)
	return render(request, "user.html", context = {"user":request.user, "user_form": user_form})