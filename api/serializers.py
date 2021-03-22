from rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from api.models import User, Role, Client, Contrat, Event, Status
from django.contrib.auth.validators import UnicodeUsernameValidator


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ('id', 'type')


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('id', 'type')


class MyRegisterSerializer(RegisterSerializer):
    tab_role = []
    roles = Role.objects.all()
    for role in roles:
        tab_role.append(role.id)

    role_id = serializers.ChoiceField(choices=tab_role)

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'email': self.validated_data.get('email', ''),
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            'role_id': self.validated_data.get('role_id', ''),
        }


class UserSerializer(serializers.ModelSerializer):
    role = RoleSerializer(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'role')
        extra_kwargs = {
            'username': {
                'validators': [UnicodeUsernameValidator()],
            }
        }


class ContratSerializer(serializers.ModelSerializer):
    saler = UserSerializer(read_only=True)
    client = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Client.objects.all())

    class Meta:
        model = Contrat
        fields = ('id', 'decription', 'amount', 'payment_due', 'created_time', 'saler', 'client')


class EventSerializer(serializers.ModelSerializer):
    support = serializers.PrimaryKeyRelatedField(queryset=User.objects.filter(role__type="support"))
    status = StatusSerializer()
    support = UserSerializer()
    client = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Client.objects.all())

    class Meta:
        model = Event
        fields = ('id', 'title', 'description', 'date_event',
                  'created_time', 'status', 'support', 'client',)

    def create(self, validated_data):
        status_data = validated_data.get("status")
        validated_data["status"] = Status.objects.get(type=status_data['type'])
        support_data = validated_data.get("support")
        validated_data["support"] = User.objects.get(username=support_data['username'])
        event = Event.objects.create(**validated_data)
        return event


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'first_name', 'last_name', 'email', 'phone',
                  'compagny_name', 'client_contrat', 'saler')
