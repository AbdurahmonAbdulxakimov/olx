from django.conf import settings
from django.urls import path
from rest_framework.routers import DefaultRouter, SimpleRouter

from users.api.views import UserViewSet
from post.views import PostAPIView, VipPostsAPIView
from common.views import ChapterAPIView

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)



app_name = "api"

urlpatterns = [
    path('posts/', PostAPIView.as_view()),
    path('posts/vip/', VipPostsAPIView.as_view()),
    path('posts/<int:pk>/', VipPostsAPIView.as_view()),
    
    path('chapters/', ChapterAPIView.as_view()),
]

urlpatterns += router.urls
