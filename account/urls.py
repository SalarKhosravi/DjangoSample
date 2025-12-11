
from django.urls import path
from .views import TestApiView, github_update_webhook

urlpatterns = [
    path("github-update/", github_update_webhook, name="github-update"),

    path('test/', TestApiView.as_view(), name='test-api'),
]





