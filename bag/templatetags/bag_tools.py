from django import template
from decimal import Decimal

register = template.Library()

@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    # Check if quantity is a dict and extract the value if necessary
    if isinstance(quantity, dict):
        quantity_value = quantity.get('quantity', 0)  # Default to 0 if 'quantity' is not present
    else:
        quantity_value = quantity
    
    # Ensure quantity_value is a valid number
    if isinstance(quantity_value, (int, float, Decimal)):
        return price * Decimal(quantity_value)
    else:
        raise ValueError("Invalid quantity value: must be int, float, or Decimal")
