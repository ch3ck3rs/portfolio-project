from django.shortcuts import render, get_object_or_404
from .models import Blog
from rest_framework import viewsets
from blog.serializers import BlogSeralizer


def allblogs(request):
    blogs = Blog.objects
    return render(request, 'blog/allblogs.html', {'blogs':blogs})


def detail(request, blog_id):
    detail_blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':detail_blog})


class BlogViewSet(viewsets.ModelViewSet):
    """
    API endoint that allows blogs to be viewed or edited
    """
    queryset = Blog.objects.all()  # .order_by('-date_joined')
    serializer_class = BlogSeralizer
