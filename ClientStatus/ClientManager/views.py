from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required

from ClientManager.forms import UserLoginForm


# Create your views here.

class BaseView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'client.html')


class LoginUser(LoginView):
    form_class = UserLoginForm
    template_name = 'login.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        return response


@login_required
def main_page(request):
    return render(request, 'client.html')
