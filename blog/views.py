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
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
postlist = PostListAPIView.as_view()


class PostDetailAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthorOrReadOnly]

    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    
    def put(self, request, pk):
        post = Post.objects.get(pk=pk)
        serializer = PostSerializer(post, data=request.data, partial=True) # partial=True를 추가하여 부분 업데이트를 허용
        print("요청유저",request.user)
        print("요청유저pk",request.user.pk)
        print("게시물저자pk",post.author.pk)
        print("게시물저자",post.author)
        print(serializer)
        if request.user.pk == post.author.pk:
            if serializer.is_valid():
                serializer.save(author=request.user)
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        else:
            return Response({'error':'작성자만 수정 가능합니다.'}, status=400)   

postdetail = PostDetailAPIView.as_view()