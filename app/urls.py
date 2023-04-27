from django.urls import path
from app import views

app_name = "app"   


urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("Products", views.Product, name = "Product"),
]