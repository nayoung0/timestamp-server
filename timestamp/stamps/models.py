from django.db import models

# Create your models here.

class Template(models.Model):
    """
    스탬프 템플릿
    """
    name = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)