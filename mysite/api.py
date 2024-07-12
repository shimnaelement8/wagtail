from wagtail.api.v2.views import PagesAPIViewSet
from wagtail.api.v2.router import WagtailAPIRouter
from wagtail.images.api.v2.views import ImagesAPIViewSet
from wagtail.documents.api.v2.views import DocumentsAPIViewSet
from app.serializers.blogSerializers import BlogPageSerializer
from blog.models import BlogPage
from wagtail.api.v2.views import BaseAPIViewSet


# Create the router. "wagtailapi" is the URL namespace
api_router = WagtailAPIRouter('wagtailapi')

# Add the three endpoints using the "register_endpoint" method.
# The first parameter is the name of the endpoint (such as pages, images). This
# is used in the URL of the endpoint
# The second parameter is the endpoint class that handles the requests
#api_router.register_endpoint('pages', PagesAPIViewSet)
#api_router.register_endpoint('images', ImagesAPIViewSet)
#api_router.register_endpoint('documents', DocumentsAPIViewSet)

class PostPagesAPIViewSet(BaseAPIViewSet):
    base_serializer_class = BlogPageSerializer
    queryset = BlogPage.objects.all()

    def get_queryset(self):
        return self.queryset

api_router.register_endpoint("posts", PostPagesAPIViewSet)