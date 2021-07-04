from django.urls import path
from django.urls.resolvers import URLPattern
from .views import about, index
# from . import views # import all views

urlpatterns = [
    path("fs/", index, name="index"),
    path("about/", about, name="about")
]
