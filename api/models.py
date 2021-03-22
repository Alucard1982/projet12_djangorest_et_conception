from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class Role(models.Model):
    type = models.CharField(max_length=128)


class User(AbstractUser):
    email = None
    role = models.ForeignKey(to=Role, on_delete=models.CASCADE)
    is_staff = True


class Client(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(max_length=128)
    phone = models.CharField(max_length=128, unique=True)
    compagny_name = models.CharField(max_length=128)
    client_contrat = models.BooleanField()


class Contrat(models.Model):
    decription = models.CharField(max_length=128)
    amount = models.FloatField()
    payment_due = models.DateField()
    created_time = models.DateTimeField(auto_now_add=True)
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE, related_name="contrats")
    saler = models.ForeignKey(to=User, on_delete=models.DO_NOTHING, related_name="salers")


class Status(models.Model):
    type = models.CharField(max_length=128)


class Event(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=128)
    date_event = models.DateField()
    created_time = models.DateTimeField(auto_now_add=True)
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE, related_name='events')
    support = models.ForeignKey(to=User, on_delete=models.DO_NOTHING)
    status = models.ForeignKey(to=Status, on_delete=models.DO_NOTHING)
    contrat = models.OneToOneField(to=Contrat, on_delete=models.CASCADE)
from django.db import models

# Create your models here.
