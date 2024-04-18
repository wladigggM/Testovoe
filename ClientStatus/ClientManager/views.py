from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib.auth.decorators import login_required

from ClientManager.forms import UserLoginForm, ClientStatusForm
from ClientManager.models import Client, User
from ClientManager.utils import generate_client_data, generate_users


# Create your views here.
class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class ClientView(View):
    def get(self, request, client_id):
        client = get_object_or_404(Client, pk=client_id)
        form = ClientStatusForm(instance=client)

        data = {
            'client': client,
            'form': form,
        }
        return render(request, 'client.html', data)

    def post(self, request, client_id):
        client = get_object_or_404(Client, pk=client_id)
        form = ClientStatusForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            messages.success(request, "Статус клиента успешно обновлен!")
            return redirect('../', client_id=client.id)
        else:
            data = {
                'client': client,
                'form': form,
            }
            return render(request, 'client.html', data)


class ClientsTableView(View):
    def get(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            my_client = Client.objects.filter(responsible_person=request.user)
        else:
            my_client = {''}
        data = {
            'my_client': my_client,
        }
        return render(request, 'clients.html', data)


class DataSynthesizer(View):
    def get(self, request, *args, **kwargs):

        """ ДЛЯ ГЕНЕРАЦИИ 5-ти юзеров и по 1 клиенту на каждого юзера """

        new_client_list = generate_client_data(5)

        for client_data in new_client_list:
            Client.objects.create(
                acc_num=client_data['acc_num'],
                last_name=client_data['last_name'],
                first_name=client_data['first_name'],
                middle_name=client_data['middle_name'],
                birth_date=client_data['birth_date'],
                tax_id=client_data['tax_id'],
                responsible_person=client_data['responsible_person']
            )
        return render(request, 'synthesizer.html')


class LoginUser(LoginView):
    form_class = UserLoginForm
    template_name = 'login.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        return response


@login_required
def main_page(request):
    return render(request, 'base.html')
