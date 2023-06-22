from django.urls import path, include
from rest_framework import routers

from post.views import PostViewList, PostEditViewSet, PostDetailView

router = routers.DefaultRouter()
router.register('post', PostEditViewSet, basename='post')

urlpatterns = [
    # URLS for Posts
    path('all_posts/', PostViewList.as_view({'get': 'list'}), name='all_posts'),
    path('', include(router.urls)),
    path('post_detail/<int:pk>/', PostDetailView.as_view(), name='post_detail')
]
