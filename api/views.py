from .serializers import RegionSerializer, FruitSerializer
from .models import Region, Fruit
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


#Decorators que recebe os metodos HTTP
@api_view(['GET', 'POST'])
def region_list(request):
    if request.method == 'GET':
        #Seleciona todos objetos do model Region
        region = Region.objects.all()
        #Serializer funciona como Modelform do django, porém o Serializer retorna em modo JSON
        #O many=True significa que permite o serialize mais de um objeto
        serializer = RegionSerializer(region, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # O RegionSerializer verifica se o request.data do POST é válido ao RegionSerializer
        serializer = RegionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            #Caso o serializer for válido, retorna o .data salvo.
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def region_detail(request, pk):
    #Recebe o pk argumento da urls.py e busca no queryset se há objetos com a pk recebida
    try:
        region = Region.objects.get(pk=pk)
    #Caso não exista, retorna o erro.
    except Region.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        #Serializa apenas um objeto do argumento recebido
        serializer = RegionSerializer(region)
        return Response(serializer.data)

    #Altera as informações do objeto do argumento recebido com a .data postado
    elif request.method == 'PUT':
        serializer = RegionSerializer(region, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #Deleta o objeto argumentado
    elif request.method == 'DELETE':
        region.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#---------------------------------------------------------------------------------------------------------#

@api_view(['GET', 'POST'])
def fruit_list(request):
    if request.method == 'GET':
        #Seleciona todos objectos do model Region
        fruit = Fruit.objects.all()
        #Serializer funciona como Modelform do django, porém o Serializer retorna em modo JSON
        #O many=True significa que permite o serializer ter mais de um object
        serializer = FruitSerializer(fruit, many=True)
            #O serializer.data é semelhante ao .POST do django
        return Response(serializer.data)


    elif request.method == 'POST':
        serializer = FruitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
def fruit_detail(request, pk):
    try:
        fruit = Fruit.objects.get(pk=pk)
    except Fruit.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FruitSerializer(fruit)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = FruitSerializer(fruit, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    elif request.method == 'DELETE':
        fruit.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

