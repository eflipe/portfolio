from django.contrib import admin
from app_blog.models import Post, Category, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish', 'status')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('status', 'publish')

class CategoryAdmin(admin.ModelAdmin):
    pass


class CommentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
