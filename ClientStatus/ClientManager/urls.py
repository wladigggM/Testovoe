from django.urls import path

from ClientManager.views import BaseView

urlpatterns = [
    path('', BaseView.as_view())
]
