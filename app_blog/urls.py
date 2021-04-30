from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path("", views.BlogListView.as_view(), name="blog_index"),
    path("<int:year>/<int:month>/<int:day>/<slug:post>/", views.blog_detail, name="blog_detail"),
    path("<category>/", views.blog_category, name="blog_category"),
]
