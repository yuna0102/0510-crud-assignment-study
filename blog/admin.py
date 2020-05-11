from django.contrib import admin
from .models import Post
#class Post를 models.py로 부터 import해준다

# Register your models here.

admin.site.register(Post)
#register해준다는 것은 class Post --> Blog.Post 'admin/' 페이지에 보여주게 됨