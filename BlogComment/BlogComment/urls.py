from django.contrib import admin
from django.urls import path
from comments.views import ArticleAPIView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/articles/', ArticleAPIView.as_view()),
    path('api/v1/articles/<int:pk>/', ArticleAPIView.as_view()),
]
