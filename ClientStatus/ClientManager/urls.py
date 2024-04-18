from django.contrib.auth.views import LogoutView
from django.urls import path

from ClientManager.views import BaseView, LoginUser

urlpatterns = [
    path('', BaseView.as_view()),
    path('/login/', LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
