from django.contrib import admin
from .models import Post,Profile,comments

# Register your models here.
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(comments)
