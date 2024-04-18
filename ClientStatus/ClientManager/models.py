from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Client(models.Model):
    acc_num = models.CharField(max_length=50, unique=True)
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    tax_id = models.CharField(max_length=12, unique=True)
    responsible_person = models.CharField(max_length=100)
    STATUS_CHOICES = [
        ('Не в работе', 'Не в работе'),
        ('В работе', 'В работе'),
        ('Отказ', 'Отказ'),
        ('Сделка закрыта', 'Сделка закрыта'),
    ]

    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='Не в работе')


class User(AbstractUser):
    full_name = models.CharField(max_length=50)
