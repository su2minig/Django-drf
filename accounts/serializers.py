from .models import CustomUser
from rest_framework import serializers # 직렬화 모듈
from rest_framework.authtoken.models import Token # 토큰 모델 Token.objects.get()이런식으로 토큰 확인 가능
from rest_framework.validators import UniqueValidator # 중복 검사(회원 가입할 때 동일한 아이디가 있는지 검사 등)
from django.contrib.auth.password_validation import validate_password # 비밀번호 유효성 검사
from django.contrib.auth import authenticate # 인증 모듈

    

class RegisterSerializer(serializers.ModelSerializer):
    '''
    회원 가입 시리얼라이저
    '''
    email = serializers.EmailField(
        required = True,
        validators = [UniqueValidator(queryset=CustomUser.objects.all())] # 중복 검사
    )
    username = serializers.CharField(
        required = True,
        validators = [UniqueValidator(queryset=CustomUser.objects.all())] # 중복 검사
    )
    password = serializers.CharField(
        write_only = True, 
        required = True, 
        validators = [validate_password]
    ) # 비밀번호 유효성 검사(너무 짧은 비밀번호 등)
    password2 = serializers.CharField(
        write_only = True, 
        required = True
    ) # 비밀번호 확인 필드

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'password2']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password': '비밀번호가 일치하지 않습니다.'})
        return attrs
    
    def create(self, validated_data):
        user = CustomUser.objects.create(
            email = validated_data['email'],
            username = validated_data['username']
        )
        user.set_password(validated_data['password']) # 비밀번호 암호화
        user.save()
        Token.objects.create(user=user) # 토큰 생성
        # token = Token.objects.create(user=user)
        # print(token)
        return user
    

class LoginSerializer(serializers.ModelSerializer):
    '''
    로그인 시리얼라이저
    '''
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'password'] # 로그인 시 이메일 비밀번호만 필요

    def validate(self, data):
        print(data)
        user = authenticate(**data)
        print(user)
        print(dir(user))
        if user:
            token = Token.objects.get(user=user)
            return token
        raise serializers.ValidationError("유효하지 않은 로그인입니다.")
    

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def update(self, instance, validated_data):
        # 'update' 메서드를 오버라이드하여 비밀번호를 안전하게 설정하도록 처리할 수 있습니다.
        instance.username = validated_data.get('username', instance.username)
        instance.set_password(validated_data.get('password'))
        instance.save()
        return instance