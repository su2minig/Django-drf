from django.urls import path, include
from .views import UserCreateViewSet

signup_viewset = UserCreateViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

urlpatterns = [
    path('signup/', signup_viewset, name='signup'),
]