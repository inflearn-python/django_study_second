from rest_framework import generics
# Create your views here.
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

from instagram.models import Post
from instagram.serializers import PostModelSerializer


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostModelSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostModelSerializer
    # authentication_classes = [IsAuthenticated]
    permission_classes = [IsAuthenticatedOrReadOnly]


    def perform_create(self, serializer):
        # FIXME : 인증이 되어있다는 가정하에, author 를 지정
        author = self.request.user  # User or AnonymousUser
        ip = self.request.META['REMOTE_ADDR']
        serializer.save(author=author, ip=ip)


    @action(detail=False, methods=['GET'])
    def public(self, request):
        qs = self.queryset.filter(is_public=True)
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['PATCH'])
    def set_public(self, request, pk):
        instance = self.get_object()
        instance.is_public = True
        instance.save(update_fields=['is_public'])
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()

    def get(self, request, *args, **kwargs):
        post = self.get_object()
        return Response({
            'post': PostModelSerializer(post).data,
        })