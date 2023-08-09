from django.urls import path
from socialApp import views

urlpatterns = [
    path('home/<int:id>/',views.HomeView.as_view(), name="home")
]