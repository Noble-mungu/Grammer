from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import NewPostForm, CreateProfileForm, EditProfile, WriteComment
from .models import Post,User, Profile,comments


# Create your views here.

@login_required(login_url='/accounts/login/')
def index(request):    
    commenters = comments.get_comments()
    current_user = request.user
    profile = Profile.open_profile(current_user) 
    posts = Post.get_posts()    
    is_liked = False          
    for post in posts:            
        if post.likes.filter(id = request.user.id).exists():
            is_liked = True        
            return render(request, 'index.html', {"posts": posts,"current_user": current_user, "profile": profile, "commenters": commenters, "is_liked": is_liked })

        else:
            return render(request, 'index.html', {"posts": posts,"current_user": current_user, "profile": profile, "commenters": commenters, "is_liked": is_liked })

#create a post
@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    profile = Profile.open_profile(current_user) 
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user    
            post.profiles = profile                                
            post.save()
        return redirect('home')
    else:
        form = NewPostForm()
    return render(request, 'new_post.html', {"form":form})


#view post details
@login_required(login_url='/accounts/login/')
def view_post(request, id):
    current_user = request.user
    profile = Profile.open_profile(current_user.id)
    commentss = comments.get_post_comment(id)
    post = Post.get_post_details(id)
    is_liked = False     
    if post.likes.filter(id = request.user.id).exists():
        is_liked = True    
        
    if request.method == 'POST':        
        commentform = WriteComment(request.POST, request.FILES)                
        if commentform.is_valid():
            comment = commentform.save(commit=False)            
            comment.profile = profile
            comment.post = post
            comment.save()                            
        return HttpResponseRedirect(reverse('detail', args=[str(id)]))        

    else:
        commentform = WriteComment()

    return render(request, 'detail.html', {"current_user": current_user,"post":post, "profile": profile ,"commentss": commentss, "is_liked": is_liked,"commentform":commentform })


#like function
def likeview(request, id):
    post= get_object_or_404(Post, id=request.POST.get('post_id'))
    is_liked = False
    if post.likes.filter(id = request.user.id).exists():
        post.likes.remove(request.user)
        is_liked = False
    else:        
        post.likes.add(request.user)
        is_liked = True
    return redirect('home')


#view function to create user profile
@login_required(login_url='/accounts/login/')
def create_profile(request):        
    current_user = request.user
    if request.method == 'POST':
        createform = CreateProfileForm(request.POST, request.FILES)
        if editform.is_valid():
            profile = createform.save(commit=False)
            profile.user =  current_user
            profile.save()
        return redirect('home')
    else:
        createform = CreateProfileForm()
    return render(request, 'create-profile.html', {"createform": createform})

#view your profile
def profile(request, id):
    current_user = request.user
    profile = Profile.open_profile(id)
    posts = Post.get_posts() 
    feeds = Post.get_feed(id)
    return render(request, 'profile.html', {"profile": profile ,"current_user": current_user, "feeds": feeds, "posts": posts}) 

#view other profile
def profilevisit(request, id):
    current_user = request.user
    profile = Profile.open_profile(id)
    feeds = Post.get_feed(id)    
    is_followed = False
    if profile.followers.filter(id = current_user.id).exists():
        is_followed = True
        return render(request, 'visit-profile.html', {"profile": profile ,"current_user": current_user ,"feeds": feeds, "is_followed": is_followed})
    else:
        return render(request, 'visit-profile.html', {"profile": profile ,"current_user": current_user ,"feeds": feeds, "is_followed": is_followed}) 

#function to edit user profile and bio
@login_required(login_url='/accounts/login/')
def editprofile(request,id):        
    profiles = Profile.open_profile(id)
    current_user = request.user
    if request.method == 'POST':        
        editprofile = EditProfile(request.POST, request.FILES)                
        if editprofile.is_valid():
            profile = editprofile.save(commit=False)            
            profile.user = current_user
            profile.save()                            
        return HttpResponseRedirect(reverse('editprofile', args=[str(id)]))        

    else:
        editprofile = EditProfile()        
    return render(request, 'edit-profile.html', {"profiles": profiles, "editprofile": editprofile, "current_user": current_user})

#follow function
def followview(request, id):
    profile= get_object_or_404(Profile, id=request.POST.get('profile_id'))    
    myprofile = Profile.open_profile(request.user.id) 
    is_followed = False
    if profile.followers.filter(id = request.user.id).exists():        
        profile.followers.remove(request.user)
        myprofile.following.remove(profile.user.id)        
        is_followed = False
    else:        
        profile.followers.add(request.user)
        myprofile.following.add(profile.user.id)        
        is_followed = True
    return HttpResponseRedirect(reverse('profilevisit', args=[str(id)]))        


def search_results(request):
    current_user = request.user
    profile = Profile.open_profile(current_user.id)
    if 'user' in request.GET and request.GET["user"]:
        search_term = request.GET.get("user")
        searched_profile = Profile.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message, "searchs": searched_profile, "current_user":current_user,"profile": profile})

    else:
        message = "You haven't searched for any term"
        return render(request, "search.html",{"message":message, "current_user":current_user, "profile": profile})