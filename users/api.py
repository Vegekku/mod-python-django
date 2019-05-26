from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import status, filters
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from users.permissions import UserPermission
from users.serializers import UserListSerializer, UserSerializer, UserWriteSerializer, BlogSerializer


class UsersAPI(APIView):

    permission_classes = [UserPermission]

    # def get(self, request):
    #     users = User.objects.all()
    #     serializer = UserListSerializer(users, many=True)
    #     return Response(serializer.data)

    def post(self, request):
        serializer = UserWriteSerializer(data=request.data)
        if serializer.is_valid():
            new_user = serializer.save()
            user_serializer = UserSerializer(new_user)
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserAPI(APIView):

    permission_classes = [UserPermission]

    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        self.check_object_permissions(request, user)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        self.check_object_permissions(request, user)
        serializer = UserWriteSerializer(user, data=request.data)
        if serializer.is_valid():
            updated_user = serializer.save()
            user_serializer = UserSerializer(updated_user)
            return Response(user_serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        self.check_object_permissions(request, user)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BlogsAPI(ListAPIView):

    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('username',)
    ordering_fields = ('username',)
    ordering = ('username',)

    queryset = User.objects.all()
    serializer_class = BlogSerializer
