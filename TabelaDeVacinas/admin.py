from django.contrib import admin

# Register your models here.

from .models import Tabela_Disponibilidade
from .models import Tabela_Funcionamento

admin.site.register(Tabela_Disponibilidade)
admin.site.register(Tabela_Funcionamento)