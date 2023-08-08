from django.shortcuts import render,redirect
from socialApp.models import PostModel,CommentModel,LikeModel,SaveModel
from django.views.generic import View
from django.db.models import Q

class HomeView(View):
    def get(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            friends = request.user.friends.all()
            if friends or request.user:
                posts = PostModel.objects.filter(
                    Q(user__in = friends)|
                    Q( user = request.user)
                )
            user_comments = CommentModel.objects.filter(
                user = request.user, 
            )

            context = {
                "posts" : posts,
                "friends": friends,
                "user_comments" : user_comments,
            }
        return render(request,"home.html",context)
    
    def post(self,request,*args,**kwargs):
        choice = request.POST.get("choice")
        if request.user.is_authenticated:
            text = request.POST.get("text")
            image = request.FILES.get("image")
            video = request.FILES.get("video")


            
            if choice == "post_create":
                PostModel.objects.create(
                    user = request.user,
                    text = text,
                    image = image,
                    video = video
                )

            
            elif choice == "save_create":
                SaveModel.objects.create(
                    user = request.user,
                    post = post
                )
        
            elif choice == "comment":
                comment = request.POST.get("comment")
                post_id = request.POST.get("post_id")

                post = PostModel.objects.get(id=post_id)

                CommentModel.objects.create(
                    user = request.user,
                    post = post,
                    comment = comment,
                )    

            elif choice == "reply":
                reply = request.POST.get("reply")

                comment_id = request.POST.get("comment_id")
                comment = CommentModel.objects.get(id=comment_id)

                post_id = request.POST.get("post_id")
                post = PostModel.objects.get(id=post_id)

                CommentModel.objects.create(
                    user = request.user,
                    post = post,
                    comment = reply,
                    parent = comment
                )

            return redirect("home")
#---------------------------------------------------------------------------------
def DeleteComment(request,id):
    comment = CommentModel.objects.get(id=id)
    comment.delete()
    return redirect("home")
#---------------------------------------------------------------------------------
class MySavePost(View):
    def get(self,request,*args,**kwargs):
        if not request.user.is_authenticed:
            save_posts = SaveModel.objects.filter(
                user = request.user
            )

            context = {
                "save_posts" : save_posts
            }

            return render()
#--------------------------------------------------------------------------
def DeleteSavePost(request,id):
    save_post = SaveModel.objects.get(id=id)
    save_post.delete()
    return redirect()
#---------------------------------------------------------------------------


    