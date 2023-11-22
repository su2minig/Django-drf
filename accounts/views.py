from rest_framework.viewsets import ModelViewSet
from .serializers import CustomUserSerializer
from .models import CustomUser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView


# class UserCreateView(ModelViewSet):
#     serializer_class = CustomUserSerializer
#     queryset = CustomUser.objects.all()
    
#     def create(self, request, *args, **kwargs):
#         serializer = CustomUserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    

class UserCreateAPIView(CreateAPIView):
    serializer_class = CustomUserSerializer

signup = UserCreateAPIView.as_view()