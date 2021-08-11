from django.urls import path
from .views import (
    AppnomiListView,
    AppnomiDetailView,
    AppnomiCreateView,
    AppnomiUpdateView,
    AppnomiDeleteView,
)

urlpatterns = [
    path('post/<int:pk>/delete/', AppnomiDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/edit/', AppnomiUpdateView.as_view(), name='post_edit'),
    path('post/new/', AppnomiCreateView.as_view(), name='post_new'),
    path('', AppnomiListView.as_view(), name='home'),
    path('post/<int:pk>/', AppnomiDetailView.as_view(), name='post_detail'),
]