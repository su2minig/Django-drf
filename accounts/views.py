from rest_framework.viewsets import ModelViewSet
from .serializers import CustomUserSerializer
from .models import CustomUser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView


class UserCreateViewSet(ModelViewSet):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()
    

# class UserCreateAPIView(CreateAPIView):
#     serializer_class = CustomUserSerializer

# signup = UserCreateAPIView.as_view()