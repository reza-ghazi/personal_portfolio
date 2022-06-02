from django.shortcuts import render, get_object_or_404
from .models import Blog


def all_blogs(request):
    # Showing blogs in date order. the most recent blog is the first one.
    # And showing only the last 5 blogs in the first page.
    blogs = Blog.objects.order_by('-date')[:5]
    return render(request, 'blog/all_blogs.html', {'blogs': blogs})


# Showing the content of specific blog by its id
def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog})
