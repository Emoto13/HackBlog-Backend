from rest_framework import viewsets, generics
from blogs.models import PoliticsBlog, SportBlog, TechBlog, OpinionBlog, OtherBlog

from blogs.serializers import PoliticsBlogSerializer, SportBlogSerializer, TechBlogSerializer, \
    OpinionBlogSerializer, OtherBlogSerializer


# Politics
class PoliticsBlogListViewSet(viewsets.ModelViewSet):
    queryset = PoliticsBlog.objects.all()
    serializer_class = PoliticsBlogSerializer


class PoliticsBlogCreateView(generics.CreateAPIView):
    queryset = PoliticsBlog.objects.all()
    serializer_class = PoliticsBlogSerializer


# Sport
class SportBlogListViewSet(viewsets.ModelViewSet):
    queryset = SportBlog.objects.all()
    serializer_class = SportBlogSerializer


class SportBlogCreateView(generics.CreateAPIView):
    queryset = SportBlog.objects.all()
    serializer_class = SportBlogSerializer


# Tech
class TechBlogListViewSet(viewsets.ModelViewSet):
    queryset = TechBlog.objects.all()
    serializer_class = TechBlogSerializer


class TechBlogCreateView(generics.CreateAPIView):
    queryset = TechBlog.objects.all()
    serializer_class = TechBlogSerializer


# Opinion
class OpinionBlogListViewSet(viewsets.ModelViewSet):
    queryset = OpinionBlog.objects.all()
    serializer_class = OpinionBlogSerializer


class OpinionBlogCreateView(generics.CreateAPIView):
    queryset = OpinionBlog.objects.all()
    serializer_class = OpinionBlogSerializer


# Other
class OtherBlogListViewSet(viewsets.ModelViewSet):
    queryset = OtherBlog.objects.all()
    serializer_class = OtherBlogSerializer


class OtherBlogCreateView(generics.CreateAPIView):
    queryset = OtherBlog.objects.all()
    serializer_class = OtherBlogSerializer
