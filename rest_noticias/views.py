from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from _noticias.models import Noticias
from .serializers import NoticiasSerializer


@csrf_exempt
@api_view(['GET', 'POST'])
def lista_noticias(request):
    if request.method == 'GET':
        noticias = Noticias.objects.all()
        serializer = NoticiasSerializer(noticias, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = NoticiasSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', "PUT", 'DELETE'])
def detalle_noticias(request, id):
    try:
        noticias = Noticias.objects.get(id=id)
    except Noticias.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = NoticiasSerializer(noticias)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser.parse(request)
        serializer = NoticiasSerializer(juego, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        noticias.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
