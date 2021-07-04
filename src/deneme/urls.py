from django.urls import path
from .views import deneme

urlpatterns = [
    path("home", deneme, name="deneme"),
]
