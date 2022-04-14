from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from comments.views import *


router = routers.DefaultRouter()
router.register(r'articles', ArticleViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
]
