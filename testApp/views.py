from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from testApp.permissions import AdminOrReadOnly
from testApp.serializers import CPUSerializer, MonitorSerializer, RAMSerializer, SoundCardSerializer, \
    CategoriesSerializer
from testApp.models import Categories, CPU, RAM, Monitor, SoundCard


class CategoriesViewSet(viewsets.ModelViewSet):
    permission_classes = (AdminOrReadOnly,)
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'


class CPUViewSet(viewsets.ModelViewSet):
    permission_classes = (AdminOrReadOnly,)
    queryset = CPU.objects.all()
    serializer_class = CPUSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'


class RAMViewSet(viewsets.ModelViewSet):
    permission_classes = (AdminOrReadOnly,)
    queryset = RAM.objects.all()
    serializer_class = RAMSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'


class MonitorViewSet(viewsets.ModelViewSet):
    permission_classes = (AdminOrReadOnly,)
    queryset = Monitor.objects.all()
    serializer_class = MonitorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'


class SoundCardViewSet(viewsets.ModelViewSet):
    permission_classes = (AdminOrReadOnly,)
    queryset = SoundCard.objects.all()
    serializer_class = SoundCardSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'
