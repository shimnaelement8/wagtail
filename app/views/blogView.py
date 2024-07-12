from rest_framework import viewsets
from wagtail.api.v2.views import BaseAPIViewSet
from blog.models import BlogPage
from app.serializers.blogSerializers import BlogPageSerializer

class PostPagesAPIViewSet(BaseAPIViewSet):
    base_serializer_class = BlogPageSerializer
    queryset = BlogPage.objects.all()

    def get_queryset(self):
        return self.queryset