from .serializers import RegisterSerializer, LoginSerializer
from .models import CustomUser
from rest_framework.response import Response
from rest_framework import status, generics


class SignupView(generics.CreateAPIView): #CreateAPIView는 post요청을 받아서 새로운 객체를 생성
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer

signup = SignupView.as_view()

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True) # 유효성 검사
        token = serializer.validated_data
        return Response({
            'token': token.key,
        }, status=status.HTTP_200_OK)
    
login = LoginView.as_view()