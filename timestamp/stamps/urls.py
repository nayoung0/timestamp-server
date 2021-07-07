from django.urls import path
from stamps import views

urlpatterns = [
    path(r'kakao-noti/products', views.StampListView.as_view(), name='stamps'),
]