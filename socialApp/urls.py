from django.urls import path
from socialApp import views

urlpatterns = [
    path('home/',views.HomeView.as_view(), name="home"),
    path('delete/<int:id>/',views.DeleteComment,name="delete_comment")
]