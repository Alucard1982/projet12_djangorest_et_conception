from django.contrib import admin

# Register your models here.
from django.contrib import admin
from api.models import Role, Status, User, Client, Contrat, Event


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_time')


class ClientAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'email', 'phone')


class ContratAdmin(admin.ModelAdmin):
    list_display = ('decription', 'amount', 'created_time')


admin.site.register(Role)
admin.site.register(Status)
admin.site.register(User)
admin.site.register(Client, ClientAdmin)
admin.site.register(Contrat, ContratAdmin)
admin.site.register(Event, EventAdmin)
