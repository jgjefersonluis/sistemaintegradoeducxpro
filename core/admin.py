from django.contrib import admin
from .models import Pesquisa, Tele
# Register your models here.

@admin.register(Pesquisa)
class PesquisaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'idade', 'telefone', 'responsavel', 'pesquisador')


@admin.register(Tele)
class TeleAdmin(admin.ModelAdmin):
    list_display = ('nome', 'idade', 'telefone', 'responsavel', 'pesquisador',
                    'parentesco', 'escola', 'turno')

