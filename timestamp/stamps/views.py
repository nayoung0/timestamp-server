from django.conf import settings
from django.contrib.auth.models import User
from django.db import transaction

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


class StampListView(generics.CreateAPIView):
    """ 스탬프 리스트 조회 및 스탬프 생성 """
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        return Response(data={}, status=status.HTTP_200_OK)

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        return Response(data={}, status=status.HTTP_201_CREATED)