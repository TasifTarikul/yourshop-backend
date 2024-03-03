from django.utils.translation import gettext_lazy as _

O_PENDING = 1
O_CONFIRMED = 2
O_DELIVERED = 3

ORDER_STATUS = (
    (O_PENDING, _('Pending')),
    (O_CONFIRMED, _('Confirmed')),
    (O_DELIVERED, _('Delivered')),
)