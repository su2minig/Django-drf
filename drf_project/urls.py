from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('accounts.urls')),
    path('blog/', include('blog.urls')),
    path('chat/', include('chatbot.urls')),
]
