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


class CPUViewSet(CategoriesViewSet):
    queryset = CPU.objects.all()
    serializer_class = CPUSerializer


class RAMViewSet(CategoriesViewSet):
    queryset = RAM.objects.all()
    serializer_class = RAMSerializer


class MonitorViewSet(CategoriesViewSet):
    queryset = Monitor.objects.all()
    serializer_class = MonitorSerializer


class SoundCardViewSet(CategoriesViewSet):
    queryset = SoundCard.objects.all()
    serializer_class = SoundCardSerializer
