from django.contrib import admin
from estacionamento.models import Carro, Cliente, Vendedor, Fornecedo, Seguranca, Vagas
# Register your models here.

admin.site.register(Carro)
admin.site.register(Cliente)
admin.site.register(Vendedor)
admin.site.register(Fornecedo)
admin.site.register(Seguranca)
admin.site.register(Vagas)
