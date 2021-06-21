from django.db import models

class Picture(models.Model):
    """ 타임스탬프 사진 """
    image = models.ImageField(blank=True, null=True, default=None)
    title = models.CharField(max_length=200)
    background_color = models.CharField(max_length=10)
    text_color = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    