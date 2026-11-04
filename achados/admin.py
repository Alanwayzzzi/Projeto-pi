from django.contrib import admin

from .models import Objeto, Sala


@admin.register(Sala)
class SalaAdmin(admin.ModelAdmin):
    list_display = ("nome", "criador", "codigo", "criada_em")


@admin.register(Objeto)
class ObjetoAdmin(admin.ModelAdmin):
    list_display = ("nome", "sala", "local_encontrado", "criado_em")
