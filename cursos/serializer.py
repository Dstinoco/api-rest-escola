from rest_framework import serializers
from cursos.models import Curso, Avaliacao
from django.db.models import Avg

class AvaliacaoSerializer(serializers.ModelSerializer):

    

    class Meta:
        extra_kargs = {
            'email': {'write_only': True}
        }

        model = Avaliacao
        fields = ('id', 'curso', 'nome', 'email', 'comentario', 'avaliacao', 'criacao', 'ativo')



    def validate_avaliacao(self, valor):
        if valor in range(1, 6):
            return valor
        raise serializers.ValidationError("A avaliação precisa ser de 1 a 5 apenas")    




class CursoSerializer(serializers.ModelSerializer):

    #lista
    #avaliacoes = AvaliacaoSerializer(many=True, read_only=True)

    #link
    #avaliacoes = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='avaliacao-detail')

    #ID
    avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    media_avaliacoes = serializers.SerializerMethodField()

    class Meta:
        model = Curso
        fields = ('id', 'titulo', 'url', 'criacao', 'ativo', 'avaliacoes', 'media_avaliacoes')    

    def get_media_avaliacoes(self, obj):
        media = obj.avaliacoes.aggregate(Avg('avaliacao')).get('avaliacao__avg')  

        if media is None:
            return 0
        return round(media * 2) / 2    