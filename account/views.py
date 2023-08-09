from django.shortcuts import render,redirect
from account.models import AccountModel,ProfileAboutModel
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.http import Http404

        

def check_password(password):
    if len(password)>=8:
        return True
    return False

def check_validation(password):
    has_digit, has_upper_case, has_lower_case, has_symbol = False,False,False,False

    for i in password:
        if i.isdigit():
            has_digit = True
        elif i.isalpha() and i.isupper():
            has_upper_case = True
        elif i.isalpha() and i.islower():
            has_lower_case = True
        else:
            has_symbol = True

    return has_digit and has_upper_case and has_lower_case and has_symbol
    
class SignupView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"signup.html")
    
    def post(self,request,*args,**kwargs):
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        email = request.POST.get("email")
        password = request.POST.get("password")
        birthday = request.POST.get("birthday")
        gender = request.POST.get("gender")

        
        if not AccountModel.objects.filter(email = email).exists():
                if not check_password(password):
                        messages.info(request,"Password must be at least 8 symbols")
                        return redirect("signup")
                elif not check_validation(password):
                        messages.info(request,"Password must contain both characters and number")
                        return redirect("signup")
                else:
                        AccountModel.objects.create_user(
                            first_name = firstname,
                            last_name = lastname,
                            email = email,
                            password = password,
                            birthday = birthday,
                            gender = gender,
                        )                   
                user = authenticate(request,email=email,password=password)
                if user is not None:
                    login(request,user)
                    return redirect("home")
        else:
                    messages.info(request,"Email has been taken")
                    return redirect("signup")
        return render(request,'signup.html')
    
class LoginUserView(View):
     def get(self,request,*args,**kwargs):
          return render(request,"login.html")
     def post(self,request,*args,**kwargs):
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, email = email, password = password)
        if user is not None:
            login(request,user)
            messages.success(request,"You logged in")
            return redirect("home")
        else:
                if not AccountModel.objects.filter(email = email).exists():
                      messages.info(request,"Please enter correct email")
                else:
                     messages.info(request,"Please, enter correct password")
                return redirect("login")
#----------------------------------------------------------------------------------------------
def logoutUser(request):
    logout(request)
    return redirect("signup")
#--------------------------------------------------------------------------------------------
class Changepassword(View):
     def get(self,request,*args,**kwargs):
          
          return render(request,"changepassword.html")
     def post(self,request,*args,**kwargs):
        if request.user.is_authenticated:
              raise Http404
        email = request.POST.get("email")
        newpassword1 = request.POST.get("newpassword1")
        newpassword2 = request.POST.get("newpassword2")

        user = AccountModel.objects.get(email = email)
        if newpassword1 == newpassword2 and check_password(newpassword1) and check_validation(newpassword1):
                user.set_password(newpassword1)
                user.save()
                messages.success(request, "Password changed")
                return redirect("login")
        else:
            if newpassword1 != newpassword2:
                messages.info(request, "There is a password mismatch")
            elif not check_password(newpassword1):
                messages.info(request, "Password must be at least 8 symbols")
            elif not check_validation(newpassword1):
                messages.info(request, "Password must contain both characters and numbers")
            return redirect("changepassword")
#---------------------------------------------------------------------------------------
class SettingsView(View):
     def get(self,request,*args,**kwargs):
          
          return render(request,"settings.html")
     
     def post(self,request,*args,**kwargs):
        if not request.user.is_authenticated:
               raise Http404
         
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        email = request.POST.get("email")
        avatar = request.FILES.get("avatar")
        birtday = request.POST.get("birtday")
        work_at = request.POST.get("work_at")
        live_in = request.POST.get("live_in")
        gender = request.POST.get("gender")
        oldpassword = request.POST.get("oldpassword")
        newpassword = request.POST.get("newpassword")

        if firstname:
              request.user.first_name = firstname
              request.user.save()
        if lastname:
             request.user.last_name = lastname
             request.user.save()
        if not AccountModel.objects.filter(email=email).exists():
             request.user.email = email
             request.user.save()
        if avatar:
             request.user.avatar = avatar
             request.user.save()
        if birtday:
             request.user.birthday = birtday
             request.user.save()
        if work_at:
             request.user.work_at = work_at
             request.user.save()
        if live_in:
             request.user.live_in = live_in
             request.user.save()
        if gender:
             request.user.gender = gender
             request.user.save()
        if oldpassword and newpassword:
            if request.user.check_password(oldpassword):
                if not check_password(newpassword):
                       messages.info(request,"Password must be at least 8 symbols")
                elif not check_validation(newpassword):
                    messages.info(request, "Password must contain both characters and numbers")
                else:
                    request.user.set_password(newpassword)
                    request.user.save()
            else:
                messages.info(request, "Please enter correct oldpassword")
                return redirect("settings")
        return render(request,"settings.html")
          
          


                


             



