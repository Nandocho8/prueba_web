from _noticias.models import Noticias
from rest_framework import serializers


class NoticiasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Noticias
        fields = '__all__'
