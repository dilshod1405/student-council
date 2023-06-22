from rest_framework import viewsets, filters, generics
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from post.models import Post
from post.serializers import PostCardSerializer, PostEditSerializer, PostDetailSerializer


# See All Posts
class PostViewList(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostCardSerializer
    filter_backends = [filters.SearchFilter, ]
    search_fields = ['title', 'author__username', 'category__title']
    pagination_class = LimitOffsetPagination


# Edit personal Post
class PostEditViewSet(ModelViewSet):
    serializer_class = PostEditSerializer
    permission_classes = [IsAuthenticated, ]
    # authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    filter_backends = [filters.SearchFilter, ]
    search_fields = ['title', 'author__username', 'category__title']

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


# See post detail (Post haqidagi to'liq ma'lumotlar)
class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
