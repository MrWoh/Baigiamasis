from django.urls import path
from .views import (
    send_order_email,

)

urlpatterns = [
    path('order_success/<int:order_id>/<int:supplier_id>/',
         send_order_email, name='order_success'),
]
