from .serializers import RegisterSerializer, LoginSerializer, UserUpdateSerializer
from .models import CustomUser
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status, generics
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView



class SignupView(generics.CreateAPIView): #CreateAPIView는 post요청을 받아서 새로운 객체를 생성
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer

signup = SignupView.as_view()

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        # user = authenticate(
        #     username=request.data.get("username"), password=request.data.get("password")
        # )
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True) # 유효성 검사
        token = serializer.validated_data
        return Response({
            'token': token.key,
        }, status=status.HTTP_200_OK)

    
login = LoginView.as_view()
    

class UserViewSet(ModelViewSet):
    '''
    사용자 정보 RUD
    '''
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, pk=None):
        '''
        사용자 정보 조회
        '''
        user = CustomUser.objects.get(pk=pk)
        serializer = self.get_serializer(user)
        return Response(serializer.data)
    
    def update(self, request, pk):
        '''
        사용자 정보 수정
        '''
        user = CustomUser.objects.get(pk=pk)
        serializer = UserUpdateSerializer(user, data=request.data)
        if request.user == user:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, pk):
        '''
        사용자 정보 삭제
        '''
        user = CustomUser.objects.get(pk=pk)
        if request.user == user:
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)