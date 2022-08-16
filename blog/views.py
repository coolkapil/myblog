from rest_framework import viewsets, status
from .models import Post
from django.contrib.auth.models import User, Permission
from .serializers import PostSerializer, UserSerializer
from .permissions import IsStaffUser, IsAdminUser
from rest_framework.response import Response


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer        


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = (UserPermission,)


    # def list(self, request):
    #     if self.request.user.is_staff:
    #         return super(UserViewSet, self).list(request)
    #     else:
    #         content = {'Unauthorised': 'This API is private'}
    #         return Response(content, status=status.HTTP_401_UNAUTHORIZED)


    # def create(self, request):
    #     if self.request.user.is_superuser:
    #         return super(UserViewSet, self).create(request)
    #     else:
    #         content = {'Unauthorised': 'This API is private'}
    #         return Response(content, status=status.HTTP_401_UNAUTHORIZED)


    # def update(self, request, *args, **kwargs):
    #     if self.request.user.is_superuser:
    #         return super(UserViewSet, self).update(request)
    #     else:
    #         content = {'Unauthorised': 'This API is private'}
    #         return Response(content, status=status.HTTP_401_UNAUTHORIZED)
    
    # def destroy(self, request, *args, **kwargs):
    #     if self.request.user.is_superuser:
    #         return super(UserViewSet, self).delete(request)
    #     else:
    #         content = {'Unauthorised': 'This API is private'}
    #         return Response(content, status=status.HTTP_401_UNAUTHORIZED)
