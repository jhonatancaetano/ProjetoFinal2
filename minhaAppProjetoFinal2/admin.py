from django.contrib import admin

# Register your models here.


#from .models import postagemcaduser

#admin.site.register(postagemcaduser)

#from .models import postagem

#admin.site.register(postagem)

from .models import TipoDeComida

admin.site.register(TipoDeComida)

from .models import Restaurante

admin.site.register(Restaurante)

from .models import Filial

admin.site.register(Filial)

from .models import Gerente

admin.site.register(Gerente)

from .models import RevisaoDeComentario

admin.site.register(RevisaoDeComentario)

from .models import Comentario

admin.site.register(Comentario)

from .models import ClassificacaoDoItem

admin.site.register(ClassificacaoDoItem)

from .models import ItensDeConsumo

admin.site.register(ItensDeConsumo)

from .models import TipoDeRelacionamento

admin.site.register(TipoDeRelacionamento)

from .models import Usuario

admin.site.register(Usuario)

from .models import Relacionamento

admin.site.register(Relacionamento)

from .models import NivelDeLotacao

admin.site.register(NivelDeLotacao)

from .models import Lotacao

admin.site.register(Lotacao)

from .models import TipoDeIncidenteInterno

admin.site.register(TipoDeIncidenteInterno)

from .models import IncidenteInterno

admin.site.register(IncidenteInterno)

from .models import EventoExterno

admin.site.register(EventoExterno)

from .models import Recomendacao

admin.site.register(Recomendacao)

from .models import AssociacaoFilialEventoExterno

admin.site.register(AssociacaoFilialEventoExterno)

from .models import AssociacaoItemDeConsumoRecomendacao

admin.site.register(AssociacaoItemDeConsumoRecomendacao)

from .models import AssociacaoRestauranteUsuario

admin.site.register(AssociacaoRestauranteUsuario)