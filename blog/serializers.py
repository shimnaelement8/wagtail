from rest_framework import serializers
from blog.models import BlogPage,Author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id','name']  # Adjust fields as needed

class BlogPageSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True)  # Nested serializer for authors
    title = serializers.CharField()  # Include the title field from the Page model
    meta = serializers.SerializerMethodField()


    class Meta:
        model = BlogPage
        fields = ['title','date', 'intro', 'body', 'authors','meta']  # List the fields you want in the API response

    def get_meta(self, obj):
        request = self.context.get('request')
        return {
            'id': obj.id,
            'type': obj.content_type.model,
            'detail_url': request.build_absolute_uri(obj.url) if request else obj.url,
        }