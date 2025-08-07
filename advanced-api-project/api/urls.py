from django.urls import path
from .views import MyAPIView

urlpatterns = [
    path('my-api/', MyAPIView.as_view(), name='my_api'),
    path('my-api/<int:id>/', MyAPIView.as_view(), name='my_api_detail'),
]
