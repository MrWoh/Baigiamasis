from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from order_manager.models import Order
from supplier_manager.models import MySupplier


def send_order_email(request, order_id, supplier_id):
    user_email = request.user.email

    supplier = get_object_or_404(MySupplier, id=supplier_id)
    order = get_object_or_404(Order, id=order_id)

    html_content = render_to_string('order_success.html', {
        'order': order, 'supplier': supplier,
    })
    text_content = strip_tags(html_content)

    email = EmailMultiAlternatives(
        order.order_name,
        text_content,
        user_email,
        [supplier.email, ],
    )
    email.attach_alternative(html_content, "text/html")
    email.send()
    messages.info(request, "Email was sent successfully")
    return redirect(reverse('my_order'))
