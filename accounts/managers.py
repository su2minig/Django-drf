# accounts/managers.py
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):

    def create_user(self, username, email, password, **extra_fields):        
        if not email:            
            raise ValueError('이메일을 기입해주세요')
        if not username:            
            raise ValueError('아이디를 입력하세요')
        if not password:            
            raise ValueError('비밀번호를 입력해주세요')
        email = self.normalize_email(email)
        user = self.model(            
            email=email,
            username=username,
            **extra_fields,      
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        
        return self.create_user(username, email, password, **extra_fields)