from django.contrib import admin

# Register your models here.

from comment.models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['publisher', 'content', 'created_on']
