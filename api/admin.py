from django.contrib import admin

# Register your models here.
from django.contrib import admin
from api.models import Role, Status, User, Client, Contrat, Event

admin.site.register(Role)
admin.site.register(Status)
admin.site.register(User)
admin.site.register(Client)
admin.site.register(Contrat)
admin.site.register(Event)