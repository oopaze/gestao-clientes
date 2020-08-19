from django.urls import path
from .views import cadastrar_usuario, ler_usuario, atualizar_usuario, deletar_usuario

urlpatterns = [
    path('', ler_usuario, name='ler_usuario'),
    path('cadastrar/', cadastrar_usuario, name='cadastrar_usuario'),
    path('atualizar/', atualizar_usuario, name='atualizar_usuario'),
    path('deletar/', deletar_usuario, name='deletar_usuario'),
]
