from django.urls import path
from account import views

urlpatterns = [
    path('signup/',views.SignupView.as_view(),name="signup"),
    path('login/',views.LoginUserView.as_view(),name="login"),
    path('logout/',views.logoutUser,name="logout"),
    path('changepassword/',views.Changepassword.as_view(),name="changepassword"),
    path('settings/',views.SettingsView.as_view(),name="settings")
]