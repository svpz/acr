from django.urls import path
from .views import NewsListCreateView, NewsDetailView

urlpatterns = [
    path('api/list/', NewsListCreateView.as_view(), name='news-list-create'),
    path('api/edit/<int:pk>/', NewsDetailView.as_view(), name='news-detail'),
]
