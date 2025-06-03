
from django.db import models
from accounts.models import CustomUser
# Create your models here.



class Post(models.Model):
    auth = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=255 )
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    
    def __str__(self):
        return f"{self.title} by {self.auth}"
    