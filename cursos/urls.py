from django.urls import path
from rest_framework.routers import SimpleRouter
from cursos.views import CursoAPIView, AvaliacaoAPIView, CursosAPIView, AvaliacoesAPIView, AvaliacaoViewSet, CursoViewSet

routers = SimpleRouter()
routers.register('cursos', CursoViewSet)
routers.register('avaliacoes', AvaliacaoViewSet)

urlpatterns = [

path('cursos/', CursosAPIView.as_view(), name='cursos'),
path('cursos/<int:pk>', CursoAPIView.as_view(), name='curso'),
path('cursos/<int:curso_pk>/avaliacoes/', AvaliacoesAPIView.as_view(), name='curso'),
path('cursos/<int:curso_pk>/avaliacoes/<int:avaliacao_pk', AvaliacaoAPIView.as_view(), name='curso'),

path('avaliacoes/', AvaliacoesAPIView.as_view(), name='avaliacoes'),
path('avaliacoes/<int:avaliacao_pk>', AvaliacaoAPIView.as_view(), name='avaliacao'),

]