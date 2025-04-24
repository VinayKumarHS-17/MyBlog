from django.contrib import admin
from .models import Comment,Like
# Register your models here.


class CommentAdmin(admin.ModelAdmin):
    list_display=['post','user','text','created_at']

class LikeAdmin(admin.ModelAdmin):
    list_display=['post','count']

admin.site.register(Comment,CommentAdmin)
admin.site.register(Like,LikeAdmin)