from django.contrib import admin
from .models import Receita
# Register your models here.


class ListandoReceitas(admin.ModelAdmin):
    list_display =('id','nome_receita','categoria') # adicionar oq sera mostrado no admin
    list_display_links = ('id','nome_receita')  # deixar clicavel 
    search_fields = ('nome_receita',) # Fazer o sistema de pesquisa nescesario ter uma , no final
    list_filter = ('categoria',) #filtrar por alguma coisa  nescesario ter uma , no final
    list_per_page = 2 # dados por pagina
admin.site.register(Receita,ListandoReceitas)