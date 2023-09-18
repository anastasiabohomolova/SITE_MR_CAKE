from django.contrib import admin
from cake.models import Info, Category, Filling



class InfoModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'min_size', 'type') #ці категорії бачимо на передньому плані#
    list_display_links = ('min_size', ) #посилання цієї категорії на повну інформацї про товар#
    list_editable = ('type', 'name') #ці категорії можна змінити одразу#
    list_filter = ('type', ) #фільтрація товарів за типом#
    search_fields = ['name'] #пошук товару по  його назві#



class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'description') #ці категорії бачимо на передньому плані#
    list_display_links = ('name', ) #посилання цієї категорії на повну інформацї про товар#
    list_editable = ('description', ) #цю категорію можна одразу змінити#
    list_filter = ('name', ) #фільтрація за назвою#
    search_fields = ['name'] #пошук за назвою#


class FillingModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'description') #ці категорії бачимо на передньому плані#
    list_display_links = ('name', ) #посилання цієї категорії на повну інформацї про начинку#
    list_editable = ('description', ) #цю категорію можна одразу змінити#
    list_filter = ('type', ) #фільтрація за назвою#
    search_fields = ['name'] #пошук за назвою#


admin.site.register(Info, InfoModelAdmin)
admin.site.register(Category, CategoryModelAdmin)
admin.site.register(Filling, FillingModelAdmin)








