from django.urls import path

from . views import SetWebhookView,CallbackView


urlpatterns = [
    path('set/', SetWebhookView.as_view()),
    path('callback/', CallbackView.as_view()),
]