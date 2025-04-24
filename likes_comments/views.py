from django.shortcuts import get_object_or_404, render, redirect
from articles.models import Article
from .models import Comment,Like
# Create your views here.

# ------------ COMMENTS ------------ #
# add a comment to a particular post
def add_comment_view(request, id):
    if request.method=='POST':
        comment_text=request.POST.get('comment')
        article=get_object_or_404(Article,id=id)
        if comment_text:
            Comment.objects.create(post=article, user=request.user, text=comment_text)
        return redirect("article_list_views")
    return render(request,'article_list.html')


# Displaying comments by user who commented on post
def view_comments(request,id):
    article = get_object_or_404(Article, id=id)
    comments = Comment.objects.filter(post=article).order_by('-created_at')
    return render(request,'view_comments.html',{'comments':comments, 'article':article})



# allow only logged in user to delete only their own comment
def delete_comment_view(request, id):
    comment=get_object_or_404(Comment,id=id)
    comment.delete()
    return redirect("article_list_views")


# ------------ LIKES ------------ #
def like_article_view(request,id):
    article = get_object_or_404(Article, id=id)
    like, created = Like.objects.get_or_create(post=article)
    like.increment()
    return redirect('article_list_views') 