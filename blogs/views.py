from rest_framework import viewsets
from blogs.models import PoliticsBlog, SportBlog, TechBlog, OpinionBlog, OtherBlog

from blogs.serializers import PoliticsBlogSerializer, SportBlogSerializer, TechBlogSerializer, \
    OpinionBlogSerializer, OtherBlogSerializer


class PoliticsBlogListViewSet(viewsets.ModelViewSet):
    queryset = PoliticsBlog.objects.all()
    serializer_class = PoliticsBlogSerializer


class SportBlogListViewSet(viewsets.ModelViewSet):
    queryset = SportBlog.objects.all()
    serializer_class = SportBlogSerializer


class TechBlogListViewSet(viewsets.ModelViewSet):
    queryset = TechBlog.objects.all()
    serializer_class = TechBlogSerializer


class OpinionBlogListViewSet(viewsets.ModelViewSet):
    queryset = OpinionBlog.objects.all()
    serializer_class = OpinionBlogSerializer


class OtherBlogListViewSet(viewsets.ModelViewSet):
    queryset = OtherBlog.objects.all()
    serializer_class = OtherBlogSerializer
