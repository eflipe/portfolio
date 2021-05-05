from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.core.mail import send_mail
from app_blog.models import Post, Comment
from app_blog.form import CommentForm, EmailPostForm


class BlogListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = "blog_index.html"


def blog_category(request, category):
    posts = Post.objects.filter(
            categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "blog_category.html", context)


def blog_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                                   status='published',
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()

    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": form,
        }
    return render(request, "blog_detail.html", context)


def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False

    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            # send mail
            subject = f"{cd['name']} te recomienda que leas " \
                      f"{post.title}"
            message = f"Lee {post.title} en {post_url}\n\n" \
                      f"{cd['name']} dice: {cd['comments']}"
            send_mail(subject, message, 'heyheymycode@gmail.com',
                      [cd['to']])
            sent = True
    else:
        form = EmailPostForm()

    template = 'share.html'
    context = {
        'post': post,
        'form': form,
        'sent': sent
            }
    return render(request, template, context)
