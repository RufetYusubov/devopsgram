from django.contrib import admin
from socialApp.models import PostModel, CommentModel, LikeModel, SaveModel

admin.site.register(PostModel)
admin.site.register(CommentModel)
admin.site.register(LikeModel)
admin.site.register(SaveModel)


