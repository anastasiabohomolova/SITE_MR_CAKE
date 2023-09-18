from django.urls import path
from cake.views import *
from django.conf import settings
from django.conf.urls.static import static


#сторінки аплікації cake#

app_name = 'cake'

urlpatterns = [
    path('', home_page),
    path('details/<int:id>/', page_details, name='page_details'),
    path('kids_cakes/', page_kids, name='page_kids'),
    path('wedding_cakes/', page_wedding, name='page_wedding'),
    path('bithday_cakes/', page_birthday, name='page_birthday'),
    path('corporate_cakes/', page_corporate, name='page_corporate'),
    path('cake_pops/', page_cake_pops, name='page_cake_pops'),
    path('macaroons/', page_macaroons, name='page_macaroons'),
    path('cake_filling/', page_filling, name='page_filling'),
    path('order_cake/', page_order, name='page_order'),
    path('page_company/', page_company, name='page_company')

]