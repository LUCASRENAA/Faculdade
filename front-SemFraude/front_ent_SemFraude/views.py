from random import random

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth.decorators import user_passes_test

def check_admin(user):
   return user.is_superuser



@user_passes_test(check_admin)
def index(request):
    return render(request, "front_ent_SemFraude/index.html")
@user_passes_test(check_admin)

def lote(request):
    return render(request, "front_ent_SemFraude/lote.html")

@user_passes_test(check_admin)

def orgaoDonatario(request):
    return render(request, "front_ent_SemFraude/orgaoDonatario.html")
@user_passes_test(check_admin)

def orgaoFiscalizador(request):
    return render(request, "front_ent_SemFraude/orgaoFiscalizador.html")
@user_passes_test(check_admin)

def produto(request):
    return render(request, "front_ent_SemFraude/produto.html")


def site(request):
    return render(request, "front_ent_SemFraude/telainicial.html")

def semfraude(request):
    return render(request, "front_ent_SemFraude/semfraude.html")

@user_passes_test(check_admin)

def visualizar(request,classe):
    return render(request, "front_ent_SemFraude/Visualizar_Itens.html",{"classe":classe})

@csrf_exempt
def json_example(request):
    data = {
        'name': 'Vitor',
        'location': 'Finland',
        'is_active': True,
        'count': 28
    }
    dump = json.dumps(data)
    return HttpResponse(dump, content_type='application/json')

def json_example2(request):
    vetor  = []
    data = {
        'id': 1,
        'name': 'Vitor',
        'location': 'Finland',
        'is_active': True,
        'count': 28
    }
    vetor.append(data)
    data = {
        'id': 2,
        'name': 'Vitor2',
        'location': 'Finlan2d',
        'is_active': True,
        'count': 28
    }

    vetor.append(data)
    
    dump = json.dumps(vetor)
    return HttpResponse(dump, content_type='application/json')
