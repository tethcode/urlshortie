from django.urls import path
from .views import shorten_url, redirect_url
from django.http import JsonResponse

def home(request):
    return JsonResponse({"message": "URL Shortener API is working!"})

urlpatterns = [
    path("", home),
    path("api/shorten/", shorten_url, name="api-shorten"),
    path("<str:short_code>/", redirect_url, name="redirect")
]
