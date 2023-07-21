from django.shortcuts import render
from socialApp.models import PostModel
from django.views.generic import View

class HomeView(View):
    def get(self,request,*args,**kwargs):
        posts = PostModel.objects.filter(
            user = request.user.friends
        )

        context = {
            "posts" : posts
        }

        return render(request,"home.html",context)
    