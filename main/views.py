from ast import Return
from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required,permission_required
# Create your views here.

def index(request):
    return redirect('/home/')

def home(request):
    posts=Post.objects.all().order_by('-created_at')
    if request.method=='POST':
        id=request.POST.get('post_id')
        object=Post.objects.get(pk=id)
        object.delete()
        return redirect('/home/')
    return render(request,'main/home.html',{'posts':posts})

def signup(request):
    form=SignUpForm()
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('/login/')
    return render(request,'registration/register.html',{'form':form})

@login_required(login_url='/login/')
def Create_Post(request):
    form=PostForm()
    if request.method =="POST":
        form=PostForm(request.POST,request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.save()
            return redirect('/home/')
    return render(request,'main/post.html',{'form':form})

@login_required(login_url='/login/')
def MyPosts(request):
    posts=Post.objects.filter(author=request.user)
    if request.method=='POST':
        id=request.POST.get('post_id')
        object=Post.objects.get(pk=id)
        object.delete()
        return redirect('/home/')
    return render(request,'main/myposts.html',{'posts':posts})

@login_required(login_url='/login/')
def update(request,id):
    if request.method=='POST':
        object=Post.objects.get(pk=id)
        form=PostForm(request.POST,request.FILES,instance=object)
        if form.is_valid():
            form.save()
            return redirect('/home/')
    else:
        object=Post.objects.get(pk=id)
        form=PostForm(instance=object)
    return render(request, 'main/update.html',{'form':form})

    