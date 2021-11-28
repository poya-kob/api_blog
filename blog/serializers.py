from rest_framework.relations import HyperlinkedIdentityField
from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from rest_framework import serializers
from rest_framework_nested.relations import NestedHyperlinkedRelatedField
from rest_framework_nested.serializers import NestedHyperlinkedModelSerializer

from .models import Blog, BlogCategory, Comments


class CategorySerializer(ModelSerializer):
    class Meta:
        model = BlogCategory
        exclude = ['id']


class BlogListSerializer(HyperlinkedModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Blog
        exclude = ['active', 'text']


# moshkel inheritance in bood
class CommentsSerializer(NestedHyperlinkedModelSerializer):
    user = serializers.StringRelatedField()
    blog = serializers.StringRelatedField()
    parent_lookup_kwargs = {'blog_pk': 'blog__pk'}

    class Meta:
        model = Comments
        fields = "__all__"


class BlogDetailSerializer(HyperlinkedModelSerializer):
    # comment = HyperlinkedIdentityField(
    #     view_name='comments-list',
    #     lookup_url_kwarg='blog_pk'
    # )
    comment = NestedHyperlinkedRelatedField(
        many=True,
        read_only=True,  # Or add a queryset
        view_name='comments-detail',
        parent_lookup_kwargs={'blog_pk': 'blog__pk'}
        # ^-- Nameserver queryset will .filter(domain__pk=domain_pk)
        #     being domain_pk (ONE underscore) value from URL kwargs
    )

    class Meta:
        model = Blog
        exclude = ['active', 'category']
