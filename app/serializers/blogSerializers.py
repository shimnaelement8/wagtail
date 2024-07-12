from rest_framework import serializers
from blog.models import BlogPage

class BlogPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPage
        fields = ['date', 'intro', 'body', 'authors']  # Adjust fields as needed