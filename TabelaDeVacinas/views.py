from django.shortcuts import render
from .models import UBS, Vacina, UBSVacina

# Views

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def search(request):
    tabelas = UBSVacina.objects.select_related('ubs', 'vacina').order_by('ubs__nome_ubs', 'vacina__nome_vacina')
    return render(request, 'search.html', {'tabelas': tabelas})

def buscar_disponibilidade(request):
    query = request.GET.get('search_query', '')  # Obtém a consulta de pesquisa
    ubs_vacinas = UBSVacina.objects.select_related('ubs', 'vacina')

    if query:  # Se a consulta não estiver vazia
        ubs_vacinas = ubs_vacinas.filter(ubs__nome_ubs__icontains=query)

    return render(request, 'search.html', {'ubs_vacinas': ubs_vacinas})

def buscar_horario(request):
    nome_ubs = request.GET.get('nome_ubs', '')
    tabelas = UBSVacina.objects.filter(ubs__nome_ubs__icontains=nome_ubs)
    return render(request, 'more_info.html', {'tabelas': tabelas})
