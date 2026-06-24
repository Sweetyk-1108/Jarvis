from django.db import models

class ChatHistory(models.Model):
    user_message = models.TextField()
    jarvis_response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
