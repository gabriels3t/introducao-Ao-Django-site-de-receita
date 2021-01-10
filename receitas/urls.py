from django.urls import path

from . import views

urlpatterns =[
    path('',views.index,name='index'),
    path('receita',views.receita,name='receita')
]
#  path('nome que eu quero da url',views.Pagina q eu quero chamar
# ,name='nomedapaginaigual do html')