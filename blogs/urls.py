from django.urls import path

from blogs.views import BlogListByTopic

urlpatterns = [
    path('blogs/', BlogListByTopic.as_view(), name='blogs')
]
