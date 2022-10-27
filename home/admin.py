from django.contrib import admin

from home.models import Cidade, Detalhes


class CidadeAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')


class DetCidadeAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'nome', 'nullable',
        'dataFundacao', 'populacaoEstimada',
        'altitude'
    )


admin.site.register(Cidade, CidadeAdmin)
admin.site.register(Detalhes, DetCidadeAdmin)
