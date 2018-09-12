from django.db import models

# Create your models here.
class CreateComment(models.Model):
        date = models.DateTimeField(auto_now_add=True)
        content = models.CharField(max_length=200)
        server_IP = models.GenericIPAddressField(default="146.155.13.189")

        def __str__(self):
            return self.content
