from django.shortcuts import render
from .models import Blog, Subscriber
from django.contrib import messages
from django.shortcuts import redirect

from .forms import BlogForm

from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def about(request):
    context ={
        'message': 'Hello everyone, welcome to my blog'
    }
    return render(request, 'about.html', context)

def blog_list(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request, 'blogs.html', context)

def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog =form.save()
            messages.success(request, 'Blog post created successfully!')
            return redirect('blog)list')
        else:
            messages.error(request, 'please correct the errors below.')
    else:
        form =BlogForm()

    return render(request, 'create_blog.html', {'form': form})

def subscribe(request):
    if request.method == 'POST':
        email = request.POST['email']
        if Subscriber.objects.filter(email=email).exists():
            messages.error(request, 'You are already subscribed.')
        else:
            subscriber = Subscriber(email=email)
            subscriber.save()
            messages.success(request, 'Thank you for subscribing!')
            return redirect('subscribe')
    return render(request, 'subscribe.html')

def error_404(request, exception):
    return render(request, '404.html')