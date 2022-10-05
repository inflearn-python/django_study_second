from django.contrib import admin
# Register your models here.
from django.utils.safestring import mark_safe

from instagram.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'photo_tag', 'message', 'message_length', 'is_public']
    list_display_links = ['message']
    list_filter = ['created_at', 'is_public']
    search_fields = ['message']

    def photo_tag(self, post):
        if post.photo:
            return mark_safe(f'<img src="{post.photo.url}" style="width: 72px; >')
        return None

    def message_length(self, post):
        return f'{len(post.message)} 글자'
