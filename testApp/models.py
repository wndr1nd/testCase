from django.db import models
from django.utils.translation import gettext as _


class Categories(models.Model):
    category = models.CharField(_("Категория"), max_length=100)
    description = models.CharField(_("Описание"), max_length=100)
    name = models.CharField(_("Название"), max_length=100, null=True)

    def __str__(self):
        return self.name


class CPU(models.Model):
    name = models.TextField(_("Наименование"), max_length=100)
    core = models.IntegerField(_("Общее колличество ядер"))
    frequency = models.FloatField(_("Базовая частота процессора ГГц"))
    price = models.FloatField(_("Цена"))

    def __str__(self):
        return self.name


class RAM(models.Model):
    name = models.CharField(_("Наименование"), max_length=100)
    type = models.CharField(_("Тип памяти"), max_length=100)
    frequency = models.IntegerField(_("Тактовая частота МГц"))
    price = models.FloatField(_("Цена"))

    def __str__(self):
        return self.name


class Monitor(models.Model):
    name = models.CharField(_("Наименование"), max_length=100)
    diagonal = models.FloatField(_("Диагональ экрана"))
    matrix = models.CharField(_("Технология изготовления матрицы"), max_length=100)
    price = models.FloatField(_("Цена"))

    def __str__(self):
        return self.name


class SoundCard(models.Model):
    name = models.CharField(_("Наименование"), max_length=100)
    model = models.CharField(_("Модели ЦАП"), max_length=100)
    capacity = models.IntegerField(_("Разрядность АЦП"))
    price = models.FloatField(_("Цена"))

    def __str__(self):
        return self.name
