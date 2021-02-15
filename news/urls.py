from django.urls import path
from .views import PostList, SoloPost, PostSearch

urlpatterns = [
    path('', PostList.as_view()),
    path('search', PostSearch.as_view()),
    path('<int:pk>', SoloPost.as_view()),
]