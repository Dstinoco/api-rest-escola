from rest_framework import generics, status, viewsets, mixins
from rest_framework.generics import get_object_or_404
from rest_framework import permissions

from rest_framework.decorators import action
from rest_framework.response import Response 

from cursos.models import Curso, Avaliacao
from cursos.serializer import CursoSerializer, AvaliacaoSerializer
from cursos.permissions import EhSuperUser


"""
API V1
"""

#CURSOS  #CURSOS  #CURSOS  #CURSOS  #CURSOS  

class CursosAPIView(generics.ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class CursoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer    



#Avaliações  #Avaliações  #Avaliações  #Avaliações  #Avaliações  



class AvaliacoesAPIView(generics.ListCreateAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    def get_queryset(self):
        if self.kwargs.get('curso_pk'):
            return self.queryset.filter(curso_id=   self.kwargs.get('curso_pk'))
        return self.queryset.all()



class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    def get_object(self):
        if self.kwargs.get('curso_pk'):
            return get_object_or_404(self.get_queryset(), curso_id=self.kwargs.get('curso_pk'), pk=self.kwargs.get('avaliacao_pk'))
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get("avaliacao_pk"))


"""
API V2
"""

class CursoViewSet(viewsets.ModelViewSet):
    permission_classes = (
        
        permissions.DjangoModelPermissions, )
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

    @action(detail=True, methods=['get'])
    def avaliacoes(self, request,  pk=None):
        self.pagination_class.page_size = 1
        avaliacoes = Avaliacao.objects.filter(curso_id=pk)
        page = self.paginate_queryset(avaliacoes)

        if page is not None:
            serialize = AvaliacaoSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)


class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer





class Avaliacao(mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin, 
                mixins.UpdateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer