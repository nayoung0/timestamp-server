from django.shortcuts import render

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from pictures.serializers import PictureSerializer
from pictures.models import Picture

class PictureList(generics.RetrieveAPIView):
    """ 사진 목록 """
    permission_classes = (AllowAny, )
    authentication_classes = ()
    serializer_class = PictureSerializer

    def get_queryset(self):
        pictures = Picture.objects.all()
        return pictures

    def get(self, request, *args, **kwargs):
        pictures = self.get_queryset()
        serializer = self.get_serializer(pictures, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
