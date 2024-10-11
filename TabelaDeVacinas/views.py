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

def lista_ubs_vacinas(request):
    ubs_vacinas = UBSVacinas.objects.select_related('ubs', 'vacina').all()
    return render(request, 'lista_ubs_vacinas.html', {'ubs_vacinas': ubs_vacinas})

def buscar_disponibilidade(request):
    search_query = request.GET.get('search_query', '')
    tabelas = Tabela_Disponibilidade.objects.all()
    if search_query:
        from django.db.models import Q
        tabelas = tabelas.filter(Q(nome_ubs__icontains=search_query) | Q(nome_vacina__icontains=search_query))
    return render(request, 'search.html', {'tabelas': tabelas})

def more_info(request):
    tabelas = Tabela_Funcionamento.objects.all().order_by('nome_ubs')
    return render(request, 'more_info.html', {'tabelas': tabelas})

def buscar_horario(request):
    nome_ubs = request.GET.get('nome_ubs', '')
    tabelas = Tabela_Funcionamento.objects.filter(nome_ubs__icontains=nome_ubs)
    return render(request, 'more_info.html', {'tabelas': tabelas})
