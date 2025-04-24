from django.urls import path
from .views import article_create_view,article_delete_view,article_details_view,article_list_views,article_update_view, category_list_view, category_post_view, user_article_list_views

urlpatterns = [
    path("articles_list/",article_list_views,name='article_list_views'),
    path("cat_list/",category_list_view,name='category_list_view'),
    path("articles/cat_post/<int:id>",category_post_view,name='category_post_view'),
    path("user_art/",user_article_list_views,name='user_article_list_views'),
    path("art_det/<int:id>",article_details_view,name='article_details_view'),
    path("art_create/",article_create_view,name='article_create_view'),
    path("art_upd/<int:id>/",article_update_view,name='article_update_view'),
    path("art_del/<int:id>",article_delete_view,name='article_delete_view'),
]
