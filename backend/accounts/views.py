from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from django.shortcuts import get_object_or_404
from rest_framework import status, mixins, generics
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import UserSerializer
from module import custom_decorator


class UserList(generics.ListAPIView):
    """
    모든 User 목록을 반환하거나, 회원가입을 합니다.
    """

    User = get_user_model()
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request):
        password = request.data.get('password')
        password_confirmation = request.data.get('passwordConfirmation')
        if password != password_confirmation:
            return Response({'error': '비밀번호가 일치하지 않습니다.'},
                            status=status.HTTP_400_BAD_REQUEST)

        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            saved_user = serializer.save()
            saved_user.set_password(password)
            saved_user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserDetail(mixins.DestroyModelMixin,
                 generics.RetrieveAPIView):
    """
    User의 프로필 보기, 회원정보수정, 회원탈퇴를 합니다.
    """

    User = get_user_model()
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'

    @permission_classes([IsAuthenticated])
    @custom_decorator.authorization
    def patch(self, request, username: str):
        old_password = request.data.get('oldPassword')
        new_password = request.data.get('newPassword')
        if not check_password(old_password, request.user.password):
            return Response({'error': '비밀번호가 일치하지 않습니다.'},
                            status=status.HTTP_400_BAD_REQUEST)

        user = get_object_or_404(self.User, username=username)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            saved_user = serializer.save()
            if new_password:
                saved_user.set_password(new_password)
                saved_user.save()
        return Response(serializer.data)
    
    @authentication_classes([IsAuthenticated])
    @custom_decorator.authorization
    def delete(self, request, username: str):
        return self.destroy(request, username)