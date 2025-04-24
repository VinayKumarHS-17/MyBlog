from django.shortcuts import render, redirect,get_object_or_404
from .models import Profile
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required
# Create your views here.

# to view a particular user profile (similar to insta:no of blog posts/articles, total number of likes overall, user bio, picture, list all the blogs posted)

def view_profile(request):
    try:
        profile_info = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile_info = Profile.objects.create(user=request.user)
    return render(request,'user_profile.html',{'profile_info':profile_info})


# user should be able to edit only his own profile, not other users profile
# can edit bio and profile picture only
def edit_profile(request,id):
    profile = Profile.objects.get(id=id)
    if request.method=='POST':
        form = ProfileForm(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            form.save()
            return redirect('view_profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request,"edit_profile.html",{'form':form})
        



# Optional...
'''
# user should be able to delete only his own profile, not other users profile
# make sure to give a confirmation message ....
# as all the posts will be connected to the user..
'''

def delete_profile(request, id):
    try:
        profile = Profile.objects.get(id=id)
    except Profile.DoesNotExist:
        return redirect('view_profile')
    
    if request.user.is_superuser or request.user == profile.user:
        if request.method=='POST':
            profile.delete()
            return redirect('view_profile')
        else:
            return render(request,'confirm_del.html',{'profile':profile})
    else:
        return redirect('view_profile')
    

