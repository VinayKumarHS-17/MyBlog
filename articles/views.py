from django.shortcuts import render,redirect
from .models import Category,Article,Author
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.


# Public Feed
# list all the articles

def article_list_views(request):
    if request.user.is_authenticated:
        articles=Article.objects.all()
        return render(request,'article_list.html',{'articles':articles})
    else:
        messages.error(request,"You must be Signup or Logged-in to view Posts.")
        return redirect('signup')
    


# list all the categories

def category_list_view(request):
    if request.user.is_authenticated:
        categories=Category.objects.all()
        return render(request,'category_list.html',{'categories':categories})
    else:
        messages.error(request,"You must be Signup or Logged-in to Categories.")
        return redirect('signup')
    


# list all the articles under a specific category
def category_post_view(request,id):
    all_cate=Category.objects.filter(id=id).first()
    if all_cate:
        list_spe_cat=Article.objects.filter(category=all_cate)
    else:
        list_spe_cat=Article.objects.none()
    return render(request,"specific_category.html",{'list_spe_cat':list_spe_cat})


# button (my blogs/my article), when clicked on this
# show only the logged-in users articles

def user_article_list_views(request,id):
    if request.user.is_authenticated:
        user_article=Article.objects.filter(user=request.user)
    else:
        messages.error(request,"User not found")
    return render(request,'user_article_list.html',{'user_article':user_article})



# Show full details of a blog post / article when clicked on it

def article_details_view(request,id):
    article_view=Article.objects.get(id=id)
    return render(request,'view_article.html',{'article_view':article_view})

# Allow only logged-in user to create a new article

def article_create_view(request):
    if not request.user.is_authenticated:
        messages.error(request,"You must be Signup or Login to create a new article.")
        return redirect('signup')
    
    if request.method=='POST':
        title=request.POST.get('title')
        content=request.POST.get('content')
        author_name=request.POST.get('author')
        category=request.POST.get('category')

        if not all([title, content, author_name, category]):
            return render(request, 'article_create.html', {
                'error': 'All fields are required.'
            })
    
        author, _= Author.objects.get_or_create(author_name=author_name)
        category, _= Category.objects.get_or_create(Category_name=category)

        Article.objects.create(title=title,content=content,author=author,category=category)
        return redirect('article_list_views')
    return render(request,'article_create.html')


# allow only logged-in user to update only his own article
# user must not be able to edit anything from other users article/blog post

def article_update_view(request,id):
    if not request.user.is_authenticated:
        return redirect("signup")
    
    article=Article.objects.get(id=id)
    if request.method=='POST':
        title=request.POST.get('title')
        content=request.POST.get('content')
        author=request.POST.get('author')
        category=request.POST.get('category')
        
        author,_=Author.objects.get_or_create(author_name=author)
        category,_=Category.objects.get_or_create(Category_name=category)

        article.title=title
        article.content=content
        article.author=author
        article.category=category
        article.save()
        return redirect('article_list_views')
    return render(request,'article_create.html',{'val':article})




# Allow user to delete the article which only belongs to them.

def article_delete_view(request,id):
    val=Article.objects.get(id=id)
    val.delete()
    return redirect("article_list_views")