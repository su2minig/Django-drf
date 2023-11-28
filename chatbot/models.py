# chatbot/models.py
from django.conf import settings
from django.db import models

class ChatHistory(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Conversation(models.Model):
    ChatHistory = models.ForeignKey(ChatHistory, on_delete=models.CASCADE)
    prompt = models.CharField(max_length=512)
    response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.prompt}: {self.response}"