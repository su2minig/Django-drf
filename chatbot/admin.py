from django.contrib import admin
from .models import ChatHistory, Conversation

admin.site.register(ChatHistory)
admin.site.register(Conversation)