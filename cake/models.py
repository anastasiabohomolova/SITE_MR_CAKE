from django.conf import settings
from django.db import models



def type(): #вибірка категорії для товару#
    category = [
        ('Торти на день народження', 'the a birthday'),
        ('Дитячі торти', 'kids'),
        ('Весільні торти', 'wedding'),
        ('Корпоративні торти', 'corporate'),
        ('Кейк-попси', 'cake-pops'),
        ('Макаруни', 'macaroons')
    ]
    return category



def upload_location(instance, filename):
    return f'{instance.id}, {filename}'


class Info(models.Model): #модель про інформацію товарів#
    image = models.ImageField(upload_to=upload_location,
                              null=True,
                              blank=True,
                              height_field='height_field',
                              width_field='width_field') #картинка товару#
    height_field = models.IntegerField(default=0) #висота за замовчуванням картинки#
    width_field = models.IntegerField(default=0) #ширина за замовчуванням картинки#
    name = models.CharField(max_length=30) #назва до 30 символів#
    price = models.CharField(max_length=100) #ціна товару#
    min_size = models.CharField(max_length=30) #мінімальне замовлення#
    type = models.CharField(max_length=30, choices=type(), default='') #категорія товару#

    class Meta:
        ordering = ('name',) #сортування по назві товару#

    def __str__(self):
        return self.name #повертає об'єкт за його назвою#

    def home(self):
        return f'/mr_cake/' #повертає на головну сторінку#

    def get_detail_url(self):
        return f'/mr_cake/details/{self.id}' #повертає сторінку конкретного товару по id#

class Category(models.Model): #модель про категорію товару#
    image = models.ImageField(upload_to=upload_location,
                              null=True,
                              blank=True,
                              height_field='height_field',
                              width_field='width_field') #картинка категорії#
    height_field = models.IntegerField(default=0) #висота за замовчуванням картинки#
    width_field = models.IntegerField(default=0) #ширина за замовчуванням картинки#
    name = models.CharField(max_length=30) #назва категорії до 30 символів#
    description = models.TextField() #опис категорії без обмежень до к-сті символів#

    class Meta:
        ordering = ('name',)  #сортування по назві категорії#

    def __str__(self):
        return self.name  #повертає об'єкт за його назвою#

def type_filling(): #вибірка для начинки#
    category = [
        ('Торти/Поп-кейки', 'cakes/pop-cakes'),
        ('Макаруни', 'macaroons')

    ]
    return category

class Filling(models.Model): #модель начинки товару#
    image = models.ImageField(upload_to=upload_location,
                              null=True,
                              blank=True,
                              height_field='height_field',
                              width_field='width_field') #картинка начинки#
    height_field = models.IntegerField(default=0) #висота за замовчуванням картинки#
    width_field = models.IntegerField(default=0) #ширина за замовчуванням картинки#
    name = models.CharField(max_length=100) #назва начинки#
    description = models.TextField() #опис начинки без обмежень до к-сті символів#
    type = models.CharField(max_length=30, choices=type_filling(), default='')  # категорія начинки#

    def __str__(self):
        return self.name  #повертає об'єкт за його назвою#










