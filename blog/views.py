from rest_framework import viewsets
from blog.models import BlogPage
from .serializers import BlogPageSerializer

class BlogPageViewSet(viewsets.ModelViewSet):
    queryset = BlogPage.objects.all()
    serializer_class = BlogPageSerializer

    