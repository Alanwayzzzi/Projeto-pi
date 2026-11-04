import secrets
from django.conf import settings
from django.db import models


def gerar_codigo():
    "Código curto que os colegas usam para entrar na sala (ex.: 'a3f9c1')."
    return secrets.token_hex(3)


class Sala(models.Model):
    nome = models.CharField("nome da sala", max_length=80)
    descricao = models.CharField("descrição", max_length=200, blank=True)
    criador = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="salas_criadas",
    )
    membros = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="salas",
        blank=True,
    )
    codigo = models.CharField(max_length=12, unique=True, default=gerar_codigo)
    criada_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-criada_em"]

    def __str__(self):
        return self.nome

    @property
    def cor_indice(self):
        """Escolhe uma das 6 cores do banner (estilo Google Sala de Aula)."""
        return self.pk % 6 if self.pk else 0


class Objeto(models.Model):
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE, related_name="objetos")
    nome = models.CharField("objeto", max_length=100)
    descricao = models.TextField("descrição", blank=True)
    local_encontrado = models.CharField("onde foi encontrado", max_length=100, blank=True)
    adicionado_por = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="objetos_adicionados",
    )
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-criado_em"]

    def __str__(self):
        return f"{self.nome} ({self.sala})"
