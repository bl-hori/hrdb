from django.urls import path

from . import views

name = "base"

urlpatterns = [path("", views.home, name="home")]
