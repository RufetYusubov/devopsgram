from django.db import models
from account.models import AccountModel

class PostModel(models.Model):
    user = models.ForeignKey(AccountModel,on_delete=models.CASCADE,related_name="user_posts")
    text = models.TextField(blank=True,null=True)
    image = models.ImageField(upload_to='posters/',blank=True,null=True)
    video = models.FileField(upload_to='videos/',blank=True,null=True)

    class Meta:
        verbose_name = "Post"

    def __str__(self) -> str:
        return self.user.first_name + " " + self.user.last_name
    
    @property
    def imageURL(self):
        if self.image:
            return self.image.url
        else:
            return 'images/placeholder.png'
    
    
class CommentModel(models.Model):
    user = models.ForeignKey(AccountModel,on_delete=models.CASCADE,related_name="user_comments")
    post = models.ForeignKey(PostModel,on_delete=models.CASCADE,related_name="post_comments",blank=True,null=True)
    parent = models.ForeignKey("self",on_delete=models.CASCADE,blank = True,null=True,related_name="replies")
    comment = models.TextField(blank=True,null=True)
    pub_date = models.DateTimeField(auto_now_add=True, blank=True,null=True)
    
    class Meta:
        verbose_name = "Comment"
        ordering = ("id",)

    def __str__(self) -> str:
        return self.user.first_name + " "+ self.user.last_name + str(self.id)
        


class LikeModel(models.Model):
    user = models.ForeignKey(AccountModel,on_delete=models.CASCADE,related_name="user_likes")
    post = models.ForeignKey(PostModel,on_delete=models.CASCADE,related_name="post_likes",blank=True,null=True)
    comment = models.ForeignKey(CommentModel,on_delete=models.CASCADE,related_name="comment_likes",blank=True,null=True)


    class Meta:
        verbose_name = "Like"

    def __str__(self) -> str:
        return self.user.first_name + " "+ self.user.last_name + str(self.id)
    



class SaveModel(models.Model):
    user = models.ForeignKey(AccountModel,on_delete=models.CASCADE,related_name="user_saves")
    post = models.ForeignKey(PostModel,on_delete=models.CASCADE,related_name="post_saves")

    class Meta:
        verbose_name = "Save"

    def __str__(self) -> str:
        return self.user.first_name + " "+self.user.last_name + str(self.id)
    


    


        
