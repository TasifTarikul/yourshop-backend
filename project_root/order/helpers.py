import random
import string

from .models import Order

def generate_order_id():
    generated_num = "".join(random.choices(string.digits, k=10))
    qs = Order.objects.filter(order_number=generated_num)
    if qs.exists():
        generate_order_id()
    return generated_num
