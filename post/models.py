from django.db import models
from datetime import date
# Create your models here.
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    desc = models.TextField()
    img = models.ImageField(upload_to='pictures',blank=True)
    date = models.DateTimeField(auto_now_add=1)
    def __str__(self):
        return self.title
    
