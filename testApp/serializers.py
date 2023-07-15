from rest_framework import serializers
from testApp.models import Categories, CPU, RAM, Monitor, SoundCard


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'


class CPUSerializer(serializers.ModelSerializer):
    class Meta:
        model = CPU
        fields = '__all__'


class RAMSerializer(serializers.ModelSerializer):
    class Meta:
        model = RAM
        fields = '__all__'


class MonitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monitor
        fields = '__all__'


class SoundCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoundCard
        fields = '__all__'
