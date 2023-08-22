from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['usuario', 'nombre', 'email', 'direccion' ,'producto', 'cantidad', 'metodo_pago', 'estado_pedido']

# class ModifyOrderForm(forms.ModelForm):
#     class Meta:
#         model = Order
#         fields = ['estado']
