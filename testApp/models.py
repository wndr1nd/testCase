from django.db import models


class Categories(models.Model):
    category = models.CharField(max_length=100, verbose_name="Категория")
    description = models.CharField(max_length=100, verbose_name="Расшифровка")
    name = models.CharField(max_length=100, verbose_name="Название", null=True)

    def __str__(self):
        return self.name


class CPU(models.Model):
    name = models.TextField(max_length=100, verbose_name="Наименование")
    core = models.IntegerField(verbose_name="Общее колличество ядер")
    frequency = models.FloatField(verbose_name="Базовая частота процессора ГГц")
    price = models.FloatField(verbose_name="Цена")

    def __str__(self):
        return self.name


class RAM(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    type = models.CharField(max_length=100, verbose_name="Тип памяти")
    frequency = models.IntegerField(verbose_name="Тактовая частота МГц")
    price = models.FloatField(verbose_name="Цена")

    def __str__(self):
        return self.name


class Monitor(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    diagonal = models.FloatField(verbose_name="Диагональ экрана")
    matrix = models.CharField(max_length=100, verbose_name="Технология изготовления матрицы")
    price = models.FloatField(verbose_name="Цена")

    def __str__(self):
        return self.name


class SoundCard(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    model = models.CharField(max_length=100, verbose_name="Модели ЦАП")
    capacity = models.IntegerField(verbose_name="Разрядность АЦП")
    price = models.FloatField(verbose_name="Цена")

    def __str__(self):
        return self.name
