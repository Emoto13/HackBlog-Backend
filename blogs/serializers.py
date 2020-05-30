from rest_framework import serializers

from blogs.models import PoliticsBlog, SportBlog, TechBlog, OpinionBlog, OtherBlog


class PoliticsBlogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PoliticsBlog
        fields = ['id', 'title', 'content', 'date', 'image', 'author_name']


class SportBlogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SportBlog
        fields = ['id', 'title', 'content', 'date', 'image', 'author_name']


class TechBlogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OpinionBlog
        fields = ['id', 'title', 'content', 'date', 'image', 'author_name']


class OpinionBlogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TechBlog
        fields = ['id', 'title', 'content', 'date', 'image', 'author_name']


class OtherBlogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OtherBlog
        fields = ['id', 'title', 'content', 'date', 'image', 'author_name']
