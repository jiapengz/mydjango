from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404

# Create your views here.

def post_list(request):
	post = Post.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')
	return render(request, 'blog/post_list.html', {'posts':post})

def post_detail(request, pk):
	queryset = Post.objects.filter(publish_date__lte=timezone.now())
	post = get_object_or_404(queryset, pk=pk)
	return render(request, 'blog/post_detail.html', {'post': post})