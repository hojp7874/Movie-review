from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .models import User
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from .serializers import UserSerializer
from django.contrib.auth import get_user_model


@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def profile(request):
    User = get_user_model()
    person = get_object_or_404(User, username=request.user)
    serializer = UserSerializer(person)
    return Response(serializer.data)



# 유저정보 가져오기
@api_view(['GET'])
def get_users(request):
    # users = get_user_model()
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    print('serializer complete')
    return Response(serializer.data)


@api_view(['POST'])
def signup(request):
	#1-1. Client에서 온 데이터를 받아서
    password = request.data.get('password')
    password_confirmation = request.data.get('passwordConfirmation')
		
	#1-2. 패스워드 일치 여부 체크
    if password != password_confirmation:
        return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)
		
	#2. UserSerializer를 통해 데이터 직렬화
    serializer = UserSerializer(data=request.data)
    
	#3. validation 작업 진행 -> password도 같이 직렬화 진행
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        #4. 비밀번호 해싱 후 
        user.set_password(request.data.get('password'))
        user.save()
        # print(user.password)
    # password는 직렬화 과정에는 포함 되지만 → 표현(response)할 때는 나타나지 않는다.
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
def user_update_delete(request):
    print('call')
    if request.method == 'PUT':
        print('PUT')
        #1-1. Client에서 온 데이터를 받아서
        old_password = request.data.get('oldPassword')
            
        #1-2. 패스워드 일치 여부 체크
        if old_password != request.user.password:
            print(request.user.password)
            return Response({'error': '이전 비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)
            
        #2. UserSerializer를 통해 데이터 직렬화
        serializer = UserSerializer(data=request.data)
        
        #3. validation 작업 진행 -> password도 같이 직렬화 진행
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            #4. 비밀번호 해싱 후 
            user.set_password(request.data.get('newPassword'))
            user.save()
            # print(user.password)
        # password는 직렬화 과정에는 포함 되지만 → 표현(response)할 때는 나타나지 않는다.
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        print('DELETE')
        user = User.objects.get(pk=request.user)
        user.delete()
        return Response({'id가 삭제되었습니다'})