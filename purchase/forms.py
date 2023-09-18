from django import forms
from purchase.models import Purchase


class PurchaseForm(forms.ModelForm): #формочка для оформлення замовлення покупцям#
    class Meta:
        model = Purchase
        fields = [
            'ПІБ',
            'Адреса',
            'Телефон',
            'Назва_торта',
            'Категорія',
            'Начинка',
            'Вага',
            'Побажання'
        ]