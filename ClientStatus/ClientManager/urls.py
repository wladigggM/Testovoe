from django.contrib.auth.views import LogoutView
from django.urls import path

from ClientManager.views import LoginUser, DataSynthesizer, Index, ClientsTableView, ClientView

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('synthesizer/', DataSynthesizer.as_view(), name='synthesizer'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('clients-table/', ClientsTableView.as_view(), name='clients-table'),
    path('clients-table/id/<int:client_id>', ClientView.as_view(), name='client')
]
