from django.db import models
from articles.models import Article
from django.contrib.auth.models import User
# Create your models here.

class Comment(models.Model):
    post=models.ForeignKey(Article,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    text=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username}-->{self.text[:30]}"
    


class Like(models.Model):
    post=models.OneToOneField(Article,on_delete=models.CASCADE)
    count=models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.post}--->{self.count}"
    
    def increment(self):
        self.count+=1
        self.save(update_fields=['count'])
