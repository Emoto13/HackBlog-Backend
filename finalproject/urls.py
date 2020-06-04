"""finalproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from blogs.views import PoliticsBlogListViewSet, SportBlogListViewSet,\
    TechBlogListViewSet, OpinionBlogListViewSet, OtherBlogListViewSet,\
    PoliticsBlogCreateView, SportBlogCreateView, OpinionBlogCreateView, TechBlogCreateView, OtherBlogCreateView
from finalproject import settings
from comment.views import CommentViewSet

router = routers.DefaultRouter()
router.register('politics', PoliticsBlogListViewSet)
router.register('sport', SportBlogListViewSet)
router.register('tech', TechBlogListViewSet)
router.register('opinion', OpinionBlogListViewSet)
router.register('other', OtherBlogListViewSet)
router.register('comments', CommentViewSet)

urlpatterns = [
    path('sport/create', SportBlogCreateView.as_view(), name='sport-post'),
    path('politics/create', PoliticsBlogCreateView.as_view(), name='politics-post'),
    path('tech/create', TechBlogCreateView.as_view(), name='tech-post'),
    path('opinion/create', OpinionBlogCreateView.as_view(), name='opinion-post'),
    path('other/create', OtherBlogCreateView.as_view(), name='other-post'),

    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
