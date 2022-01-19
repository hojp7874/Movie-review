from django.shortcuts import get_object_or_404
from rest_framework.response import Response


def authorization(func):
    def wrapper(self, request, *args, **kwargs):
        user = get_object_or_404(self.User, *args, **kwargs)
        if user != request.user:
            return Response({'error': '사용자 권한이 없습니다.'})
        return func(self, request, *args, **kwargs)
    return wrapper