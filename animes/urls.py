from django.urls import path

from django.urls import path
from .views import AnimeListView, AnimeDetailView, AnimeCreateView, AnimeUpdateView, AnimeDeleteView

urlpatterns = [
    path('', AnimeListView.as_view(), name='anime_list'),
    path('<int:pk>/', AnimeDetailView.as_view(), name='anime_detail'),
    path('create/', AnimeCreateView.as_view(), name='anime_create'),
    path('<int:pk>/update/', AnimeUpdateView.as_view(), name='anime_update'),
    path('<int:pk>/delete/', AnimeDeleteView.as_view(), name='anime_delete'),
]
