from .models import Board, Comments
from .serializers import BlogSerializer, CommentSerializer
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status, viewsets, mixins
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .permissions import IsOwnerOrReadOnly
from rest_framework.views import APIView
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication


'''
전체 블로그를 조회&작성
'''
class BlogList(ListCreateAPIView):
    queryset = Board.objects.all()
    serializer_class = BlogSerializer
    # authentication_classes = [BasicAuthentication, SessionAuthentication]
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
		
    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user = user)

'''
한 블로그 조회
'''
class BlogDetail(ReadOnlyModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BlogSerializer
    # authentication_classes = [BasicAuthentication, SessionAuthentication]
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class  BlogViewSet(mixins.UpdateModelMixin, 
                        mixins.ListModelMixin, 
                        mixins.RetrieveModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):
    queryset = Board.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

'''
comments 조회/작성
'''
class CommentsList(ListCreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer
    # authentication_classes = [BasicAuthentication, SessionAuthentication]
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)