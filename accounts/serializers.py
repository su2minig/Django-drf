from .models import CustomUser
from rest_framework.serializers import ModelSerializer

class CustomUserSerializer(ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = ['email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    
    def create(self, validated_data):
        '''
        사용자 유효성 검사 후 사용자 생성하는 함수
        '''
        password = validated_data.pop('password')
        user = CustomUser(
            email=validated_data.pop('email'))
        user.set_password(password)
        user.save()
        return user