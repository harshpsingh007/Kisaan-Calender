from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('pricing/',views.contact,name='pricing'),
    path("handlerequest/", views.handlerequest, name="HandleRequest"),
]