from django.shortcuts import render
from .models import UBS, Vacinas, UBSVacinas

# Views

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def search(request):
    tabelas = Tabela_Disponibilidade.objects.all().order_by('nome_ubs', 'nome_vacina')
    return render(request, 'search.html', {'tabelas': tabelas})

def buscar_disponibilidade(request):
    ubs_vacinas = UBSVacinas.objects.select_related('ubs', 'vacina').all()
    return render(request, 'lista_ubs_vacinas.html', {'ubs_vacinas': ubs_vacinas})
