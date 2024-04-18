from django.contrib import admin

from ClientManager.models import Client, User


# Register your models here.

class ClientAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'middle_name', 'acc_num', 'birth_date', 'tax_id', 'responsible_person',
                    'status']
    search_fields = ['acc_num', 'last_name', 'first_name', 'middle_name', 'birth_date', 'tax_id', 'responsible_person',
                     'status']
    list_display_links = ['last_name', 'first_name', 'middle_name']


class ClientTabularAdmin(admin.TabularInline):  # Или используйте admin.TabularInline для табличного стиля
    model = Client
    fields = (
        'last_name',
        'first_name',
        'middle_name',
        'acc_num',
        'tax_id',
        'status',
    )
    extra = 0


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'full_name', 'email']
    search_fields = ['username', 'full_name', 'email']
    list_display_links = ['username', 'full_name']

    inlines = (ClientTabularAdmin,)

admin.site.register(User, UserAdmin)
admin.site.register(Client, ClientAdmin)
