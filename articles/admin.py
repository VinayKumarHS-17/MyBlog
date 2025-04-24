from django.contrib import admin
from .models import Category,Article,Author
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display=['Category_name']

class AuthorAdmin(admin.ModelAdmin):
    list_display=['author_name','country']

class ArticleAdmin(admin.ModelAdmin):
    list_display=['title','content','author','category','created_at']


admin.site.register(Category,CategoryAdmin)
admin.site.register(Article,ArticleAdmin)
admin.site.register(Author,AuthorAdmin)