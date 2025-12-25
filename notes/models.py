from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Note(models.Model):
    # заменяем дефолтный автоинкрементный id на UUID  ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 

    title = models.CharField(max_length=200)
    text = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.PositiveSmallIntegerField(default=0)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notes')
    is_public = models.BooleanField(default=False)

    # def __str__(self):
    #     return self.title       
    
    class Meta:
        ordering = ['-updated_at', 'title']
       



