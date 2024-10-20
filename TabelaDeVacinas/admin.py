from django.contrib import admin

# Register your models here.
from .models import UBSVacina
from .models import TabelaFuncionamento

admin.site.register(UBSVacina)
admin.site.register(TabelaFuncionamento)
