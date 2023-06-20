from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Anime
from django.contrib.auth import get_user_model


class AnimeTests(TestCase):
    def test_list_page_status_code(self):
        url = reverse("anime_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_list_page_template(self):
        url = reverse("anime_list")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "anime/anime-list.html")
        self.assertTemplateUsed(response, "_base.html")

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test", email="teas@email.com", password="1234"
        )

        self.anime = Anime.objects.create(
            title="test", description="test info", added_by=self.user
        )

    def test_str_method(self):
        self.assertEqual(str(self.anime), "test")

    def test_detail_view(self):
        url = reverse("anime_detail", args=[self.anime.pk])
        response = self.client.get(url)
        self.assertTemplateUsed(response, "anime/anime-detail.html")

    def test_create_view(self):
        obj = {
            "title": "test2",
            "description": "info...",
            "image": "url",
            "added_by": self.user.pk,
        }

        url = reverse("anime_create")
        response = self.client.post(path=url, data=obj, follow=True)
        self.assertRedirects(response, reverse("anime_detail", args=[2]))
