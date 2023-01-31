from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm
# Create your views here.
def index (request):

        #if the method is post
    if request.method=='POST':
        form=PostForm(request.POST)
        #if the form is valid
        if form.is_valid():
        #form to be saved 
            form.save()
        #form to be redirected to home
            return HttpResponseRedirect("/")
        #if the form is invalid
        else:
            return HttpResponseRedirect(form.errors.as_json())
       
    posts=Post.objects.all()[:20]
    
    return render(request,'posts.html',{"posts":posts})
 
def delete(request,post_id):
    #select USer
    post=Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect("/") 
    
def edit(request, post_id):

    posts=Post.objects.get(id=post_id) #
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=posts)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
        else:
            return HttpResponse("not valid")

    return render(request,'edit.html', {'posts':posts})
        


