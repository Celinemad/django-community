from django.db import models
from members.models import CustomUser

class Board(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, null=True, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return self.title
    
class Comments(models.Model):
    id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Board, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()

    def __str__(self):
        return self.comment
