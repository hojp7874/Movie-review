from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from rest_framework import status, mixins, generics
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import UserSerializer
from module import custom_decorator
from module.error import ConfirmError


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
            try:
                validate_password(password=password, user=self.User)
            except ValidationError as e:
                return Response({'error': e}, status=status.HTTP_400_BAD_REQUEST)
            user = serializer.save()
            user.set_password(password)
            user.save()
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
        password = request.data.get('password')
        new_password = request.data.get('newPassword')
        new_password_confirmation = request.data.get('newPasswordConfirmation')
        if password and not check_password(password, request.user.password):
            return Response({'error': '비밀번호가 틀렸습니다.'},
                            status=status.HTTP_400_BAD_REQUEST)
        if new_password and new_password != new_password_confirmation:
            return Response({'error': '비밀번호가 일치하지 않습니다.'},
                            status=status.HTTP_400_BAD_REQUEST)
                            
        user = get_object_or_404(self.User, username=username)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            if new_password:
                user.set_password(new_password)
                user.save()
        return Response(serializer.data)
    
    @authentication_classes([IsAuthenticated])
    @custom_decorator.authorization
    def delete(self, request, username: str):
        return self.destroy(request, username)