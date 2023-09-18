from django.urls import path
from purchase.views import *
from django.conf import settings
from django.conf.urls.static import static


#сторінки  аплікацї-purchase#

app_name = 'purchase'

urlpatterns = [
    path('', create_order, name='create_order'),

]