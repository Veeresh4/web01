from django.urls import path
from app import views

app_name = "app"   

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("Products", views.Products, name="Products"),
    path("register", views.register, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name="logout"),
]