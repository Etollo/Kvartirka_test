from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'body', 'comments')
    list_filter = ('date_publication', 'slug')
    search_fields = ('title', 'body', 'data_publication', 'slug')


admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'content_type', 'created', 'content_object')
    list_filter = ('created', 'updated')
    search_fields = ('name', 'object_id', 'body')
    autocomplete_lookup_fields = {
        'generic': [['content_type', 'object_id']],
    }


admin.site.register(Comment, CommentAdmin)
