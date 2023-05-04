from django.contrib import admin
from .models import Cliente, Car, Aluguel


# Register your models here.

admin.site.register(Cliente)
admin.site.register(Car)
admin.site.register(Aluguel)