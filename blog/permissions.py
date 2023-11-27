from rest_framework import permissions
from rest_framework.authtoken.models import Token

SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')


class IsAuthorOrReadOnly(permissions.BasePermission):
    # R은 모두 허용
    # C는 로그인 사용자 허용
    # UD는 작성자만 허용
    def has_permission(self, request, view):
        '''
        GET, HEAD, OPTIONS 요청은 인증 여부와 상관없이 항상 True를 리턴
        '''
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.method == "POST":
            token = request.headers.get('Authorization', None)
            if token:
                token_key = token.split()[1]
                # 유효한 토근인지 확인합니다. 아래 코드에서 token이 유효하지 않으면 애러 발생하면 except로 넘어갑니다.
                token = Token.objects.get(key=token_key)
                print("ddd",request.user)
                if token.user:
                    return True
            else:
                return False
        
    def has_object_permission(self, request, view, obj):
        '''
        GET, HEAD, OPTIONS 요청은 인증 여부와 상관없이 항상 True를 리턴합니다.
        그 외 요청(PUT, DELETE)에 대해서는 작성자에 한해서만 True를 리턴합니다.
        '''
        if request.method in permissions.SAFE_METHODS:
            return True
        token = request.headers.get('Authorization', None)
        if token:
            token_key = token.split()[1]
            # 유효한 토근인지 확인합니다. 아래 코드에서 token이 유효하지 않으면 애러 발생하면 except로 넘어갑니다.
            token = Token.objects.get(key=token_key)
            print(obj.author, token.user)
            return obj.author == token.user.username
        else:
            return False