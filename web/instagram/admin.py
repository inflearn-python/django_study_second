from django.contrib import admin

# Register your models here.
from instagram.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass