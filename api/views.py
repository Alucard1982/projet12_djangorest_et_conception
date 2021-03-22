from django.shortcuts import render

# Create your views here.
from django.http import Http404

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from api.models import User, Client, Contrat, Event
from api.permissions import IsGestionnaire, IsSalerGestionClient, IsSupportGestionEvent
from api.serializers import UserSerializer, MyRegisterSerializer, ClientSerializer, ContratSerializer, EventSerializer

from rest_auth.registration.views import RegisterView


class CustomRegisterView(RegisterView):
    serializer_class = MyRegisterSerializer
    permission_classes = [IsGestionnaire, IsAuthenticated]


class UserListView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsGestionnaire, IsAuthenticated]
    try:
        queryset = User.objects.all()
    except User.DoesNotExist:
        raise Http404


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsGestionnaire, IsAuthenticated]
    serializer_class = UserSerializer

    try:
        queryset = User.objects.all()
    except User.DoesNotExist:
        raise Http404


class ClientListView(generics.ListAPIView):
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]
    try:
        queryset = Client.objects.all()
    except Client.DoesNotExist:
        raise Http404


class ClientCreateView(generics.CreateAPIView):
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated, IsSalerGestionClient]
    try:
        queryset = Client.objects.all()
    except Client.DoesNotExist:
        raise Http404


class ClientDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsSalerGestionClient]
    serializer_class = ClientSerializer

    try:
        queryset = Client.objects.all()
    except Client.DoesNotExist:
        raise Http404


class ContratListView(generics.ListAPIView):
    serializer_class = ContratSerializer
    permission_classes = [IsAuthenticated]
    try:
        queryset = Contrat.objects.all()
    except Contrat.DoesNotExist:
        raise Http404


class ContratCreateView(generics.CreateAPIView):
    serializer_class = ContratSerializer
    permission_classes = [IsAuthenticated, IsSalerGestionClient]
    try:
        queryset = Contrat.objects.all()
    except Contrat.DoesNotExist:
        raise Http404

    def perform_create(self, serializer):
        serializer.save(saler=self.request.user)


class ContratDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ContratSerializer
    permission_classes = [IsAuthenticated, IsSalerGestionClient]
    try:
        queryset = Contrat.objects.all()
    except Contrat.DoesNotExist:
        raise Http404


class ContratByClientListView(generics.ListAPIView):
    serializer_class = ContratSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        """override le queryset"""

        id_client = self.kwargs.get('pk')
        try:
            return Contrat.objects.filter(client=id_client)
        except Contrat.DoesNotExist:
            raise Http404


class EventListView(generics.ListAPIView):
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]
    try:
        queryset = Event.objects.all()
    except Event.DoesNotExist:
        raise Http404


class EventCreateView(generics.CreateAPIView):
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated, IsSalerGestionClient]
    try:
        queryset = Event.objects.all()
    except Event.DoesNotExist:
        raise Http404


class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated, IsSupportGestionEvent]
    try:
        queryset = Event.objects.all()
    except Event.DoesNotExist:
        raise Http404


class EventByClientListView(generics.ListAPIView):
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        """override le queryset"""

        id_client = self.kwargs.get('pk')
        try:
            return Event.objects.filter(client=id_client)
        except Event.DoesNotExist:
            raise Http404
