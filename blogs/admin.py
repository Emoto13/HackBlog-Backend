from django.contrib import admin

from blogs.models import PoliticsBlog, SportBlog, TechBlog, OpinionBlog, OtherBlog


@admin.register(PoliticsBlog)
class PoliticsBlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'date')


@admin.register(SportBlog)
class SportBlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'date')


@admin.register(TechBlog)
class TechBlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'date')


@admin.register(OpinionBlog)
class PoliticsBlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'date')


@admin.register(OtherBlog)
class PoliticsBlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'date')
