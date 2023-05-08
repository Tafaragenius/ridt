from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.utils import timezone
from . models import Blog, Comment

# Create your views here.
def dashboard(request):
    blogs = Blog.objects.all()
    comments = Comment.objects.all()
    return render(request, 'dashboard.html', {'blogs':blogs, 'comments':comments})

@login_required
def create_blog(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        blog = Blog(title=title, content=content, created_by=request.user.author)
        blog.save()
        messages.success(request, 'Blog created Successfully')
        return redirect('dashboard')
    return render(request, 'create-blog.html')

def read_blog(request, blog_id):
    blog = get_object_or_404(Blog,id=blog_id)
    comments = blog.comments.all()
    return render(request, 'read-blog.html',{'blog':blog,'comments':comments})

@staff_member_required
def admin_blog(request):
    blogs = Blog.objects.all()
    return render(request, 'admin-blog.html',{'blogs':blogs})

@staff_member_required
def delete_blog(request, blog_id):
    blog = get_object_or_404(blog,id=blog_id)
    blog.delete()
    messages.success(request,'Blog deleted Successfully')
    return redirect('admin-blog')

@login_required
def create_comment(request,blog_id):
    if request.method == 'POST':
        content = request.POST['content']
        blog = get_object_or_404(Blog,id=blog_id)
        comment = Comment(content=content, blog=blog,created_by=request.user.author)
        comment.save()
        messages.success(request,'Comment Created Successfully')
        return redirect('read-blog',blog_id=blog_id)
    return render(request, 'create-comment.html')

@staff_member_required
def admin_comment(request):
    comments = Comment.objects.all()
    return render(request, 'admin-comment.html', {'comments':comments})

@staff_member_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment,id=comment_id)
    comment.delete()
    messages.success(request,'Comment deleted successfully')
    return redirect('admin-comment')

@staff_member_required
def admin_user(request):
    users = User.objects.all()
    return render(request, 'admin-user.html',{'users'})


