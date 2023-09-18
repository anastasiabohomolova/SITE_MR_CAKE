from django.contrib import admin
from purchase.models import Purchase


class PurchaseModelAdmin(admin.ModelAdmin): #модель в адмінці оформлених замовлень#
    list_display = ('Телефон', 'ПІБ', 'Назва_торта', 'Адреса', 'Категорія', 'Начинка', 'Вага', 'Побажання') #інформацію цих категорії бачимо одразу#
    list_display_links = ('ПІБ', ) #посилання за ФІО#
    list_editable = ('Телефон', ) #одразу можна змінити телефон#
    list_filter = ('ПІБ', 'Назва_торта', 'update') #фільтрація замовлень за цими категоріями#
    search_fields = ['ПІБ', 'Назва_торта'] #пошук замовлень за цими категоріями#

admin.site.register(Purchase, PurchaseModelAdmin)
