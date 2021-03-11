from django.urls import path
from membros.views.views import jovem, jovens, jovensForm, jovenUpdate, jovemDelete, mocidade, mocidadelista
from membros.views.filter import filtrocategoria, categoriafiltro,jovem_search,jovens_ministerio_musica,jovens_ministerio_integracao,jovens_ministerio_estudo,jovens_ministerio_oracao


urlpatterns = [

    path('jovens/', jovens, name='jovens'),
    path('jovem/<int:jovem_id>', jovem, name='jovem'),
    path('jovens/', jovem_search, name='jovem_search'),
    path('jovemcreate/', jovensForm, name='jovemcreate'),
    path('jovemAtualizar/<int:jovem_id>', jovenUpdate, name='jovemAtualizar'),
    path('jovemDeletar/<int:jovem_id>', jovemDelete, name='jovemDeletar'), 

    path('mocidade/', mocidade, name='mocidade'),
    path('mocidade/<int:igreja_id>', mocidadelista, name='mocidadelista'),
    path('categoria_search/', filtrocategoria, name='filtrocategoria'),
    path('categoria/<int:categoria_id>', categoriafiltro, name='categoriafiltro'),

    path('igreja/<int:igreja_id>/celulas/ministerio_musica/<int:celula_id>/detalhes/jovens', jovens_ministerio_musica, name='jovens_ministerio_musica'),
    path('igreja/<int:igreja_id>/celulas/ministerio_oracao/<int:celula_id>/detalhes/jovens', jovens_ministerio_oracao, name='jovens_ministerio_oracao'),
    path('igreja/<int:igreja_id>/celulas/ministerio_integracao/<int:celula_id>/detalhes/jovens', jovens_ministerio_integracao, name='jovens_ministerio_integracao'),
    path('igreja/<int:igreja_id>/celulas/ministerio_estudo/<int:celula_id>/detalhes/jovens', jovens_ministerio_estudo, name='jovens_ministerio_estudo'),

]