from django.shortcuts import render, get_object_or_404

from .models import Post

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from taggit.models import Tag


# Create your views here.
def post_list(request, tag_slug=None):
    # Pagination with 3 posts per page
    post_list = Post.published.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        post_list = post_list.filter(tags__in=[tag])
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page', 1)
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        # If page_number is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page_number is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/list.html', {'posts': posts, 'tag': tag})


from django.http import Http404
def post_detail(request, year, month, day, post):
    try:
        post = get_object_or_404(Post,
                             status=Post.Status.PUBLISHED,
                             slug=post,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    except Post.DoesNotExist:
        raise Http404("No Post found.")
    return render(request,
                  'blog/detail.html',
                  {'post': post})