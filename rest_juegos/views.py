from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from _juegos.models import Juegos
from .serializers import JuegosSerializer


@csrf_exempt
@api_view(['GET', 'POST'])
def lista_juegos(request):
    if request.method == 'GET':
        juegos = Juegos.objects.all()
        serializer = JuegosSerializer(juegos, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = JuegosSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', "PUT", 'DELETE'])
def detalle_juegos(request, id):
    try:
        juegos = Juegos.objects.get(id=id)
    except Juegos.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = JuegosSerializer(juegos)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser.parse(request)
        serializer = JuegosSerializer(juego, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        juegos.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
