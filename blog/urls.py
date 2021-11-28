from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework_nested import routers

from .views import BlogViewSet, CommentViewSet

router = SimpleRouter()
router.register('blog', BlogViewSet, basename='blog')
domains_router = routers.NestedSimpleRouter(router, r'blog', lookup='blog')
domains_router.register(r'comments', CommentViewSet, basename='comments')
urlpatterns = [
    path('', include(router.urls)),
    path('', include(domains_router.urls)),

]
