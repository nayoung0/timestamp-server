from rest_framework import serializers
from django.conf import settings

from pictures.models import Picture

class PictureSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)
    title = serializers.CharField(required=True, max_length=200)
    background_color = serializers.CharField(required=False)
    text_color = serializers.CharField(required=False)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Picture
        fields = ('id', 'image', 'title', 'background_color', 'text_color', 'created_at', 'updated_at')
