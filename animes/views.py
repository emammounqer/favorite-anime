from django.shortcuts import render

# Create your views here.
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Anime


class AnimeListView(ListView):
    template_name = "anime/anime-list.html"
    model = Anime


class AnimeDetailView(DetailView):
    template_name = "anime/anime-detail.html"
    model = Anime


class AnimeCreateView(CreateView):
    template_name = "anime/anime-create.html"
    model = Anime
    fields = ["title", "description", "image", "added_by"]


class AnimeUpdateView(UpdateView):
    template_name = "anime/anime-update.html"
    model = Anime
    fields = ["title", "description", "image", "added_by"]


class AnimeDeleteView(DeleteView):
    template_name = "anime/anime-delete.html"
    model = Anime
    success_url = reverse_lazy("anime_list")
