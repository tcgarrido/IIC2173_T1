from django.db import models
import socket

# Create your models here.
class CreateComment(models.Model):
        date = models.DateTimeField(auto_now_add=True)
        content = models.CharField(max_length=200)
        server_IP = socket.gethostbyname(socket.gethostname())

        def __str__(self):
            return self.content
