from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import ObjetoForm, SalaForm
from .models import Objeto, Sala


def bem_vindo(request):
    return render(request, "bem_vindo.html")


def cadastro(request):
    form = UserCreationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        usuario = form.save()
        login(request, usuario)
        return redirect("salas")
    return render(request, "registration/cadastro.html", {"form": form})


@login_required
def salas(request):
    """Salas das quais o usuário faz parte (criadas por ele ou em que entrou)."""
    return render(request, "salas.html", {"salas": request.user.salas.all()})


@login_required
@require_POST
def sala_criar(request):
    form = SalaForm(request.POST)
    if form.is_valid():
        sala = form.save(commit=False)
        sala.criador = request.user
        sala.save()
        sala.membros.add(request.user)
        messages.success(request, f"Sala “{sala.nome}” criada.")
        return redirect("sala_detalhe", pk=sala.pk)
    messages.error(request, "Não foi possível criar a sala. Confira o nome.")
    return redirect("salas")


@login_required
@require_POST
def sala_entrar(request):
    codigo = request.POST.get("codigo", "").strip().lower()
    try:
        sala = Sala.objects.get(codigo=codigo)
    except Sala.DoesNotExist:
        messages.error(request, "Nenhuma sala encontrada com esse código.")
        return redirect("salas")
    sala.membros.add(request.user)
    messages.success(request, f"Você entrou em “{sala.nome}”.")
    return redirect("sala_detalhe", pk=sala.pk)


@login_required
def sala_detalhe(request, pk):
    sala = get_object_or_404(request.user.salas, pk=pk)
    return render(
        request,
        "sala_detalhe.html",
        {
            "sala": sala,
            "objetos": sala.objetos.select_related("adicionado_por"),
            "eh_dono": sala.criador_id == request.user.id,
        },
    )


@login_required
@require_POST
def objeto_adicionar(request, pk):
    sala = get_object_or_404(request.user.salas, pk=pk)
    if sala.criador_id != request.user.id:
        return HttpResponseForbidden("Só quem criou a sala pode adicionar objetos.")
    form = ObjetoForm(request.POST)
    if form.is_valid():
        objeto = form.save(commit=False)
        objeto.sala = sala
        objeto.adicionado_por = request.user
        objeto.save()
        messages.success(request, "Objeto adicionado.")
    else:
        messages.error(request, "Informe o nome do objeto.")
    return redirect("sala_detalhe", pk=sala.pk)


@login_required
@require_POST
def objeto_excluir(request, pk):
    objeto = get_object_or_404(Objeto, pk=pk)
    if objeto.sala.criador_id != request.user.id:
        return HttpResponseForbidden("Só quem criou a sala pode excluir objetos.")
    sala_pk = objeto.sala_id
    objeto.delete()
    messages.success(request, "Objeto excluído.")
    return redirect("sala_detalhe", pk=sala_pk)


@login_required
def perfil(request):
    return render(request, "perfil.html")
