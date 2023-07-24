from django.urls import path
from account import views

urlpatterns = [
    path('signup/',views.SignupView.as_view(),name="signup"),
    path('logout/',views.logoutUser,name="logout")
]