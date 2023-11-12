from django.db import models
from datetime import datetime

class Post(models.Model):  # Renamed the model to "Post" for consistency
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=100000)  # Changed CharField to TextField for longer text
    created_at = models.DateTimeField(default=datetime.now, blank=True)
