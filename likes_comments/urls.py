from django.urls import path
from . import views

urlpatterns = [
    path("add_comm/<int:id>",views.add_comment_view,name='add_comment_view'),
    path("view_comment/<int:id>",views.view_comments,name='view_comments'),
    path("del_comm/<int:id>/",views.delete_comment_view,name='delete_comment_view'),
    path("like_art/<int:id>",views.like_article_view,name='like_article_view'),
]
