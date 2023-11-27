from rest_framework.viewsets import ModelViewSet
from .models import Post
from .serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthorOrReadOnly
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

# class PostViewSet(ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     # permission_classes = [IsAuthenticated, IsAuthorOrReadOnly] # 로그인된 사용자만 접근 가능
#     # permission_classes = [IsAuthorOrReadOnly] 
#     permission_classes = [IsAuthenticated]

class PostListAPIView(APIView):
    # permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthorOrReadOnly]
    
    def get(self, request):
        post_list = Post.objects.all()
        serializer = PostSerializer(post_list, many=True)
        return Response(serializer.data)
    def post(self, request):
        # request에 headers에 있는 Authorization: Bearer ${token}로 넘어온 토큰 확인하여 post 처리
        print(request.headers)
        print(request.headers['Authorization'])
        print(request.headers['Authorization'].split(' ')[1])
        token = request.headers.get('Authorization', None)
        print(token)
        if token:
            print('토큰 존재!')
            try:
                token_key = token.split()[1]
                # 유효한 토근인지 확인합니다. 아래 코드에서 token이 유효하지 않으면 애러 발생하면 except로 넘어갑니다.
                token = Token.objects.get(key=token_key)
                print('토큰:', token)
                print('사용자:', token.user.username)
                request.data['author'] = token.user.pk
                print(request.data)
            except:
                print('토큰이 유효하지 않습니다.')
                return Response({'error':'애러야!!'}, status=400)
        print(request.data)
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
postlist = PostListAPIView.as_view()

class PostDetailAPIView(APIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthorOrReadOnly]

    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    
    def put(self, request, pk):
        token = request.headers.get('Authorization', None)
        print(request.headers)
        if token:
            print('토큰 존재!')
            try:
                token_key = token.split()[1]
                # 유효한 토근인지 확인합니다. 아래 코드에서 token이 유효하지 않으면 애러 발생하면 except로 넘어갑니다.
                token = Token.objects.get(key=token_key)
                print('토큰:', token)
                print('사용자:', token.user.username)
                print(request.data)
            except:
                print('토큰이 유효하지 않습니다.')
                return Response({'error':'애러야!!'}, status=400)
        post = Post.objects.get(pk=pk)
        serializer = PostSerializer(post, data=request.data)
        if token.user.pk == post.author:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        else:
            return Response({'error':'작성자만 수정 가능합니다.'}, status=400)
    

postdetail = PostDetailAPIView.as_view()