from django.urls import path
from . import views

app_name = 'cadastros' 

urlpatterns = [
    path('', views.empresas, name='empresas'),
    path('criar/', views.cadastros, name='cadastros'),
    path('criar_empresas', views.criar_empresa, name='criar_empresa'),
    path('empresa_editar/<int:id>/', views.empresa_editar, name='empresa_editar'),
    path('listar_cnpj', views.listar_cnpj, name='listar_cnpj'),
    path('deletar_cnpj/<int:id>/', views.deletar_cnpj, name='deletar_cnpj'),
    path('deletar_empresa/<int:id>/', views.deletar_empresa, name='deletar_cnpj'),

]
